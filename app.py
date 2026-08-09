import streamlit as st

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================
st.set_page_config(
    page_title="SIPETA",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
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
    pass

# =====================================================
# CEK LOGIN
# =====================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =====================================================
# JIKA SUDAH LOGIN
# =====================================================
if st.session_state.logged_in:
    st.switch_page("1_Dashboard.py")

# =====================================================
# LANDING PAGE
# =====================================================
st.markdown("""
<div class="dashboard-banner">

<h1>🌱 SIPETA</h1>

<h3>Sistem Pemantauan Kualitas Tauge</h3>

<p>
Aplikasi berbasis web untuk melakukan
<b>klasifikasi kualitas tauge</b>
menggunakan algoritma
<b>Gaussian Naive Bayes</b>.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="card-stat">

<div class="icon">📁</div>

<h3>Dataset</h3>

<p>Import Dataset CSV</p>

</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card-stat">

<div class="icon">🧠</div>

<h3>Algoritma</h3>

<p>Gaussian Naive Bayes</p>

</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card-stat">

<div class="icon">🌱</div>

<h3>Klasifikasi</h3>

<p>Kualitas Tauge</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.divider()

st.subheader("Tentang SIPETA")

st.write("""
SIPETA merupakan aplikasi berbasis web yang digunakan
untuk membantu proses klasifikasi kualitas tauge
berdasarkan karakteristik fisiknya menggunakan
algoritma Gaussian Naive Bayes.

Aplikasi ini dikembangkan sebagai implementasi
penelitian skripsi Program Studi Teknik Informatika,
Universitas Kebangsaan Republik Indonesia.
""")

st.write("")

if st.button(
    "🔐 Masuk ke Halaman Login",
    use_container_width=True,
    type="primary"
):
    # Langsung panggil nama filenya tanpa 'pages/'
    st.switch_page("0_Login.py")

st.divider()

st.caption(
    "© 2026 SIPETA | Sistem Pemantauan Kualitas Tauge | Teknik Informatika | Universitas Kebangsaan Republik Indonesia"
)
