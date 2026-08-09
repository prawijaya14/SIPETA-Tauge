import streamlit as st
import os

import streamlit as st
import os

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Tentang SIPETA",
    page_icon="ℹ️",
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
ℹ️ Tentang SIPETA
</h1>

<h3 style="color:white;">
Sistem Pemantauan Kualitas Tauge
</h3>

<p style="color:white;">

Halaman ini berisi informasi mengenai aplikasi SIPETA,
algoritma yang digunakan, tujuan pengembangan sistem,
serta informasi penelitian.

</p>

</div>

""", unsafe_allow_html=True)

# =====================================================
# LOGO
# =====================================================

st.markdown(
    "<h2 style='color:black;'>🌱 Logo Aplikasi</h2>",
    unsafe_allow_html=True
)

if os.path.exists("assets/SIPETA.png"):

    _, tengah, _ = st.columns([1,2,1])

    with tengah:
        st.image(
            "assets/SIPETA.png",
            width=250
        )

else:

    st.warning("Logo SIPETA belum tersedia.")

st.divider()

# =====================================================
# DESKRIPSI
# =====================================================

st.markdown(
    "<h2 style='color:black;'>📖 Deskripsi Aplikasi</h2>",
    unsafe_allow_html=True
)

st.write("""

SIPETA (Sistem Pemantauan Kualitas Tauge) merupakan
aplikasi berbasis web yang dikembangkan untuk membantu
proses klasifikasi kualitas tauge menggunakan algoritma
Gaussian Naive Bayes.

Aplikasi ini mampu mengelola data latih, melakukan
klasifikasi kualitas tauge, menyimpan riwayat hasil
klasifikasi, serta mengevaluasi performa model.

""")

st.divider()

# =====================================================
# PARAMETER
# =====================================================

st.markdown(
    "<h2 style='color:black;'>📌 Parameter Klasifikasi</h2>",
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:

    st.success("✔ Umur")

    st.success("✔ Panjang")

    st.success("✔ Warna")

with c2:

    st.success("✔ Akar")

    st.success("✔ Kelembaban")

    st.success("✔ Kualitas")

st.divider()

# =====================================================
# ALGORITMA
# =====================================================

st.markdown(
    "<h2 style='color:black;'>🧠 Algoritma</h2>",
    unsafe_allow_html=True
)

st.info("""

Gaussian Naive Bayes merupakan algoritma klasifikasi
berdasarkan Teorema Bayes yang mengasumsikan setiap
atribut bersifat independen.

Pada SIPETA algoritma ini digunakan untuk
mengklasifikasikan kualitas tauge menjadi:

🟢 Baik

🟡 Sedang

🔴 Buruk

""")

st.divider()

# =====================================================
# INFORMASI PENELITIAN
# =====================================================

st.markdown(
    "<h2 style='color:black;'>🎓 Informasi Penelitian</h2>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.write("**Nama Mahasiswa**")
    st.write("Trisna Prawijaya")

    st.write("**Program Studi**")
    st.write("Teknik Informatika")

    st.write("**Fakultas**")
    st.write("Fakultas Ilmu Komputer dan Sistem Informasi")

with col2:

    st.write("**Universitas**")
    st.write("Universitas Kebangsaan Republik Indonesia")

    st.write("**Metode**")
    st.write("Gaussian Naive Bayes")

    st.write("**Tahun**")
    st.write("2026")

st.divider()

# =====================================================
# TUJUAN
# =====================================================

st.markdown(
    "<h2 style='color:black;'>🎯 Tujuan Sistem</h2>",
    unsafe_allow_html=True
)

st.write("""

Membantu proses klasifikasi kualitas tauge berdasarkan
karakteristik fisik menggunakan algoritma Gaussian
Naive Bayes sehingga hasil klasifikasi dapat digunakan
sebagai informasi dalam proses pemantauan kualitas tauge.

""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown("""

<div class="footer">

<h3>🌱 SIPETA</h3>

<b>Sistem Pemantauan Kualitas Tauge</b>

<br><br>

Gaussian Naive Bayes

<br>

Program Studi Teknik Informatika

<br>

Universitas Kebangsaan Republik Indonesia

<br><br>

© 2026

</div>

""", unsafe_allow_html=True)