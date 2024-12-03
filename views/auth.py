from .base import BaseView
class AuthView:

    @staticmethod
    def show_registration_message(success, role=None, user_id=None):
        if success:
            print(f"Registrasi berhasil! Anda terdaftar sebagai {role.capitalize()} dengan ID_USERS: {user_id}.")
        else:
            print("Registrasi gagal. Email sudah terdaftar.")
            

    @staticmethod
    def show_login_message(success, role=None):
        if success:
            print(f"Login berhasil! Anda masuk sebagai {role.capitalize()}.")
        else:
            print("Login gagal. Email atau password salah.")

    @staticmethod
    def input_registration_data():
        print("\n=== Registrasi ===")
        email = input("Masukkan Email: ").strip()
        password = input("Masukkan Password: ").strip()
        return email, password

    @staticmethod
    def input_login_data():
        print("\n=== Login ===")
        email = input("Masukkan Email: ").strip()
        password = input("Masukkan Password: ").strip()
        return email, password

    @staticmethod
    def show_invalid_email_message():
        print("Email tidak valid. Hanya mahasiswa dan dosen terdaftar yang dapat mendaftar.")

