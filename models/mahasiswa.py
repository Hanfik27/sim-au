from core.lib.db import mahasiswa_col

class MahasiswaModel:
    @staticmethod
    def generate_mahasiswa_id():
        """Menghasilkan ID_MAHASISWA baru berdasarkan urutan terakhir di database."""
        last_mahasiswa = mahasiswa_col.find_one(sort=[("ID_MAHASISWA", -1)])  
        if last_mahasiswa:
            last_id = int(last_mahasiswa["ID_MAHASISWA"][1:])  
            new_id = f"M{last_id + 1:02d}" 
        else:
            new_id = "M01" 
        return new_id

    @staticmethod
    def get_all():
        return list(mahasiswa_col.find({}))

    @staticmethod
    def get_by_id(ID_MAHASISWA):
        return mahasiswa_col.find_one({"ID_MAHASISWA": ID_MAHASISWA})

    @staticmethod
    def insert(data):
        data["ID_MAHASISWA"] = MahasiswaModel.generate_mahasiswa_id()
        result = mahasiswa_col.insert_one(data)
        return result.inserted_id if result.inserted_id else None
    @staticmethod
    def update(ID_MAHASISWA, data):
        return mahasiswa_col.update_one({"ID_MAHASISWA": ID_MAHASISWA}, {"$set": data})

    @staticmethod
    def delete(ID_MAHASISWA):
        return mahasiswa_col.delete_one({"ID_MAHASISWA": ID_MAHASISWA})
