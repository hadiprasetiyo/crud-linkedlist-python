# CRUD LinkedList (Mahasiswa) - Python & MySQL

Proyek ini adalah implementasi program manajemen data mahasiswa (CRUD) menggunakan kombinasi **Linked List** di Python dan penyimpanan database **MySQL**. Proyek ini dibuat untuk tugas praktikum Algoritma dan Struktur Data (ASD).

## Fitur Utama

- **Role-Based Access Control (RBAC):**
  - **Admin:** Memiliki hak penuh untuk melakukan Insert, Update, Delete, Search, Print database, serta sinkronisasi Linked List (Update, Search, Print, Reset).
  - **User:** Memiliki akses terbatas hanya untuk mencari data, mencetak data, serta melihat & memperbarui Linked List.
- **Sinkronisasi Linked List & Database:** Data mahasiswa disimpan secara permanen di MySQL dan dipetakan ke dalam struktur data Linked List secara dinamis di memori (RAM).
- **Auto Database & Table Migration:** Sistem mendeteksi dan membuat database `python_db` serta tabel `mahasiswa` secara otomatis jika belum tersedia.
- **Tampilan Tabel Rapi:** Menggunakan `PrettyTable` untuk menampilkan data secara terstruktur di terminal/console.

---

## Struktur Direktori

```text
├── controllers/
│   ├── controllerMahasiswa.py  # Logika bisnis CRUD & operasi Linked List
│   └── queueMahasiswa.py       # Logika antrean (jika digunakan)
├── database/
│   └── database.py             # Koneksi MySQL & Auto Migration
├── models/
│   └── mahasiswa.py            # Node Linked List (Representasi Mahasiswa)
├── .gitignore                  # File pengabaian Git (env, cache)
├── main.py                     # Entry point program (Menu CLI)
└── README.md                   # Dokumentasi proyek
```

---

## Prasyarat & Instalasi

### 1. Prasyarat
Pastikan Anda memiliki software berikut terinstal di perangkat Anda:
- **Python 3.x**
- **MySQL Server** (XAMPP / Laragon / MySQL Workbench)

### 2. Instalasi Dependensi
Instal pustaka Python yang diperlukan dengan menjalankan perintah berikut:
```bash
pip install mysql-connector-python prettytable
```

### 3. Konfigurasi Database
Secara default, koneksi database menggunakan konfigurasi berikut pada [database.py](file:///database/database.py):
- **Host:** `localhost`
- **User:** `root`
- **Password:** `""` (Kosong)
- **Database:** `python_db` (Akan terbuat secara otomatis)

*Pastikan MySQL server Anda sudah aktif sebelum menjalankan aplikasi.*

---

## Cara Menjalankan

Jalankan program utama melalui terminal dengan perintah:
```bash
python main.py
```

Setelah berjalan, Anda akan diminta memasukkan **Username** dan **Password**. Pastikan data akun yang sesuai telah dikonfigurasi di tabel `account` pada database Anda untuk login sebagai Admin atau User.
