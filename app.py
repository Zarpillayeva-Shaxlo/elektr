import streamlit as st
import pickle
import os

# === Faylning mavjudligini tekshirish ===
model_path = "electr.pkl"
if not os.path.exists(model_path):
    st.error("Model fayli (electric.pkl) topilmadi. Iltimos, faylni loyiha papkasiga joylashtiring.")
    st.stop()

# === Modelni yuklash ===
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# === Streamlit ilovaning interfeysi ===
st.title("Elektr energiyasi iste'molini bashorat qilish")

st.markdown("Foydalanuvchi kiritishi kerak bo'lgan ma'lumotlar:")

# Foydalanuvchi kiritadigan ma'lumotlar
temperature = st.number_input("Harorat (Celsius):", min_value=-30.0, max_value=50.0, value=20.0, step=0.1)
time = st.number_input("Vaqt (soat):", min_value=0.0, max_value=24.0, value=12.0, step=0.1)
family_size = st.number_input("Oila a'zolari soni:", min_value=1, max_value=20, value=4, step=1)
appliances = st.number_input("Jihozlar soni (ishlayotgan):", min_value=0, max_value=100, value=5, step=1)

# Bashorat tugmasi
if st.button("Bashorat qilish"):
    try:
        # Kiritilgan ma'lumotlarni listga joylash
        user_input = [[temperature, time, family_size, appliances]]
        
        # Model orqali bashorat qilish
        prediction = model.predict(user_input)
        
        # Bashoratni ko'rsatish
        st.success(f"Bashorat qilingan elektr iste'moli: {prediction[0]:.2f} kWh")
    except Exception as e:
        st.error(f"Xatolik yuz berdi: {e}")

# Qo'shimcha ma'lumotlar yoki ko'rsatmalar
st.markdown("**Eslatma:** 'electric.pkl' fayli loyihaning ildiz papkasida bo'lishi kerak.")

# === Local muhitni sozlash bo'yicha ko'rsatmalar ===
# 1. virtual environment (venv) yaratish:  
#    ```bash
#    python -m venv venv
#    ```















