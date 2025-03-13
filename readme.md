# Cara Menjalankan Dashboard Streamlit Secara Lokal

Dashboard ini digunakan untuk menganalisis data penyewaan sepeda dengan visualisasi interaktif menggunakan Streamlit.

## Prasyarat
Sebelum menjalankan dashboard, pastikan Anda sudah menginstal beberapa dependensi berikut:

1. Python (versi 3.7 atau lebih baru)
2. Paket-paket Python yang dibutuhkan:
   - `streamlit`
   - `pandas`
   - `matplotlib`
   - `seaborn`

## Langkah-langkah Menjalankan Dashboard

### 1. Clone atau Download Repository
Anda bisa mengunduhnya atau melakukan clone dengan perintah berikut:
```bash
git clone https://github.com/muhkhadaf/Proyek-Analisis-Data-Bike-Sharing-Dataset.git
cd Proyek-Analisis-Data-Bike-Sharing-Dataset
```

### 2. Buat dan Aktifkan Virtual Environment (Opsional tapi Disarankan)
```bash
python -m venv env
source env/bin/activate  # Untuk macOS/Linux
env\Scripts\activate     # Untuk Windows
```

### 3. Install Dependensi
```bash
pip install -r requirements.txt
```
Jika tidak ada file `requirements.txt`, Anda bisa menginstal paket secara manual:
```bash
pip install streamlit pandas matplotlib seaborn
```

### 4. Jalankan Dashboard
```bash
streamlit run dashboard.py
```

### 5. Akses Dashboard
Setelah menjalankan perintah di atas, dashboard akan terbuka di browser dengan alamat berikut:
```
http://localhost:8501
```

## Catatan Tambahan
- Pastikan file dataset (`hour_data.csv` dan `day_data.csv`) tersedia di direktori yang benar.
- Jika ada perubahan pada kode, Anda bisa menghentikan proses (Ctrl + C) dan menjalankan ulang perintah `streamlit run dashboard.py`.
- Untuk keluar dari virtual environment, jalankan:
  ```bash
  deactivate
  ```

Selamat menggunakan dashboard! 🎉

