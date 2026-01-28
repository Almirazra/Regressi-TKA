import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
	page_title = "Prediksi Nilai TKA",
	page_icon="📘"
)

model = joblib.load("model.joblib")

st.title("📘 Prediksi Nilai TKA")
st.markdown("Aplikasi machine learning *regression* untuk memprediksi Nilai TKA")

jam = st.slider("Jam Belajar Per Hari", 0, 24, 5)
presentase = st.slider("Presentase Kehadiran", 0, 100, 90)
bimbel = st.pills("Ikut Bimbel", ["ya","tidak"], default="ya")

if st.button("Prediksi", type="primary"):
    data_baru = pd.DataFrame([[jam, presentase, bimbel]], columns=["jam_belajar_per_hari","persen_kehadiran", "bimbel"])
    prediksi = model.predict(data_baru)[0]
    prediksi = prediksi.clip(0,100)
    st.success(f"Model memprediksi nilai TKA : **{prediksi:.0f}**")
    st.balloons()

st.divider()
st.caption("Dibuat dengan :fire: oleh Almira Zahra")
