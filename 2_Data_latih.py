import streamlit as st
import pandas as pd
import joblib
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

from utils.database import koneksi

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Data Latih",
    page_icon="🌱",
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
📚 Data Latih
</h1>

<h3 style="color:white;">
Sistem Pemantauan Kualitas Tauge
</h3>

<p style="color:white;">

Halaman ini digunakan untuk mengelola data latih
yang digunakan pada proses pelatihan model
Gaussian Naive Bayes. Pengguna dapat melihat,
melatih, serta mengunduh dataset yang tersedia.

</p>

</div>

""", unsafe_allow_html=True)

st.write("")

# =====================================================
# AMBIL DATA DATABASE
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

# =====================================================
# TOTAL DATA
# =====================================================

total_data = len(df)

jumlah_kolom = len(df.columns)

# =====================================================
# INFORMASI MODEL
# =====================================================

st.markdown("""
<h2 style="color:black;">
ℹ️ Informasi Model
</h2>
""", unsafe_allow_html=True)

info1, info2 = st.columns(2)

with info1:

    st.info(f"""
### Gaussian Naive Bayes

✔ Digunakan untuk klasifikasi data

✔ Cepat dalam proses training

✔ Cocok untuk data numerik

✔ Ringan dijalankan pada aplikasi web

✔ Mudah diimplementasikan
""")

with info2:

    st.info(f"""
### Informasi Dataset

📊 Jumlah Data

**{total_data}**

📋 Jumlah Kolom

**{jumlah_kolom}**

🧪 Algoritma

**Gaussian Naive Bayes**
""")

st.divider()

# =====================================================
# TABEL DATA LATIH
# =====================================================

st.markdown("""
<h2 style="color:black;">
📋 Data Latih
</h2>
""", unsafe_allow_html=True)

if not df.empty:

    kiri, kanan = st.columns([3,1])

    with kiri:

        keyword = st.text_input(
            "🔍 Cari Data",
            placeholder="Masukkan kata kunci..."
        )

    with kanan:

        tampil = st.selectbox(
            "Jumlah Data",
            [10,20,50,100,len(df)],
            index=0
        )

    data_tampil = df.copy()

    if keyword:

        data_tampil = data_tampil[
            data_tampil.astype(str)
            .apply(
                lambda x: x.str.contains(
                    keyword,
                    case=False
                )
            )
            .any(axis=1)
        ]

    st.dataframe(

        data_tampil.head(tampil),

        use_container_width=True,

        hide_index=True

    )

    st.success(
        f"Total data ditemukan : {len(data_tampil)} data"
    )

else:

    st.warning(
        "Data latih belum tersedia."
    )

st.divider()

# =====================================================
# TRAINING MODEL
# =====================================================

st.markdown("""
<h2 style="color:black;">
🚀 Training Model
</h2>
""", unsafe_allow_html=True)

st.write(
    "Tekan tombol di bawah ini untuk melakukan proses pelatihan model "
    "Gaussian Naive Bayes menggunakan data latih yang tersedia."
)

if st.button(
    "🚀 Latih Model Gaussian Naive Bayes",
    use_container_width=True
):

    try:

        with st.spinner("Sedang melatih model..."):

            akurasi = train_model()

        st.success(
            f"""
Model berhasil dilatih.

Akurasi Model : **{akurasi*100:.2f}%**
"""
        )

        st.balloons()

    except Exception as e:

        st.error(
            f"Gagal melakukan training model.\n\n{e}"
        )

st.divider()

# =====================================================
# DOWNLOAD DATASET
# =====================================================

st.markdown("""
<h2 style="color:black;">
📥 Download Dataset
</h2>
""", unsafe_allow_html=True)

st.write(
    "Dataset dapat diunduh dalam format CSV untuk keperluan "
    "backup maupun analisis lebih lanjut."
)

if not df.empty:

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(

        label="📥 Download Dataset CSV",

        data=csv,

        file_name="dataset_tauge.csv",

        mime="text/csv",

        use_container_width=True

    )

else:

    st.warning(
        "Dataset belum tersedia."
    )

st.divider()

# =====================================================
# RESET DATASET
# =====================================================

st.markdown("""
<h2 style="color:black;">
🗑 Reset Dataset
</h2>
""", unsafe_allow_html=True)

st.warning(
    """
Menghapus file CSV hanya akan menghapus file dataset
yang tersimpan di komputer.

Data pada database **tidak akan ikut terhapus**.
"""
)

if st.button(
    "🗑 Hapus Dataset CSV",
    use_container_width=True
):

    if os.path.exists("dataset_tauge.csv"):

        os.remove("dataset_tauge.csv")

        st.success(
            "Dataset CSV berhasil dihapus."
        )

        st.rerun()

    else:

        st.error(
            "File dataset tidak ditemukan."
        )

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown("""

<div class="footer">

<h3>🌱 SIPETA</h3>

<p>
Sistem Pemantauan Kualitas Tauge
</p>

<br>

<p>
Metode Klasifikasi
</p>

<b>Gaussian Naive Bayes</b>

<br><br>

<p>
Program Studi Teknik Informatika
</p>

<p>
Fakultas Ilmu Komputer dan Sistem Informasi
</p>

<p>
Universitas Kebangsaan Republik Indonesia
</p>

<br>

<p>
© 2026 SIPETA
</p>

</div>

""", unsafe_allow_html=True)