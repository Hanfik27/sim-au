from models.dosen import DosenModel

class DosenController:

    @staticmethod
    def list_dosen():
        return DosenModel.get_all()

    @staticmethod
    def find_dosen(ID_DOSEN):
        return DosenModel.get_by_id(ID_DOSEN)

    @staticmethod
    def add_dosen(NIP, NAMA, EMAIL, DEPARTEMEN):
        ID_DOSEN = DosenModel.generate_dosen_id()
        data = {
            "ID_DOSEN": ID_DOSEN,
            "NAMA": NAMA,
            "NIP": NIP,
            "EMAIL": EMAIL,
            "DEPARTEMEN": DEPARTEMEN,
        }
        DosenModel.insert(data)
        print(f"dosen {NAMA} berhasil ditambahkan dengan ID {ID_DOSEN}.")

    @staticmethod
    def update_dosen(ID_DOSEN, NIP=None, NAMA=None, EMAIL=None, DEPARTEMEN=None):
        data = {}
        if NIP:
            data["NIP"] = NIP
        if NAMA:
            data["NAMA"] = NAMA
        if EMAIL:
            data["EMAIL"] = EMAIL
        if DEPARTEMEN:
            data["DEPARTEMEN"] = DEPARTEMEN
        if data:
            DosenModel.update(ID_DOSEN, data)
            print(f"dosen dengan ID {ID_DOSEN} berhasil diperbarui.")
        else:
            print("Tidak ada data yang diubah.")

    @staticmethod
    def delete_dosen(ID_DOSEN):
        data = DosenModel.get_by_id(ID_DOSEN)
        if data:
            DosenModel.delete(ID_DOSEN)
            print(f"dosen dengan ID {ID_DOSEN} berhasil dihapus.")
        else :
            print(f"Tidak ada data yang ditemukan dengan ID {ID_DOSEN}.")