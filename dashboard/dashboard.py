import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    hour_df = pd.read_csv("hour_data.csv")
    day_df = pd.read_csv("day_data.csv")
    return hour_df, day_df

hour_df, day_df = load_data()

# Mapping musim
season_mapping = {
    1: "Musim Semi",
    2: "Musim Panas",
    3: "Musim Gugur",
    4: "Musim Dingin"
}

day_df["season_label"] = day_df["season"].map(season_mapping)

# Sidebar filters
st.sidebar.header("Filter Data")

# Filter berdasarkan tanggal
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
start_date = st.sidebar.date_input("Pilih tanggal mulai:", day_df['dteday'].min())
end_date = st.sidebar.date_input("Pilih tanggal akhir:", day_df['dteday'].max())

day_filtered = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & (day_df['dteday'] <= pd.to_datetime(end_date))]

# Filter berdasarkan musim (season)
selected_season_labels = st.sidebar.multiselect(
    "Pilih Musim:",
    options=day_df["season_label"].unique(),
    default=day_df["season_label"].unique()
)

day_filtered = day_filtered[day_filtered["season_label"].isin(selected_season_labels)]

# Title
st.title("Dashboard Penyewaan Sepeda")

# Visualisasi 1: Rata-rata penyewaan berdasarkan jam
hourly_stats = hour_df.groupby('hr').agg({
    'cnt': 'mean'
}).reset_index()

st.subheader("Rata-rata Penyewaan Sepeda berdasarkan Jam")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(hourly_stats['hr'], hourly_stats['cnt'], marker='o', color='b')
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_title("Penyewaan Sepeda per Jam")
ax.grid()
st.pyplot(fig)

# Visualisasi 2: Rata-rata penyewaan berdasarkan musim
season_stats = day_filtered.groupby('season_label').agg({
    'cnt': 'mean'
}).reset_index()

st.subheader("Rata-rata Penyewaan Sepeda berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='season_label', y='cnt', data=season_stats, ax=ax, palette='viridis')
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_title("Pengaruh Musim terhadap Penyewaan Sepeda")
st.pyplot(fig)

# Visualisasi 3: Heatmap pola penyewaan berdasarkan jam dan hari
hour_weekday_data = hour_df.groupby(['hr', 'weekday'])['cnt'].mean().reset_index()
hour_weekday_pivot = hour_weekday_data.pivot(index='hr', columns='weekday', values='cnt')

st.subheader("Heatmap Penyewaan Sepeda berdasarkan Jam dan Hari")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(hour_weekday_pivot, cmap='viridis', annot=False, linewidths=0.5, ax=ax)
ax.set_xlabel("Hari (0=Minggu, 6=Sabtu)")
ax.set_ylabel("Jam")
ax.set_title("Pola Penyewaan Sepeda")
st.pyplot(fig)
