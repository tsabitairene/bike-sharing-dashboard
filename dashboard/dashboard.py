import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_df = pd.read_csv('dashboard/main_data.csv')

# Pastikan kolom 'dteday' ada dan dalam format datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Ekstrak bulan dari kolom 'dteday'
day_df['month'] = day_df['dteday'].dt.month

# Judul Dashboard
st.title('📊 Bike Sharing Dashboard')

# Sidebar untuk Filter Data
st.sidebar.header('📌 Filter Data')

weather_dict = {1: "Cerah / Langit sedikit berawan", 
                2: "Berawan / Kabut", 
                3: "Hujan ringan / Salju ringan", 
                4: "Hujan deras / Salju lebat / Badai"}

day_df['weather_desc'] = day_df['weathersit'].map(weather_dict)

selected_weather = st.sidebar.multiselect('Pilih Kondisi Cuaca:', day_df['weather_desc'].unique())

if selected_weather:
    filtered_data = day_df[day_df['weather_desc'].isin(selected_weather)]
else:
    filtered_data = day_df

# Filter data berdasarkan bulan yang dipilih
selected_month = st.sidebar.selectbox('Pilih Bulan:', day_df['month'].unique())

# Filter data berdasarkan bulan yang dipilih
filtered_data_by_month = filtered_data[filtered_data['month'] == selected_month]

# Visualisasi Distribusi Penyewaan Sepeda berdasarkan Cuaca
st.subheader('📅 Distribusi Penyewaan Sepeda Harian')
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(filtered_data['cnt'], bins=30, kde=False, ax=ax, color="blue")
plt.xlabel('Jumlah Penyewaan')
plt.ylabel('Frekuensi')
plt.title('Distribusi Penyewaan Sepeda')
st.pyplot(fig)

# Visualisasi Penyewaan Sepeda berdasarkan Bulan yang Dipilih
st.subheader(f'📅 Distribusi Penyewaan Sepeda untuk Bulan {selected_month}')
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(filtered_data_by_month['cnt'], bins=30, kde=False, ax=ax, color="green")
plt.xlabel('Jumlah Penyewaan')
plt.ylabel('Frekuensi')
plt.title(f'Distribusi Penyewaan Sepeda Bulan {selected_month}')
st.pyplot(fig)

# Sidebar Insight
st.sidebar.markdown('## 🔎 Insight')
st.sidebar.markdown('- **Jumlah penyewaan cenderung lebih tinggi saat cuaca cerah.**')
st.sidebar.markdown('- **Hujan deras atau badai dapat mengurangi jumlah penyewaan.**')

# Tampilkan data setelah difilter
st.subheader('📋 Data Penyewaan Sepeda (Setelah Filter)')
st.dataframe(filtered_data)
