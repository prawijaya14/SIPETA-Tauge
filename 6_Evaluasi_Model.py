import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from utils.database import koneksi

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(

    page_title="Evaluasi Model",

    page_icon="📈",

    layout="wide"

)

# =====================================================
# LOAD CSS
# =====================================================

try:

    with open("assets/style.css", encoding="utf-8") as css:

        st.markdown(

            f"<style>{css.read()}</style>",

            unsafe_allow_html=True

        )

except FileNotFoundError:

    st.warning("File style.css tidak ditemukan.")

# =====================================================
# LOGIN
# =====================================================

if "logged_in" not in st.session_state:

    st.switch_page("pages/0_Login.py")

# =====================================================
# HEADER
# =====================================================

st.markdown("""

<div class="dashboard-banner">

<h1 style="color:white;">
📈 Evaluasi Model
</h1>

<h3 style="color:white;">
Gaussian Naive Bayes
</h3>

<p style="color:white;">

Halaman ini digunakan untuk mengevaluasi performa
model Gaussian Naive Bayes dalam mengklasifikasikan
kualitas tauge berdasarkan data uji.

Evaluasi dilakukan menggunakan
Accuracy,
Precision,
Recall,
F1-Score,
Confusion Matrix
dan
Classification Report.

</p>

</div>

""", unsafe_allow_html=True)

st.write("")

# =====================================================
# LOAD DATASET
# =====================================================

try:

    conn = koneksi()

    df = pd.read_sql(

        "SELECT * FROM data_latih",

        conn

    )

    conn.close()

except Exception as e:

    st.error(f"Gagal mengambil data : {e}")

    st.stop()

if df.empty:

    st.warning("Dataset belum tersedia.")

    st.stop()

# =====================================================
# HAPUS ID
# =====================================================

if "id" in df.columns:

    df = df.drop(columns=["id"])

# =====================================================
# LOAD MODEL
# =====================================================

try:

    model = joblib.load(
        "model_naive_bayes.pkl"
    )

    encoder = joblib.load(
        "label_encoder.pkl"
    )

except FileNotFoundError:

    st.error("""
Model Gaussian Naive Bayes belum tersedia.

Silakan lakukan proses **Latih Model**
terlebih dahulu pada menu **Data Latih**.
""")

    st.stop()

except Exception as e:

    st.error(f"Gagal memuat model : {e}")

    st.stop()

# =====================================================
# ENCODING DATA
# =====================================================

for kolom in [

    "warna",

    "akar",

    "kelembaban",

    "kualitas"

]:

    try:

        df[kolom] = encoder[kolom].transform(
            df[kolom]
        )

    except Exception as e:

        st.error(f"Gagal melakukan encoding pada kolom {kolom}")

        st.stop()

# =====================================================
# MEMISAHKAN DATA
# =====================================================

X = df[
    [
        "umur",
        "panjang",
        "warna",
        "akar",
        "kelembaban"
    ]
]

y = df["kualitas"]

# =====================================================
# SPLIT DATA TRAINING & TESTING
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

# =====================================================
# PROSES KLASIFIKASI
# =====================================================

y_pred = model.predict(X_test)

# =====================================================
# PERHITUNGAN METRIK EVALUASI
# =====================================================

akurasi = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(

    y_test,

    y_pred,

    average="weighted"

)

recall = recall_score(

    y_test,

    y_pred,

    average="weighted"

)

f1 = f1_score(

    y_test,

    y_pred,

    average="weighted"

)

# =====================================================
# INFORMASI DATASET
# =====================================================

st.markdown("""
<h2 style='color:black'>
📚 Informasi Dataset
</h2>
""", unsafe_allow_html=True)

info1, info2, info3, info4 = st.columns(4)

with info1:

    st.markdown(f"""
<div class="custom-card">

<h4 style="color:black;">📚 Total Dataset</h4>

<h2 style="color:#0B5D1E;">
{len(df)}
</h2>

<p style="color:black;">
Data
</p>

</div>
""", unsafe_allow_html=True)

with info2:

    st.markdown(f"""
<div class="custom-card">

<h4 style="color:black;">🧪 Data Training</h4>

<h2 style="color:#0B5D1E;">
{len(X_train)}
</h2>

<p style="color:black;">
Data
</p>

</div>
""", unsafe_allow_html=True)

with info3:

    st.markdown(f"""
<div class="custom-card">

<h4 style="color:black;">🔬 Data Testing</h4>

<h2 style="color:#0B5D1E;">
{len(X_test)}
</h2>

<p style="color:black;">
Data
</p>

</div>
""", unsafe_allow_html=True)

with info4:

    st.markdown("""
<div class="custom-card">

<h4 style="color:black;">
🤖 Model
</h4>

<h3 style="color:#0B5D1E;">
Gaussian
Naive Bayes
</h3>

</div>
""", unsafe_allow_html=True)

