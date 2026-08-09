import streamlit as st
from pathlib import Path

# Mendapatkan lokasi direktori tempat app.py berada
BASE_DIR = Path(__file__).parent

# Menentukan lokasi file halaman
login_path = BASE_DIR / "pages" / "0_Login.py"
dashboard_path = BASE_DIR / "pages" / "1_Dashboard.py"

# =====================================================
# DEKLARASI HALAMAN
# =====================================================
login_page = st.Page(str(login_path), title="Login", icon="🔐")
dashboard_page = st.Page(str(dashboard_path), title="Dashboard", icon="📊")

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================
st.set_page_config(
    page_title="SIPETA",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ... (sisa kode di bawahnya tetap sama)
