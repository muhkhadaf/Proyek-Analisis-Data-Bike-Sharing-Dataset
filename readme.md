# Bike Sharing Data Analysis Dashboard

## 📌 Project Overview
Dashboard ini dikembangkan menggunakan **Streamlit** untuk menganalisis dan memvisualisasikan data penyewaan sepeda berdasarkan berbagai faktor seperti kondisi cuaca, waktu, dan hari dalam seminggu.

---

## 🛠️ Installation Guide
### 1️⃣ Clone Repository
Jika proyek ini berada dalam repository GitHub, clone menggunakan perintah berikut:
```bash
git clone https://github.com/muhkhadaf/Proyek-Analisis-Data-Bike-Sharing-Dataset.git
cd Proyek-Analisis-Data-Khadafi
```
Jika proyek sudah berada dalam folder lokal, langsung lanjut ke langkah berikutnya.

### 2️⃣ Buat Virtual Environment *(Opsional, tetapi Disarankan)*
```bash
python -m venv venv  # Buat virtual environment
source venv/bin/activate  # Aktifkan di Mac/Linux
venv\Scripts\activate  # Aktifkan di Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

Jika `requirements.txt` belum ada, bisa dibuat dengan:
```bash
pipreqs . --force
```

---

## 🚀 How to Run the Dashboard
### 1️⃣ Jalankan Streamlit
```bash
streamlit run app.py
```
Jika terjadi error **'streamlit' is not recognized**, pastikan Streamlit sudah terinstall:
```bash
pip install streamlit
```

### 2️⃣ Akses Dashboard
Setelah dijalankan, akan muncul URL seperti:
```bash
Local URL: http://localhost:8501
Network URL: http://192.168.xx.xx:8501
```
Buka browser dan akses **http://localhost:8501** untuk melihat dashboard.

---

## 🎨 Dashboard Features
✅ **Visualisasi Data:** Menampilkan analisis penyewaan sepeda berdasarkan faktor cuaca, waktu, dan hari.
✅ **Interaktif:** Memungkinkan pengguna memilih parameter tertentu untuk eksplorasi data lebih lanjut.
✅ **Insights & Kesimpulan:** Menyajikan temuan utama dari analisis data.

---

## 📝 Author
Project ini dikembangkan oleh **Muhammad Khadafi Riyadi**. Jika ada pertanyaan, silakan hubungi melalui [email kamu] atau melalui repository ini.

---

## 📜 License
Proyek ini menggunakan lisensi **MIT License**. Kamu bebas menggunakan dan mengembangkan proyek ini dengan memberikan atribusi yang sesuai.

---


