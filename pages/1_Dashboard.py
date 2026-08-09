import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

from datetime import datetime

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from utils.database import koneksi

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Dashboard SIPETA",
    page_icon="🌱",
    layout="wide"
)

# =====================================================
# LOGIN
# =====================================================

if "logged_in" not in st.session_state:
    st.switch_page("pages/0_Login.py")

# =====================================================
# LOAD CSS
# =====================================================

try:
    with open("assets/style.css", encoding="utf-8") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# =====================================================
# LOAD DATASET
# =====================================================

try:

    df_latih = pd.read_csv("dataset_tauge_2000.csv")

    total_data = len(df_latih)

except:

    df_latih = pd.DataFrame()

    total_data = 0

# =====================================================
# LOAD MODEL
# =====================================================

akurasi = 0

try:

    model = joblib.load("model_naive_bayes.pkl")

    encoder = joblib.load("label_encoder.pkl")

    data = df_latih.copy()

    for kolom in [
        "warna",
        "akar",
        "kelembaban",
        "kualitas"
    ]:

        data[kolom] = encoder[kolom].transform(
            data[kolom]
        )

    X = data[
        [
            "umur",
            "panjang",
            "warna",
            "akar",
            "kelembaban"
        ]
    ]

    y = data["kualitas"]

    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=0.2,

        random_state=42,

        stratify=y

    )

    hasil = model.predict(X_test)

    akurasi = accuracy_score(
        y_test,
        hasil
    ) * 100

except:
    pass

# =====================================================
# LOAD DATA RIWAYAT
# =====================================================

try:

    conn = koneksi()

    df = pd.read_sql(

        "SELECT * FROM hasil_prediksi",

        conn

    )

    conn.close()

except:

    df = pd.DataFrame()

total_klasifikasi = len(df)

# =====================================================
# HEADER
# =====================================================

now = datetime.now()

jam = now.strftime("%H:%M")

tanggal = now.strftime("%d %B %Y")

username = st.session_state.get(
    "username",
    "Administrator"
)

st.markdown(f"""

<div class="dashboard-banner">

<h1>🌱 SIPETA</h1>

<h2>Sistem Pemantauan Kualitas Tauge</h2>

<p>

Selamat datang di SIPETA merupakan aplikasi berbasis web yang dirancang untuk membantu proses klasifikasi kualitas tauge. Aplikasi ini menyediakan fitur pengelolaan data latih, klasifikasi, riwayat klasifikasi, dan evaluasi model guna menghasilkan informasi yang cepat dan akurat

<b>{username}</b>

</p>

<p>

📅 {tanggal}

&nbsp;&nbsp;&nbsp;

🕒 {jam} WIB

</p>

</div>

""", unsafe_allow_html=True)

st.write("")

# =====================================================
# CARD
# =====================================================

a,b,c,d = st.columns(4)

with a:

    st.markdown(f"""

<div class="card-stat">

<div class="icon">

📁

</div>

<h3>Dataset</h3>

<h1>{total_data}</h1>

<p>Data Latih</p>

</div>

""",unsafe_allow_html=True)

with b:

    st.markdown(f"""

<div class="card-stat">

<div class="icon">

🌱

</div>

<h3>Klasifikasi</h3>

<h1>{total_klasifikasi}</h1>

<p>Riwayat</p>

</div>

""",unsafe_allow_html=True)

with c:

    st.markdown(f"""

<div class="card-stat">

<div class="icon">

🎯

</div>

<h3>Akurasi</h3>

<h1>{akurasi:.2f}%</h1>

<p>Model</p>

</div>

""",unsafe_allow_html=True)

with d:

    st.markdown("""

<div class="card-stat">

<div class="icon">

🧠

</div>

<h3>Algoritma</h3>

<h1>GaussianNB</h1>

<p>Klasifikasi</p>

</div>

""",unsafe_allow_html=True)

# =====================================================
# INFORMASI SISTEM
# =====================================================

st.write("")

st.markdown("## 📌 Informasi Sistem")

x,y = st.columns(2)

with x:

    st.success("""

### Sistem

✔ Pemantauan Kualitas Tauge

✔ Berbasis Web

✔ Streamlit

✔ Python

""")

with y:

    st.success("""

### Teknologi

✔ Gaussian Naive Bayes

✔ MySQL

✔ Plotly

✔ Dataset CSV

""")
    
# =====================================================
# VISUALISASI DATA
# =====================================================

st.write("")

st.markdown("""
<h2 style='color:#2E7D32'>
📊 Dashboard Analitik
</h2>
""", unsafe_allow_html=True)

