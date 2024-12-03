from models.matkul import MatkulModel

class MatkulController:

    @staticmethod
    def list_matkul():
        return MatkulModel.get_all()

    @staticmethod
    def find_matkul(ID_MATKUL):
        return MatkulModel.get_by_id(ID_MATKUL)

    @staticmethod
    def add_matkul(NAMA_MATKUL, SKS, SEMESTER):
        ID_MATKUL = MatkulModel.generate_matkul_id()
        data = {
            "ID_MATKUL": ID_MATKUL,
            "NAMA_MATKUL": NAMA_MATKUL,
            "SKS": SKS,
            "SEMESTER": SEMESTER,
        }
        MatkulModel.insert(data)
        print(f"matkul {NAMA_MATKUL} berhasil ditambahkan dengan ID {ID_MATKUL}.")

    @staticmethod
    def update_matkul(ID_MATKUL, NAMA_MATKUL=None, SKS=None, SEMESTER=None):
        data = {}
        if ID_MATKUL:
            data["ID_MATKUL"] = ID_MATKUL
        if NAMA_MATKUL:
            data["NAMA_MATKUL"] = NAMA_MATKUL
        if SKS:
            data["SKS"] = SKS
        if SEMESTER:
            data["SEMESTER"] = SEMESTER
        if data:
            MatkulModel.update(ID_MATKUL, data)
            print(f"matkul dengan ID {ID_MATKUL} berhasil diperbarui.")
        else:
            print("Tidak ada data yang diubah.")

    @staticmethod
    def delete_matkul(ID_MATKUL):
        """Hapus data matkul."""
        data = MatkulModel.get_by_id(ID_MATKUL) 
        if data: 
            MatkulModel.delete(ID_MATKUL) 
            print(f"matkul dengan ID {ID_MATKUL} berhasil dihapus.")
        else: 
            print(f"Tidak ada data yang ditemukan dengan ID {ID_MATKUL}.")

