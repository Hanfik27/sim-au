from core.lib.db import dosen_col

class DosenModel:
    @staticmethod
    def generate_dosen_id():
        """Menghasilkan ID_DOSEN baru berdasarkan urutan terakhir di database."""
        last_dosen = dosen_col.find_one(sort=[("ID_DOSEN", -1)])  
        if last_dosen:
            last_id = int(last_dosen["ID_DOSEN"][1:])  
            new_id = f"D{last_id + 1:02d}" 
        else:
            new_id = "D01" 
        return new_id

    @staticmethod
    def get_all():
        return list(dosen_col.find({}))

    @staticmethod
    def get_by_id(ID_DOSEN):
        return dosen_col.find_one({"ID_DOSEN": ID_DOSEN})

    @staticmethod
    def insert(data):
        data["ID_DOSEN"] = DosenModel.generate_dosen_id()
        result = dosen_col.insert_one(data)
        return result.inserted_id if result.inserted_id else None
    @staticmethod
    def update(ID_DOSEN, data):
        return dosen_col.update_one({"ID_DOSEN": ID_DOSEN}, {"$set": data})

    @staticmethod
    def delete(ID_DOSEN):
        return dosen_col.delete_one({"ID_DOSEN": ID_DOSEN})
