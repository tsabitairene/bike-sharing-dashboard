# 📊 Proyek Analisis Data: Bike Sharing Dataset

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda berdasarkan faktor waktu dan cuaca. Dua pertanyaan bisnis utama yang dijawab dalam proyek ini adalah:
1. **Kapan waktu tersibuk untuk penyewaan sepeda?**
2. **Bagaimana pengaruh cuaca terhadap jumlah penyewaan sepeda?**

## 📂 Struktur Direktori
```
submission/
├── dashboard/
│   ├── main_data.csv        # Dataset untuk dashboard
│   ├── dashboard.py         # Kode utama untuk dashboard Streamlit
├── data/
│   ├── day.csv              # Dataset penyewaan sepeda harian
│   ├── hour.csv             # Dataset penyewaan sepeda per jam
├── notebook.ipynb           # Notebook eksplorasi dan analisis data
├── README.md                # Dokumentasi proyek
├── requirements.txt         # Daftar dependensi Python
├── url.txt                  # URL dashboard yang telah dideploy
```

## 🚀 Cara Menjalankan Dashboard
1. **Pastikan semua dependensi terinstal** dengan menjalankan:
   ```
   pip install -r requirements.txt
   ```
2. **Jalankan dashboard menggunakan Streamlit**:
   ```
   streamlit run dashboard/dashboard.py
   ```

## 🔍 Insight Utama
- **📅 Waktu Tersibuk untuk Penyewaan Sepeda**  
  - Jam sibuk terjadi pada **pukul 08:00 dan 17:00**, bertepatan dengan jam berangkat dan pulang kerja.
  
- **🌦️ Pengaruh Cuaca terhadap Penyewaan**  
  - Penyewaan sepeda **lebih tinggi saat cuaca cerah**.  
  - **Cuaca buruk seperti hujan atau salju** mengurangi jumlah penyewaan secara signifikan.

## 🌐 Deployment
Dashboard telah di-deploy dan dapat diakses melalui link berikut:  
🔗 **[Bike Sharing Dashboard](https://bike-sharing-dashboard-vj8dann7gfkjtcpeycw8ms.streamlit.app/)**  

## 📩 Kontak
- **👤 Nama:** Tsabita Irene Adielia  
- **📧 Email:** tsabitairene@gmail.com  
- **🏆 ID Dicoding:** tsabitairene  

