import streamlit as st
import pickle

# Function untuk menghitung BMI dan kategorinya
def hitung_bmi(Weight, Height):
    Height_m = Height / 100  # Konversi tinggi ke meter
    bmi = Weight / (Height_m ** 2)
    if bmi < 18.5:
        kategori = "Underweight"
    elif 18.5 <= bmi < 24.9:
        kategori = "Normal weight"
    elif 25 <= bmi < 29.9:
        kategori = "Overweight"
    else:
        kategori = "Obese"
    return bmi, kategori

# Memuat model dengan pickle
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# UI Streamlit
st.title("Aplikasi Penghitung BMI dengan Model Machine Learning")

# Input dari user
Weight = st.number_input("Masukkan berat badan Anda (kg):", min_value=1, max_value=200, value=70)
Height = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=50, max_value=250, value=170)

# Tombol untuk menghitung BMI
if st.button("Hitung BMI"):
    bmi, kategori = hitung_bmi(Weight, Height)
    st.write(f"**BMI Anda adalah: {bmi:.2f}**")
    st.write(f"**Kategori: {kategori}**")

    # Prediksi dengan model (jika model menggunakan input seperti berat dan tinggi)
    # Pastikan input sesuai dengan yang digunakan oleh model saat training
    prediction = model.predict([[Weight, Height]])
    st.write(f"**Prediksi dari model: {prediction}**")
