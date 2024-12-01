from pymongo import MongoClient

# Koneksi ke database
client = MongoClient("mongodb://localhost:27017/")
db = client["simum"]
collection = db["mahasiswa"]

class MahasiswaModel:
    @staticmethod
    def get_all():
        return list(collection.find({}))

    @staticmethod
    def get_by_nim(nim):
        return collection.find_one({"nim": nim})

    @staticmethod
    def insert(mahasiswa):
        return collection.insert_one(mahasiswa)

    @staticmethod
    def update(nim, data):
        return collection.update_one({"nim": nim}, {"$set": data})

    @staticmethod
    def delete(nim):
        return collection.delete_one({"nim": nim})
