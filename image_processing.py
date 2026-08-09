import cv2
import numpy as np

def ekstraksi_fitur(uploaded_file):

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    img = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    tinggi, lebar = img.shape[:2]

    hsv = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2HSV
    )

    warna = "Putih"

    panjang = round(lebar / 50,2)

    akar = "Panjang"

    kelembaban = "Sedang"

    umur = 4

    return {

        "umur":umur,

        "panjang":panjang,

        "warna":warna,

        "akar":akar,

        "kelembaban":kelembaban

    }