if not df.empty:

    try:
        df["tanggal"] = pd.to_datetime(df["tanggal"])
    except:
        pass

    kiri, kanan = st.columns(2)

    # =====================================================
    # PIE CHART
    # =====================================================

    with kiri:

        st.markdown("""
<div class="chart-card">
<h3>Distribusi Kualitas Tauge</h3>
</div>
""", unsafe_allow_html=True)

        pie = px.pie(

            df,

            names="hasil",

            hole=0.60,

            color="hasil",

            color_discrete_sequence=[
                "#2E7D32",
                "#43A047",
                "#81C784"
            ]

        )

        pie.update_traces(

            textposition="inside",

            textinfo="percent+label"

        )

        pie.update_layout(

            height=430,

            showlegend=True,

            paper_bgcolor="white",

            plot_bgcolor="white",

            margin=dict(
                l=10,
                r=10,
                t=30,
                b=10
            ),

            font=dict(
                family="Poppins",
                size=14
            )

        )

        st.plotly_chart(
            pie,
            use_container_width=True
        )

    # =====================================================
    # BAR CHART
    # =====================================================

    with kanan:

        st.markdown("""
<div class="chart-card">
<h3>Jumlah Data Tiap Kelas</h3>
</div>
""", unsafe_allow_html=True)

        grafik = (

            df["hasil"]

            .value_counts()

            .reset_index()

        )

        grafik.columns = [

            "Kualitas",

            "Jumlah"

        ]

        bar = px.bar(

            grafik,

            x="Kualitas",

            y="Jumlah",

            text="Jumlah",

            color="Kualitas",

            color_discrete_sequence=[
                "#2E7D32",
                "#43A047",
                "#81C784"
            ]

        )

        bar.update_traces(

            textposition="outside"

        )

        bar.update_layout(

            height=430,

            paper_bgcolor="white",

            plot_bgcolor="white",

            showlegend=False,

            margin=dict(
                l=10,
                r=10,
                t=30,
                b=10
            ),

            font=dict(
                family="Poppins",
                size=14
            )

        )

        st.plotly_chart(

            bar,

            use_container_width=True

        )

    # =====================================================
    # LINE CHART
    # =====================================================

    st.write("")

    st.markdown("""
<h2 style='color:#2E7D32'>
📈 Grafik Klasifikasi Harian
</h2>
""", unsafe_allow_html=True)

    harian = (

        df.groupby(

            df["tanggal"].dt.date

        )

        .size()

        .reset_index(name="Jumlah")

    )

    harian.columns = [

        "Tanggal",

        "Jumlah"

    ]

    line = px.line(

        harian,

        x="Tanggal",

        y="Jumlah",

        markers=True,

        line_shape="spline",

        color_discrete_sequence=[
            "#2E7D32"
        ]

    )

    line.update_traces(

        line=dict(width=5),

        marker=dict(size=9)

    )

    line.update_layout(

        height=450,

        paper_bgcolor="white",

        plot_bgcolor="white",

        margin=dict(
            l=10,
            r=10,
            t=20,
            b=10
        ),

        font=dict(
            family="Poppins",
            size=14
        )

    )

    st.plotly_chart(

        line,

        use_container_width=True

    )

else:

    st.warning(

        "Belum ada data klasifikasi."

    )
# =====================================================
# RINGKASAN HASIL
# =====================================================

st.write("")

st.markdown("""
<h2 style="color:#2E7D32;">
📌 Ringkasan Hasil Klasifikasi
</h2>
""", unsafe_allow_html=True)

if not df.empty:

    kiri, kanan = st.columns(2)

    with kiri:

        jumlah = df["hasil"].value_counts()

        for kelas in jumlah.index:

            total = jumlah[kelas]

            persen = (total / len(df)) * 100

            st.write(f"**{kelas}**")

            st.progress(int(persen))

            st.caption(f"{total} Data ({persen:.2f}%)")

    with kanan:

        st.success(f"""

### Total Data

{len(df)}

""")

        st.info(f"""

### Total Dataset

{total_data}

""")

        st.warning(f"""

### Akurasi

{akurasi:.2f} %

""")

else:

    st.info("Belum ada data.")

st.divider()

# =====================================================
# RIWAYAT TERBARU
# =====================================================

st.markdown("""
<h2 style="color:#2E7D32;">
📋 10 Riwayat Klasifikasi Terbaru
</h2>
""", unsafe_allow_html=True)

if not df.empty:

    tampil = (

        df.sort_values(

            by="tanggal",

            ascending=False

        )

        .head(10)

    )

    st.dataframe(

        tampil,

        use_container_width=True,

        hide_index=True

    )

    # ==========================================
    # DOWNLOAD EXCEL
    # ==========================================

    excel = tampil.to_csv(index=False).encode("utf-8")

    st.download_button(

        "📥 Download Data",

        excel,

        "riwayat_klasifikasi.csv",

        "text/csv",

        use_container_width=True

    )

else:

    st.warning("Belum ada riwayat.")

st.divider()

