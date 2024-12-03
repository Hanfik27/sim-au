import bcrypt
from core.lib.db import users_col

class AuthModel:
    """Model untuk operasi pada koleksi 'users'."""

    @staticmethod
    def create_default_admin():
        """Membuat akun admin default jika belum ada."""
        default_admin = {
            "ID_USERS": "U01",
            "EMAIL": "admin",
            "PASSWORD": bcrypt.hashpw("admin123".encode('utf-8'), bcrypt.gensalt()),
            "ROLE": "admin"
        }
        if not users_col.find_one({"EMAIL": default_admin["EMAIL"], "ROLE": default_admin["ROLE"]}):
            users_col.insert_one(default_admin)
            return True  
        return False 
    
    @staticmethod
    def generate_user_id():
        """Menghasilkan ID_USERS baru berdasarkan urutan terakhir di database."""
        last_user = users_col.find_one(sort=[("ID_USERS", -1)])
        if last_user:
            last_id = int(last_user["ID_USERS"][1:])
            new_id = f"U{last_id + 1:02d}"
        else:
            new_id = "U01"
        return new_id

    @staticmethod
    def find_by_email(email):
        """Mencari user berdasarkan email."""
        return users_col.find_one({"EMAIL": email})

    @staticmethod
    def register_user(email, hashed_password, role):
        """Mendaftarkan user baru ke koleksi users."""
        user_id = AuthModel.generate_user_id()
        return users_col.insert_one({
            "ID_USERS": user_id,
            "EMAIL": email,
            "PASSWORD": hashed_password,
            "ROLE": role
        })

    @staticmethod
    def verify_password(plain_password, hashed_password):
        """Verifikasi password yang diinput dengan hash di database."""
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)
