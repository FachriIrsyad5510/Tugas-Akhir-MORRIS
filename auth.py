# auth.py
from utils import input_teks_tidak_kosong

database_user = {
    "admin": "admin123"
}

def menu_autentikasi():
  """Menampilkan menu awal sebelum masuk ke aplikasi utama."""
  while True:
    print("\n" + "=" * 48)
    print("       SELAMAT DATANG DI APLIKASI DOKNOVA")
    print("=" * 48)
    print("1. Login")
    print("2. Register / Buat Akun Baru")
    print("3. Keluar Aplikasi")
    
    pilihan = input("Pilih menu (1-3): ").strip()
    
    if pilihan == "1":
      username = login_user()
      if username:
        return username
    elif pilihan == "2":
      register_user()
    elif pilihan == "3":
      print("\nTerima kasih telah menggunakan DOKNOVA.")
      exit()
    else:
      print("Error: Pilihan tidak valid. Masukkan angka 1, 2, atau 3.")

def register_user():
  print("\n--- REGISTRASI AKUN BARU ---")
  username = input_teks_tidak_kosong("Masukkan username baru: ").lower()
  
  if username in database_user:
    print("Error: Username sudah terdaftar! Silakan gunakan username lain.")
    return
  
  password = input_teks_tidak_kosong("Masukkan password: ")
  database_user[username] = password
  print(f"\n[Sukses] Akun dengan username '{username}' berhasil dibuat! Silakan login.")

def login_user():
  print("\n--- LOGIN AKUN ---")
  username = input_teks_tidak_kosong("Username: ").lower()
  password = input_teks_tidak_kosong("Password: ")
  
  if username in database_user and database_user[username] == password:
    print(f"\n[Sukses] Berhasil login. Selamat datang, {username}!")
    return username
  else:
    print("\n[Error] Username atau password salah!")
    return None