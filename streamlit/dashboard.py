import streamlit as st
import requests

API_URL = "https://fastapi-ml-api.onrender.com/predict"  # Remplace par l’URL exacte de ton API

st.title("🌸 Prédiction d'espèce d'iris")

sepal_length = st.slider("Longueur des sépales", 4.0, 8.0, 5.1)
sepal_width = st.slider("Largeur des sépales", 2.0, 4.5, 3.5)
petal_length = st.slider("Longueur des pétales", 1.0, 7.0, 1.4)
petal_width = st.slider("Largeur des pétales", 0.1, 2.5, 0.2)

if st.button("Prédire"):
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }
    response = requests.post(API_URL, json=data)
    if response.status_code == 200:
        pred = response.json()["prediction"]
        st.success(f"🌼 Prédiction : Classe {pred}")
    else:
        st.error("❌ Erreur lors de la prédiction")
