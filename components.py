import streamlit as st


# ===========================================
# LOAD CSS
# ===========================================

def load_css():

    with open("assets/style.css", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# ===========================================
# BANNER
# ===========================================

def banner(title, subtitle=""):

    st.markdown(f"""
    <div class="banner">

        <h1>{title}</h1>

        <p>{subtitle}</p>

    </div>
    """, unsafe_allow_html=True)


# ===========================================
# CARD
# ===========================================

def card(title, value, icon="📊"):

    st.markdown(f"""
    <div class="card">

        <div class="card-icon">
            {icon}
        </div>

        <div class="card-title">
            {title}
        </div>

        <div class="card-value">
            {value}
        </div>

    </div>
    """, unsafe_allow_html=True)


# ===========================================
# INFO CARD
# ===========================================

def info_card(title, isi):

    st.markdown(f"""
    <div class="info-card">

        <h3>{title}</h3>

        <p>{isi}</p>

    </div>
    """, unsafe_allow_html=True)


# ===========================================
# SUCCESS CARD
# ===========================================

def success_card(title):

    st.markdown(f"""
    <div class="success-card">

    ✅ {title}

    </div>
    """, unsafe_allow_html=True)


# ===========================================
# WARNING CARD
# ===========================================

def warning_card(title):

    st.markdown(f"""
    <div class="warning-card">

    ⚠ {title}

    </div>
    """, unsafe_allow_html=True)


# ===========================================
# ERROR CARD
# ===========================================

def error_card(title):

    st.markdown(f"""
    <div class="error-card">

    ❌ {title}

    </div>
    """, unsafe_allow_html=True)


# ===========================================
# STATUS BADGE
# ===========================================

def status_badge(status):

    warna = "#43A047"

    if status.lower() == "sedang":
        warna = "#FB8C00"

    elif status.lower() == "buruk":
        warna = "#E53935"

    st.markdown(f"""
    <div style="

        background:{warna};

        color:white;

        padding:10px;

        text-align:center;

        border-radius:20px;

        font-weight:bold;

        font-size:20px;

    ">

        {status.upper()}

    </div>
    """, unsafe_allow_html=True)


# ===========================================
# SECTION TITLE
# ===========================================

def section(title):

    st.markdown(f"""
    <h2 style='
    color:#2E7D32;
    margin-top:20px;
    '>
    {title}
    </h2>
    """, unsafe_allow_html=True)


# ===========================================
# FOOTER
# ===========================================

def footer():

    st.markdown("""

    <hr>

    <center>

    🌱 <b>SIPETA</b>

    <br>

    Sistem Klasifikasi Kualitas Tauge

    <br>

    Teknik Informatika

    <br>

    Universitas Kebangsaan Republik Indonesia

    <br><br>

    © 2026

    </center>

    """, unsafe_allow_html=True)