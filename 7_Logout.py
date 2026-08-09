import streamlit as st
import time

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Logout",
    page_icon="🚪",
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
# HEADER
# =====================================================

st.markdown("""
<div class="dashboard-banner">

<h1 style="color:white;">
🚪 Logout
</h1>

<h3 style="color:white;">
Sistem Pemantauan Kualitas Tauge
</h3>

<p style="color:white;">
Terima kasih telah menggunakan aplikasi SIPETA.
Anda akan diarahkan kembali ke halaman login.
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# PROSES LOGOUT
# =====================================================

st.session_state.clear()

st.success("✅ Logout berhasil.")

with st.spinner("Mengalihkan ke halaman login..."):
    time.sleep(2)

st.switch_page("pages/0_Login.py")