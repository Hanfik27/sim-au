from core.lib.db import mata_kuliah_col

class MatkulModel:
    @staticmethod
    def generate_matkul_id():
        """Menghasilkan ID_MATKUL baru berdasarkan urutan terakhir di database."""
        last_matkul = mata_kuliah_col.find_one(sort=[("ID_MATKUL", -1)])  
        if last_matkul:
            last_id = int(last_matkul["ID_MATKUL"][2:])  
            new_id = f"MK{last_id + 1:02d}" 
        else:
            new_id = "MK01" 
        return new_id

    @staticmethod
    def get_all():
        return list(mata_kuliah_col.find({}))

    @staticmethod
    def get_by_id(ID_MATKUL):
        return mata_kuliah_col.find_one({"ID_MATKUL": ID_MATKUL})

    @staticmethod
    def insert(data):
        data["ID_MATKUL"] = MatkulModel.generate_matkul_id()
        result = mata_kuliah_col.insert_one(data)
        return result.inserted_id if result.inserted_id else None
    @staticmethod
    def update(ID_MATKUL, data):
        return mata_kuliah_col.update_one({"ID_MATKUL": ID_MATKUL}, {"$set": data})

    @staticmethod
    def delete(ID_MATKUL):
        return mata_kuliah_col.delete_one({"ID_MATKUL": ID_MATKUL})
