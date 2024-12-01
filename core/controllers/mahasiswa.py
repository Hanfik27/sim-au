from models.mahasiswa import MahasiswaModel

class MahasiswaController:
    @staticmethod
    def list_mahasiswa():
        return MahasiswaModel.get_all()

    @staticmethod
    def find_mahasiswa(ID_MAHASISWA):
        return MahasiswaModel.get_by_nim(ID_MAHASISWA)

    @staticmethod
    def add_mahasiswa(ID_MAHASISWA, NIM, NAMA, EMAIL, NAMA_JURUSAN, NAMA_FAKULTAS):
        data = {"ID_MAHASISWA": ID_MAHASISWA,"NIM": NIM, "NAMA": NAMA, "EMAIL": EMAIL, "NAMA_JURUSAN": NAMA_JURUSAN, "NAMA_FAKULTAS": NAMA_FAKULTAS}
        MahasiswaModel.insert(data)
        print(f"Mahasiswa {NAMA} berhasil ditambahkan.")

    @staticmethod
    def update_mahasiswa(ID_MAHASISWA, NIM=None, NAMA=None, EMAIL=None, NAMA_JURUSAN=None, NAMA_FAKULTAS=None):
        data = {}
        if NIM:
            data["NIM"] = NIM
        if NAMA:
            data["NAMA"] = NAMA
        if EMAIL:
            data["EMAIL"] = EMAIL
        if NAMA_JURUSAN:
            data["NAMA_JURUSAN"] = NAMA_JURUSAN
        if NAMA_FAKULTAS:
            data["NAMA_FAKULTAS"] = NAMA_FAKULTAS
        if data: 
            MahasiswaModel.update(ID_MAHASISWA, data)
            print(f"Mahasiswa dengan ID {ID_MAHASISWA} berhasil diperbarui.")
        else:
            print("Tidak ada data yang diubah.")

    @staticmethod
    def delete_mahasiswa(ID_MAHASISWA):
        MahasiswaModel.delete(ID_MAHASISWA)
        print(f"Mahasiswa dengan ID {ID_MAHASISWA} berhasil dihapus.")

