import streamlit as st
import pandas as pd
import os

from utils.database import koneksi

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Riwayat Klasifikasi",
    page_icon="📜",
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
# HEADER
# =====================================================

st.markdown("""

<div class="dashboard-banner">

<h1 style="color:white;">
📜 Riwayat Klasifikasi
</h1>

<h3 style="color:white;">
Gaussian Naive Bayes
</h3>

<p style="color:white;">

Halaman ini menampilkan seluruh riwayat hasil
klasifikasi kualitas tauge yang telah dilakukan.
Setiap riwayat menyimpan foto tauge, data
karakteristik, hasil klasifikasi, serta tanggal
proses klasifikasi.

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
        """
        SELECT
            id,
            foto,
            umur,
            panjang,
            warna,
            akar,
            kelembaban,
            hasil,
            tanggal
        FROM hasil_klasifikasi
        ORDER BY tanggal DESC
        """,
        conn
    )

    conn.close()

except Exception as e:

    st.error(f"Gagal mengambil data : {e}")

    st.stop()

# =====================================================
# INFORMASI DATA
# =====================================================

total_data = len(df)

info1, info2 = st.columns(2)

with info1:

    st.info(f"""
### 📊 Total Riwayat

**{total_data}** Data Klasifikasi
""")

with info2:

    st.info("""
### 🧠 Metode

Gaussian Naive Bayes

Status Database

✅ Terhubung
""")

st.divider()

# =====================================================
# FILTER DATA
# =====================================================

st.subheader("🔍 Pencarian Data")

col1, col2, col3 = st.columns([3,2,1])

with col1:

    keyword = st.text_input(
        "Cari Hasil Klasifikasi",
        placeholder="Contoh : Baik, Sedang, Buruk..."
    )

with col2:

    tanggal = st.date_input(
        "Filter Tanggal",
        value=None
    )

with col3:

    st.write("")
    st.write("")

    reset = st.button(
        "🔄 Reset",
        use_container_width=True
    )

# =====================================================
# FILTER
# =====================================================

data_filter = df.copy()

if keyword:

    data_filter = data_filter[
        data_filter["hasil"]
        .astype(str)
        .str.contains(
            keyword,
            case=False,
            na=False
        )
    ]

if tanggal:

    data_filter = data_filter[
        pd.to_datetime(
            data_filter["tanggal"]
        ).dt.date == tanggal
    ]

if reset:

    data_filter = df.copy()

st.success(
    f"Menampilkan {len(data_filter)} data."
)

st.divider()

# =====================================================
# RIWAYAT KLASIFIKASI
# =====================================================

st.subheader("📋 Riwayat Hasil Klasifikasi")

if data_filter.empty:

    st.warning("Belum ada data klasifikasi.")

else:

    for index, row in data_filter.iterrows():

        with st.container():

            kiri, kanan = st.columns([1,3])

            # =====================================
            # FOTO TAUGE
            # =====================================

            with kiri:

                if pd.notna(row["foto"]):

                    lokasi_foto = os.path.join(
                        "assets",
                        "hasil_klasifikasi",
                        row["foto"]
                    )

                    if os.path.exists(lokasi_foto):

                        st.image(
                            lokasi_foto,
                            caption="Foto Tauge",
                            use_container_width=True
                        )

                    else:

                        st.warning("Foto tidak ditemukan.")

                else:

                    st.info("Tidak ada foto.")

            # =====================================
            # DETAIL HASIL
            # =====================================

            with kanan:

                st.markdown(f"""
<div style="
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 10px rgba(0,0,0,0.1);
">

<h3 style="color:#0B5D1E;">
🌱 Hasil Klasifikasi : {row['hasil']}
</h3>

</div>

""", unsafe_allow_html=True)

                info1, info2 = st.columns(2)

                with info1:

                    st.write(f"**Umur** : {row['umur']} Hari")

                    st.write(f"**Panjang** : {row['panjang']} cm")

                    st.write(f"**Warna** : {row['warna']}")

                with info2:

                    st.write(f"**Akar** : {row['akar']}")

                    st.write(f"**Kelembaban** : {row['kelembaban']}")

                    st.write(f"**Tanggal** : {row['tanggal']}")

        st.divider()

st.success(f"Total Riwayat Ditampilkan : {len(data_filter)} Data")

# =====================================================
# DOWNLOAD RIWAYAT
# =====================================================

st.subheader("📥 Download Riwayat")

csv = data_filter.to_csv(
    index=False
).encode("utf-8")

st.download_button(

    label="📥 Download Riwayat CSV",

    data=csv,

    file_name="riwayat_klasifikasi.csv",

    mime="text/csv",

    use_container_width=True

)

st.divider()

# =====================================================
# HAPUS SATU DATA
# =====================================================

st.subheader("🗑 Hapus Salah Satu Riwayat")

if not data_filter.empty:

    pilihan = st.selectbox(

        "Pilih ID Riwayat",

        data_filter["id"]

    )

    if st.button(

        "🗑 Hapus Data Terpilih",

        use_container_width=True

    ):

        try:

            conn = koneksi()

            cursor = conn.cursor()

            # Ambil nama file foto
            cursor.execute(
                """
                SELECT foto
                FROM hasil_klasifikasi
                WHERE id=%s
                """,
                (pilihan,)
            )

            hasil = cursor.fetchone()

            if hasil:

                nama_foto = hasil[0]

                if nama_foto:

                    lokasi = os.path.join(

                        "assets",

                        "hasil_klasifikasi",

                        nama_foto

                    )

                    if os.path.exists(lokasi):

                        os.remove(lokasi)

            # Hapus data database
            cursor.execute(

                """
                DELETE FROM hasil_klasifikasi
                WHERE id=%s
                """,

                (pilihan,)

            )

            conn.commit()

            cursor.close()

            conn.close()

            st.success("Riwayat berhasil dihapus.")

            st.rerun()

        except Exception as e:

            st.error(e)

else:

    st.info("Belum ada data.")

st.divider()

# =====================================================
# HAPUS SEMUA RIWAYAT
# =====================================================

st.subheader("🗑 Hapus Semua Riwayat")

st.warning("""

Semua data klasifikasi beserta foto
akan dihapus secara permanen.

""")

if st.button(

    "🗑 Hapus Semua Riwayat",

    type="primary",

    use_container_width=True

):

    try:

        # Hapus semua foto
        folder = "assets/hasil_klasifikasi"

        if os.path.exists(folder):

            for file in os.listdir(folder):

                os.remove(

                    os.path.join(

                        folder,

                        file

                    )

                )

        conn = koneksi()

        cursor = conn.cursor()

        cursor.execute(

            "DELETE FROM hasil_klasifikasi"

        )

        conn.commit()

        cursor.close()

        conn.close()

        st.success(

            "Seluruh riwayat berhasil dihapus."

        )

        st.balloons()

        st.rerun()

    except Exception as e:

        st.error(e)

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