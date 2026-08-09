import streamlit as st
import pandas as pd
import joblib
import os

from PIL import Image
from datetime import datetime

from utils.database import koneksi

# =====================================================
# KONFIGURASI
# =====================================================

st.set_page_config(
    page_title="Klasifikasi",
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
except FileNotFoundError:
    st.warning("File style.css tidak ditemukan.")

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

except:

    st.error("""
Model belum tersedia.

Silakan lakukan proses
Training Model terlebih dahulu
pada menu Data Latih.
""")

    st.stop()

# =====================================================
# HEADER
# =====================================================

st.markdown("""

<div class="dashboard-banner">

<h1 style="color:white;">
🌱 Klasifikasi Kualitas Tauge
</h1>

<h3 style="color:white;">
Gaussian Naive Bayes
</h3>

<p style="color:white;">

Silakan unggah foto tauge sebagai dokumentasi,
kemudian lengkapi karakteristik tauge untuk
melakukan proses klasifikasi kualitas.

</p>

</div>

""", unsafe_allow_html=True)

st.write("")

# =====================================================
# UPLOAD FOTO
# =====================================================

st.subheader("📷 Upload Foto Tauge")

uploaded_file = st.file_uploader(

    "Pilih Foto Tauge",

    type=["jpg", "jpeg", "png"]

)

nama_file = None

# =====================================================
# PREVIEW FOTO
# =====================================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(

        image,

        caption="Preview Foto Tauge",

        use_container_width=True

    )

    # Membuat folder jika belum ada

    os.makedirs(

        "assets/hasil_klasifikasi",

        exist_ok=True

    )

    # Nama file unik

    nama_file = (

        datetime.now().strftime("%Y%m%d_%H%M%S")

        + "_"

        + uploaded_file.name

    )

    # Simpan foto

    image.save(

        os.path.join(

            "assets/hasil_klasifikasi",

            nama_file

        )

    )

    st.success("✅ Foto berhasil diunggah.")

st.divider()

# =====================================================
# FORM INPUT DATA KLASIFIKASI
# =====================================================

st.subheader("📝 Data Karakteristik Tauge")

st.write(
    "Masukkan karakteristik tauge sesuai dengan kondisi fisiknya "
    "untuk memperoleh hasil klasifikasi."
)

kiri, kanan = st.columns(2)

# =====================================================
# INPUT KIRI
# =====================================================

with kiri:

    umur = st.number_input(

        "Umur (Hari)",

        min_value=1,

        max_value=10,

        value=3,

        step=1

    )

    panjang = st.number_input(

        "Panjang (cm)",

        min_value=1.0,

        max_value=20.0,

        value=8.0,

        step=0.1

    )

# =====================================================
# INPUT KANAN
# =====================================================

with kanan:

    warna = st.selectbox(

        "Warna",

        encoder["warna"].classes_

    )

    akar = st.selectbox(

        "Akar",

        encoder["akar"].classes_

    )

    kelembaban = st.selectbox(

        "Kelembaban",

        encoder["kelembaban"].classes_

    )

st.divider()

# =====================================================
# RINGKASAN DATA INPUT
# =====================================================

st.subheader("📋 Ringkasan Data")

ringkasan = pd.DataFrame({

    "Parameter": [

        "Umur",

        "Panjang",

        "Warna",

        "Akar",

        "Kelembaban"

    ],

    "Nilai": [

        umur,

        f"{panjang} cm",

        warna,

        akar,

        kelembaban

    ]

})

st.dataframe(

    ringkasan,

    use_container_width=True,

    hide_index=True

)

st.divider()

# =====================================================
# TOMBOL KLASIFIKASI
# =====================================================

if st.button(
    "🔍 Klasifikasikan",
    use_container_width=True
):

    try:

        with st.spinner("Sedang melakukan klasifikasi..."):

            # Encode data kategori
            warna_encode = encoder["warna"].transform([warna])[0]
            akar_encode = encoder["akar"].transform([akar])[0]
            kelembaban_encode = encoder["kelembaban"].transform([kelembaban])[0]

            # Data input
            data = pd.DataFrame([{

                "umur": umur,
                "panjang": panjang,
                "warna": warna_encode,
                "akar": akar_encode,
                "kelembaban": kelembaban_encode

            }])

            # ==========================================
            # KLASIFIKASI
            # ==========================================

            hasil = model.predict(data)[0]

            probabilitas = model.predict_proba(data)[0]

            hasil_label = encoder["kualitas"].inverse_transform([hasil])[0]

            confidence = max(probabilitas) * 100

        st.success("Klasifikasi berhasil dilakukan.")

        st.divider()

        # ==========================================
        # HASIL KLASIFIKASI
        # ==========================================

        kiri, kanan = st.columns([1,2])

        with kiri:

            if uploaded_file is not None:

                st.image(
                    image,
                    caption="Foto Tauge",
                    use_container_width=True
                )

            else:

                st.info("Foto tidak diunggah.")

        with kanan:

            st.markdown(f"""

<div class="hasil-card">

<h2 style="color:white;">
🌱 HASIL KLASIFIKASI
</h2>

<h1 style="color:white;">
{hasil_label}
</h1>

<br>

<h3 style="color:white;">
Tingkat Keyakinan
</h3>

<h2 style="color:white;">
{confidence:.2f}%
</h2>

</div>

""", unsafe_allow_html=True)

        st.divider()

        # ==========================================
        # DETAIL INPUT
        # ==========================================

        st.subheader("📋 Detail Data Klasifikasi")

        detail = pd.DataFrame({

            "Parameter":[

                "Umur",

                "Panjang",

                "Warna",

                "Akar",

                "Kelembaban",

                "Hasil",

                "Confidence"

            ],

            "Nilai":[

                umur,

                f"{panjang} cm",

                warna,

                akar,

                kelembaban,

                hasil_label,

                f"{confidence:.2f}%"

            ]

        })

        st.dataframe(

            detail,

            use_container_width=True,

            hide_index=True

        )

        st.divider()

        # ==========================================
        # SIMPAN DATABASE
        # ==========================================

        conn = koneksi()

        cursor = conn.cursor()

        cursor.execute("""

        INSERT INTO hasil_klasifikasi
        (
            umur,
            panjang,
            warna,
            akar,
            kelembaban,
            hasil,
            foto,
            tanggal
        )

        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s)

        """,

        (

            umur,

            panjang,

            warna,

            akar,

            kelembaban,

            hasil_label,

            nama_file,

            datetime.now()

        )

        )

        conn.commit()

        cursor.close()

        conn.close()

        st.success("✅ Hasil klasifikasi berhasil disimpan.")

        st.balloons()

        if st.button(
            "🔄 Klasifikasi Lagi",
            use_container_width=True
        ):
            st.rerun()

    except Exception as e:

        st.error(f"Terjadi kesalahan : {e}")