st.divider()

# =====================================================
# HASIL EVALUASI MODEL
# =====================================================

st.markdown("""
<h2 style="color:#000000;">
📊 Hasil Evaluasi Model
</h2>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(f"""

    <div style="
        background:white;
        padding:25px;
        border-radius:18px;
        text-align:center;
        box-shadow:0 5px 15px rgba(0,0,0,.10);
        border-left:6px solid #0B5D1E;
    ">

    <h4 style="color:#444;">🎯 Accuracy</h4>

    <h1 style="
        color:#0B5D1E;
        font-size:38px;
        font-weight:bold;
    ">

    {akurasi*100:.2f}%

    </h1>

    </div>

    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""

    <div style="
        background:white;
        padding:25px;
        border-radius:18px;
        text-align:center;
        box-shadow:0 5px 15px rgba(0,0,0,.10);
        border-left:6px solid #2E7D32;
    ">

    <h4 style="color:#444;">📌 Precision</h4>

    <h1 style="
        color:#2E7D32;
        font-size:38px;
        font-weight:bold;
    ">

    {precision*100:.2f}%

    </h1>

    </div>

    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""

    <div style="
        background:white;
        padding:25px;
        border-radius:18px;
        text-align:center;
        box-shadow:0 5px 15px rgba(0,0,0,.10);
        border-left:6px solid #43A047;
    ">

    <h4 style="color:#444;">📈 Recall</h4>

    <h1 style="
        color:#43A047;
        font-size:38px;
        font-weight:bold;
    ">

    {recall*100:.2f}%

    </h1>

    </div>

    """, unsafe_allow_html=True)

with col4:

    st.markdown(f"""

    <div style="
        background:white;
        padding:25px;
        border-radius:18px;
        text-align:center;
        box-shadow:0 5px 15px rgba(0,0,0,.10);
        border-left:6px solid #66BB6A;
    ">

    <h4 style="color:#444;">⭐ F1 Score</h4>

    <h1 style="
        color:#66BB6A;
        font-size:38px;
        font-weight:bold;
    ">

    {f1*100:.2f}%

    </h1>

    </div>

    """, unsafe_allow_html=True)

st.divider()

# =====================================================
# GRAFIK EVALUASI MODEL
# =====================================================

st.markdown("""
<h2 style="color:#000000;">
📊 Grafik Evaluasi Model
</h2>
""", unsafe_allow_html=True)

grafik = pd.DataFrame({

    "Metrik":[

        "Accuracy",

        "Precision",

        "Recall",

        "F1 Score"

    ],

    "Nilai":[

        round(akurasi*100,2),

        round(precision*100,2),

        round(recall*100,2),

        round(f1*100,2)

    ]

})

fig = px.bar(

    grafik,

    x="Metrik",

    y="Nilai",

    text="Nilai",

    color="Metrik",

    color_discrete_map={

        "Accuracy":"#0B5D1E",

        "Precision":"#2E7D32",

        "Recall":"#43A047",

        "F1 Score":"#66BB6A"

    }

)

fig.update_traces(

    texttemplate="%{text:.2f} %",

    textposition="outside",

    marker_line_color="black",

    marker_line_width=1

)

fig.update_layout(

    height=500,

    showlegend=False,

    plot_bgcolor="white",

    paper_bgcolor="white",

    font=dict(

        color="black",

        size=15

    ),

    xaxis=dict(

        title="",

        tickfont=dict(

            color="black",

            size=14

        ),

        showgrid=False

    ),

    yaxis=dict(

        title="Persentase (%)",

        tickfont=dict(

            color="black",

            size=14

        ),

        range=[0,100],

        gridcolor="#E0E0E0"

    ),

    margin=dict(

        l=30,

        r=30,

        t=20,

        b=20

    )

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# =====================================================
# CONFUSION MATRIX
# =====================================================

st.markdown("""
<h2 style="color:#000000;">
🧩 Confusion Matrix
</h2>
""", unsafe_allow_html=True)

cm = confusion_matrix(

    y_test,

    y_pred

)

cm_df = pd.DataFrame(

    cm,

    index=encoder["kualitas"].classes_,

    columns=encoder["kualitas"].classes_

)

heatmap = px.imshow(

    cm_df,

    text_auto=True,

    color_continuous_scale=[

        "#F1F8E9",

        "#AED581",

        "#66BB6A",

        "#2E7D32",

        "#0B5D1E"

    ],

    aspect="auto"

)

heatmap.update_layout(

    height=550,

    plot_bgcolor="white",

    paper_bgcolor="white",

    font=dict(

        color="black",

        size=15

    ),

    xaxis_title="Prediksi",

    yaxis_title="Data Aktual"

)

st.plotly_chart(

    heatmap,

    use_container_width=True

)

st.divider()