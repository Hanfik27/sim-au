from models.auth import AuthModel, users_col
from core.lib.hash import verify_password, bcrypt
from core.lib.db import db, mahasiswa_col, dosen_col
from views.auth import AuthView


class AuthController:
    @staticmethod
    def create_default_admin():
        """Membuat admin default jika belum ada."""
        if AuthModel.create_default_admin():
            print("Default admin berhasil dibuat. Login dengan:\nUsername: admin\nPassword: admin123")
        else:
            print("Default admin sudah ada.")

    @staticmethod
    def register():
        """Proses registrasi user."""
        email, password = AuthView.input_registration_data()

        # Cek apakah email valid (ada di mahasiswa atau dosen)
        mahasiswa = mahasiswa_col.find_one({"EMAIL": email})
        dosen = dosen_col.find_one({"EMAIL": email})

        if mahasiswa:
            role = "mahasiswa"
        elif dosen:
            role = "dosen"
        else:
            AuthView.show_invalid_email_message()
            return

        # Cek apakah email sudah terdaftar di users
        if AuthModel.find_by_email(email):
            AuthView.show_registration_message(False)
            return

        # Registrasi user baru
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        result = AuthModel.register_user(email, hashed_password, role)
        if result.inserted_id:
            new_user = users_col.find_one({"_id": result.inserted_id})
            AuthView.show_registration_message(True, role, new_user["ID_USERS"])
        else:
            AuthView.show_registration_message(False)

    @staticmethod
    def login():
        """Proses login user."""
        email, password = AuthView.input_login_data()

        # Cari user di database
        user = AuthModel.find_by_email(email)
        if user and AuthModel.verify_password(password, user["PASSWORD"]):
            AuthView.show_login_message(True, user["ROLE"])
            return user["ROLE"]
        else:
            AuthView.show_login_message(False)
            return None
