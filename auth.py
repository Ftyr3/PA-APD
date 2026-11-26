from data import akun

pengguna_aktif = ""
level_aktif = ""


def login():
    global pengguna_aktif, level_aktif
    percobaan = 0
    while percobaan < 3:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        try:
            if akun[username]["password"] != password:
                raise ValueError
        except (KeyError, ValueError):
            percobaan += 1
            print("Username atau password salah!")
        else:
            pengguna_aktif = username
            level_aktif = akun[username]["level"]
            print("Login berhasil!")
            return
    print("Login gagal 3 kali. Kembali ke menu awal.")


def register():
    percobaan = 0
    while percobaan < 3:
        username = input("Username baru: ").strip()
        if username == "":
            print("Username tidak boleh kosong!")
            percobaan += 1
            continue
        if username in akun:
            print("Username sudah terdaftar!")
            percobaan += 1
            continue
        password = input("Password baru: ").strip()
        if password == "":
            print("Password tidak boleh kosong!")
            percobaan += 1
            continue
        ulangi = input("Ulangi password: ").strip()
        if password != ulangi:
            print("Password tidak sama, silakan ulangi.")
            percobaan += 1
            continue
        akun[username] = {"password": password, "level": "user"}
        print("Registrasi berhasil! Silakan login.")
        return
    print("Registrasi gagal 3 kali. Kembali ke menu awal.")


def logout():
    global pengguna_aktif, level_aktif
    pengguna_aktif = ""
    level_aktif = ""
    print("Anda telah logout.")