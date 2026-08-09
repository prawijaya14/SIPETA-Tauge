import streamlit as st

# ============================================
# KONFIGURASI HALAMAN
# ============================================

st.set_page_config(
    page_title="Login SIPETA",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================
# LOAD CSS
# ============================================

try:
    with open("assets/style.css", encoding="utf-8") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# ============================================
# SESSION
# ============================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ============================================
# SUDAH LOGIN
# ============================================

if st.session_state.logged_in:
    st.switch_page("pages/1_Dashboard.py")

# ============================================
# TAMPILAN LOGIN
# ============================================

st.markdown("""
<div class="login-card">

<img src="data:image/png;base64," width="120">

<h1>🌱 SIPETA</h1>

<h3>Sistem Pemantauan Kualitas Tauge</h3>

<p>
Silakan login untuk masuk ke sistem.
</p>

</div>
""", unsafe_allow_html=True)

# ============================================
# FORM LOGIN
# ============================================

with st.form("login_form"):

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    login = st.form_submit_button(
        "LOGIN",
        use_container_width=True
    )

# ============================================
# PROSES LOGIN
# ============================================

if login:

    if username == "admin" and password == "admin123":

        st.session_state.logged_in = True

        st.session_state.username = username

        st.success("Login berhasil...")

        st.switch_page("pages/1_Dashboard.py")

    else:

        st.error(
            "Username atau Password salah!"
        )

# ============================================
# FOOTER
# ============================================

st.write("")
st.divider()

st.caption(
    "© 2026 SIPETA | Teknik Informatika | Universitas Kebangsaan Republik Indonesia"
)