# Tugas-Akhir-MORRIS
# DOKNOVA: Aplikasi Kesehatan & Kalkulator TDEE

Aplikasi berbasis terminal (CLI) yang ditulis dengan Python untuk menghitung indikator kesehatan dasar: IMT, BMR, TDEE, dan kebutuhan air harian, dilengkapi dengan sistem autentikasi pengguna (Login & Register).

---

## 1. Identitas Kelompok

| Keterangan | Isi |
|---|---|
| **Nama Aplikasi** | DOKNOVA |
| **Nama Kelompok** | _DONGKER_ |

### Daftar Anggota & Pembagian Peran

| No | Nama | NPM | Peran |
|---|---|---|---|
| 1 | _Muhammad Fadhil Hisyam_ | _714260030_ | _(Programmer dan perancang flowchart)_ |
| 2 | _Fachri Irsyad Suherman_ | _714260015_ | _(Programmer dan perancang flowchart)_ |
| 3 | _Marshella Ofiana_ | _714260018_ | _Pembuat Poster_ |
| 4 | _Dimaj Zakan Hawada_ | _714260006_ | _Dokumentasi README_ |
| 5 | _Visabililiany Avrilend Sangadji_ | _613260010_ | _Koordinator Video_ |
| 6 | _Ibnu Dzakwan Rabbani_ | _613260003_ | _Penguji/QA_ |

---

## 2. Deskripsi Aplikasi

DOKNOVA adalah program kalkulator kesehatan yang dijalankan lewat terminal. Pengguna harus melakukan autentikasi (login atau mendaftar akun baru) terlebih dahulu sebelum masuk ke menu utama. Setelah masuk, pengguna cukup memasukkan data diri seperti jenis kelamin, berat badan, tinggi badan, dan usia, lalu program menghitung hasilnya secara otomatis.

### Masalah yang Diselesaikan

- Banyak orang tidak tahu apakah berat badannya sudah ideal atau belum.
- Menghitung kebutuhan kalori dan air harian secara manual memerlukan rumus yang rumit dan rawan salah hitung.
- Informasi kesehatan dasar biasanya tersebar di banyak situs atau aplikasi yang berbeda.

DOKNOVA menggabungkan empat perhitungan tersebut dalam satu aplikasi sederhana, lengkap dengan validasi input agar data yang dimasukkan tetap masuk akal, sistem manajemen akun sederhana, serta riwayat perhitungan selama satu sesi.

> **Catatan:** Hasil perhitungan hanya perkiraan umum dan bukan pengganti saran dokter atau ahli gizi.

---

## 3. Daftar Fitur & Cara Penggunaan

### Menu Autentikasi (Awal)

Saat program pertama kali dijalankan, pengguna akan diarahkan ke menu autentikasi. Ketik angka menu (1-3) lalu tekan **Enter**:

| Menu | Fitur | Keterangan |
|---|---|---|
| 1 | Login | Masuk menggunakan akun yang sudah terdaftar (akun bawaan: `admin` / `admin123`) |
| 2 | Register / Buat Akun Baru | Mendaftarkan username dan password baru ke dalam sesi memori |
| 3 | Keluar Aplikasi | Menutup program |

### Menu Utama

Setelah berhasil login, menu utama akan tampil beserta informasi **User Aktif** pada bagian banner. Ketik angka menu (1-7) lalu tekan **Enter**:

| Menu | Fitur | Keterangan |
|---|---|---|
| 1 | Hitung IMT / BMI | Menghitung Indeks Massa Tubuh dan menampilkan kategorinya |
| 2 | Hitung BMR | Menghitung kalori dasar yang dibakar tubuh saat istirahat (rumus Mifflin-St Jeor) |
| 3 | Hitung TDEE | Menghitung kebutuhan kalori harian berdasarkan tingkat aktivitas |
| 4 | Asupan Air Harian | Merekomendasikan jumlah air minum per hari |
| 5 | Riwayat Perhitungan | Menampilkan semua hasil perhitungan pada sesi saat ini |
| 6 | Logout / Ganti Akun | Keluar dari akun aktif dan kembali ke menu autentikasi |
| 7 | Keluar Aplikasi | Menutup program |

### Cara Menggunakan Tiap Fitur

**Autentikasi (Login & Register)**
- **Register:** Pilih menu `2`, masukkan username baru (otomatis diubah ke huruf kecil dan tidak boleh duplikat) serta password.
- **Login:** Pilih menu `1`, masukkan username dan password yang sesuai. Untuk pengujian cepat, tersedia akun default dengan username `admin` dan password `admin123`. Data akun baru disimpan di memori selama sesi program berjalan.

**Menu 1: IMT**
1. Masukkan berat badan (kg) dan tinggi badan (cm).
2. Program menampilkan nilai IMT dan kategorinya:
   - Kurang dari 18,5: Kurus (Underweight)
   - 18,5 sampai kurang dari 25: Normal (Ideal)
   - 25 sampai kurang dari 30: Kelebihan Berat Badan (Overweight)
   - 30 ke atas: Obesitas

**Menu 2: BMR**
1. Masukkan jenis kelamin (`L` / `P`), berat badan, tinggi badan, dan usia.
2. Program menampilkan BMR dalam kkal/hari.

**Menu 3: TDEE**
1. Masukkan data diri seperti pada menu BMR.
2. Pilih tingkat aktivitas harian:
   - 1 = Sedentary (jarang / tidak olahraga)
   - 2 = Ringan (olahraga 1-3 hari/minggu)
   - 3 = Sedang (olahraga 3-5 hari/minggu)
   - 4 = Berat (olahraga 6-7 hari/minggu)
   - 5 = Ekstra berat (pekerja fisik / atlet)
3. Program menampilkan TDEE beserta target kalori untuk menjaga, menurunkan (-500 kkal), dan menaikkan (+500 kkal) berat badan.

**Menu 4: Asupan Air Harian**
1. Masukkan berat badan (kg) dan durasi olahraga hari ini (menit).
2. Program menampilkan rekomendasi air minum dalam liter dan mililiter.
   Rumus: 35 ml x berat badan, ditambah 350 ml untuk setiap 30 menit olahraga.

**Menu 5: Riwayat**
- Menampilkan daftar hasil perhitungan yang sudah dilakukan sejak program dibuka. Riwayat disimpan di memori, sehingga **hilang saat program ditutup**.

**Menu 6: Logout / Ganti Akun**
- Mengakhiri sesi akun saat ini dan mengembalikan pengguna ke menu autentikasi untuk login menggunakan akun lain atau membuat akun baru.

### Validasi Input

- Username dan password tidak boleh kosong (username otomatis dikonversi ke huruf kecil).
- Berat badan: 1-500 kg
- Tinggi badan: 30-300 cm
- Usia: 1-120 tahun
- Durasi olahraga: 0-1440 menit
- Jenis kelamin hanya `L` atau `P`
- Input kosong atau bukan angka akan ditolak dan pengguna diminta mengulang.

---

## 4. Penjelasan Alur Logika & Fungsi Tiap File

### Struktur Folder