import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
	page_title=" 🔥 regressi tka",
	page_icon="🔥 "
)

model = joblib.load('model.joblib')

st.title("🔥 Prediksi Nilai TKA")
st.write("Aplikasi machine learning")

jam_belajar_per_hari=st.slider("Jam belajar per hari",7,5,14)


persen_kehadiran = st.slider(
    "Persentase kehadiran (%)", 90,85,100)
bimbel=st.pills("bimbel",["ya","tidak"],default="ya")
if st.button("Prediksi Nilai TKA"):
    data_baru = pd.DataFrame(
        [[jam_belajar_per_hari, persen_kehadiran, bimbel]],
        columns=['jam_belajar_per_hari', 'persen_kehadiran', 'bimbel']
    )

    prediksi = model.predict(data_baru)[0]
	prediksi = prediksi.clip(0,100)

    st.success(f"📊 Prediksi Nilai TKA: **{prediksi[0]:.0f}**")
    st.balloons()  # 🎈 tambahan di sini

st.divider()

