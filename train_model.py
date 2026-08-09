import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

from utils.database import koneksi


def latih_model():

    conn = koneksi()

    df = pd.read_sql(
        "SELECT * FROM data_latih",
        conn
    )

    conn.close()

    if "id" in df.columns:
        df = df.drop(columns=["id"])

    encoder = {}

    for kolom in [
        "warna",
        "akar",
        "kelembaban",
        "kualitas"
    ]:

        le = LabelEncoder()

        df[kolom] = le.fit_transform(df[kolom])

        encoder[kolom] = le

    X = df[
        [
            "umur",
            "panjang",
            "warna",
            "akar",
            "kelembaban"
        ]
    ]

    y = df["kualitas"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = GaussianNB()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    akurasi = accuracy_score(
        y_test,
        y_pred
    )

    joblib.dump(
        model,
        "model_naive_bayes.pkl"
    )

    joblib.dump(
        encoder,
        "label_encoder.pkl"
    )

    return akurasi