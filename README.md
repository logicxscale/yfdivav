# 📈 Stock Dividends & Price Chart with Streamlit & yfinance

Aplikasi Streamlit sederhana untuk mengambil data dividen dan grafik harga saham menggunakan library [yfinance](https://github.com/ranaroussi/yfinance).

---
![Screenshot](https://github.com/logicxscale/yfdivav/blob/main/screenshot.png?raw=true)
---

## 🚀 Fitur

- Ambil data harga saham 1 tahun terakhir  
- Tampilkan grafik pergerakan harga saham  
- Tampilkan riwayat dan grafik dividen  
- Informasi dividen tertinggi beserta tanggalnya  

---

## 🛠️ Cara Setup dari Awal

### 1. Clone repository ini (jika ada) atau buat folder baru
```bash
git clone https://github.com/username/stock-dividends-app.git
cd stock-dividends-app
```

### 2. Buat Virtual Environment
```bash
python3 -m venv venv
```

### 3. Aktifkan Virtual Environment
- Windows 
```bash
.\venv\Scripts\activate
```
- Mac / Linux
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install streamlit yfinance matplotlib pandas
```

### 5. Jalankan aplikasi secara lokal
```bash
streamlit run app.py
```

## ☁️ Deploy ke Streamlit Cloud
1. Push kode kamu ke GitHub (repository harus public atau private dengan akses Streamlit Cloud)
2. Buka https://share.streamlit.io dan login dengan akun GitHub kamu.
3. Klik New app > Pilih repository > Pilih branch dan file app.py.
4. Klik Deploy, aplikasi kamu akan online dalam beberapa detik!

## 📂 Struktur File
```
├── app.py           # File utama aplikasi Streamlit
├── requirements.txt # List package (optional)
└── README.md        # Dokumentasi ini
```

## 📋 Catatan
- Pastikan koneksi internet aktif saat menggunakan aplikasi karena yfinance mengambil data online.
- Untuk saham Indonesia, gunakan ticker dengan akhiran .JK (contoh: BBCA.JK).
- Jika ingin menambah fitur, silakan fork dan pull request!

## ❤️ Terima Kasih!
Selamat mencoba dan semoga bermanfaat!
Jika ada pertanyaan atau saran, silakan buka issue di repository.

Made with ❤️ by [@bagusa4](https://github.com/bagusa4)