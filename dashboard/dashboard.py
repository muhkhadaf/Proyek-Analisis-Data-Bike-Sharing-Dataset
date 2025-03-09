import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("day_data.csv")
hour_df = pd.read_csv("hour_data.csv")

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

st.write("Dashboard ini membantu memahami tren penyewaan sepeda berdasarkan cuaca dan waktu!")
