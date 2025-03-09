import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("dashboard/day_data.csv")
hour_df = pd.read_csv("dashboard/hour_data.csv")

# Sidebar
st.sidebar.header("Dashboard Penyewaan Sepeda")
st.sidebar.write("Eksplorasi Data Penyewaan Sepeda Berdasarkan Cuaca dan Waktu")

# Visualisasi 1: Pengaruh Cuaca terhadap Penyewaan Sepeda
st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x=day_df["weathersit"], y=day_df["cnt"], ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Fitur Interaktif: Dropdown untuk memilih jenis pengguna
user_type = st.selectbox("Pilih Jenis Pengguna:", ["Total", "Casual", "Registered"])

# Visualisasi 2: Pola Penyewaan Sepeda Berdasarkan Waktu
st.subheader("Pola Penyewaan Sepeda Berdasarkan Jam dan Hari")
fig, ax = plt.subplots(figsize=(10, 5))

if user_type == "Total":
    sns.heatmap(hour_df.pivot_table(values='cnt', index='hr', columns='weekday', aggfunc='mean'), cmap='coolwarm', ax=ax)
elif user_type == "Casual":
    sns.heatmap(hour_df.pivot_table(values='casual', index='hr', columns='weekday', aggfunc='mean'), cmap='coolwarm', ax=ax)
elif user_type == "Registered":
    sns.heatmap(hour_df.pivot_table(values='registered', index='hr', columns='weekday', aggfunc='mean'), cmap='coolwarm', ax=ax)

ax.set_xlabel("Hari (0: Minggu, 6: Sabtu)")
ax.set_ylabel("Jam")
st.pyplot(fig)

# Menambahkan penjelasan tentang data
st.write("""
Dashboard ini berfungsi untuk mengeksplorasi data penyewaan sepeda berdasarkan dua faktor utama: kondisi cuaca dan waktu.

1. **Kondisi Cuaca**:
   - Visualisasi pertama menunjukkan pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda.
   - Data cuaca diambil dari kolom `weathersit`, yang mencakup kategori seperti cerah, mendung, atau hujan.
   - Sumbu x menunjukkan kondisi cuaca, sedangkan sumbu y menunjukkan jumlah penyewaan sepeda (`cnt`).

2. **Jenis Pengguna**:
   - Terdapat fitur interaktif untuk memilih jenis pengguna: "Total", "Casual", atau "Registered".

3. **Pola Penyewaan Berdasarkan Waktu**:
   - Visualisasi kedua menggunakan heatmap untuk menunjukkan pola penyewaan berdasarkan jam dan hari.
   - Data diambil dari dataset `hour_df`, yang mencakup informasi tentang jumlah penyewaan berdasarkan jam (`hr`) dan hari (`weekday`).

4. **Kesimpulan**:
   - Dashboard ini membantu memahami tren penyewaan sepeda berdasarkan cuaca dan waktu.
""")
