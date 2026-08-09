import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, "model_naive_bayes.pkl"))
encoder = joblib.load(os.path.join(BASE_DIR, "label_encoder.pkl"))

def prediksi(umur, panjang, warna, akar, kelembaban):

    data = pd.DataFrame({
        "umur": [umur],
        "panjang": [panjang],
        "warna": [warna],
        "akar": [akar],
        "kelembaban": [kelembaban]
    })

    # Encode data input
    for kolom in ["warna", "akar", "kelembaban"]:
        data[kolom] = encoder[kolom].transform(data[kolom])

    # Prediksi
    hasil = model.predict(data)
    probabilitas = model.predict_proba(data)

    hasil_label = encoder["kualitas"].inverse_transform(hasil)[0]

    return hasil_label, probabilitas[0], encoder["kualitas"].classes_