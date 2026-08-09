import pandas as pd
import mysql.connector

# ===============================
# Koneksi Database
# ===============================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_tauge"
)

cursor = conn.cursor()

# ===============================
# Membaca CSV
# ===============================

df = pd.read_csv("dataset_tauge_2000.csv")

print(df.head())

# ===============================
# Hapus data lama
# ===============================

cursor.execute("DELETE FROM data_latih")

# ===============================
# Simpan ke database
# ===============================

for index, row in df.iterrows():

    sql = """
    INSERT INTO data_latih
    (
        umur,
        panjang,
        warna,
        akar,
        kelembaban,
        kualitas
    )

    VALUES (%s,%s,%s,%s,%s,%s)
    """

    value = (
        int(row["umur"]),
        float(row["panjang"]),
        row["warna"],
        row["akar"],
        row["kelembaban"],
        row["kualitas"]
    )

    cursor.execute(sql, value)

conn.commit()

print("================================")
print("IMPORT BERHASIL")
print("Jumlah Data :", len(df))
print("================================")

cursor.close()
conn.close()