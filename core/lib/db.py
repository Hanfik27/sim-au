from pymongo import MongoClient

client = None
db = None
absensi_col = None
dosen_col = None
fakultas_col = None
gedung_col = None
jadwal_col = None
jurusan_col = None
kelas_col = None
lab_col = None
mata_kuliah_col = None
mahasiswa_col = None
nilai_col = None
users_col = None

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["simum"]

    absensi_col =       db["absensi"]
    dosen_col =         db["dosen"]
    fakultas_col =      db["fakultas"]
    gedung_col =        db["gedung"]
    jadwal_col =        db["jadwal"]
    jurusan_col =       db["jurusan"]
    kelas_col =         db["kelas"]
    lab_col =           db["lab"]
    mata_kuliah_col =   db["mata_kuliah"]
    mahasiswa_col =     db["mahasiswa"]
    nilai_col =         db["nilai"]
    users_col =         db["users"]

    print("Koneksi ke MongoDB berhasil.")
except Exception as e:
    print(f"Gagal terhubung ke MongoDB: {e}")
    exit()
