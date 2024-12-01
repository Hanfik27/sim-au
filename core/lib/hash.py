import bcrypt

def hash_password(password):
    """Hash password menggunakan bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password, hashed):
    """Verifikasi password yang diinput dengan hash di database."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed)
