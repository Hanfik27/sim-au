from core.lib.db import users_col

class UserModel:
    @staticmethod
    def generate_users_id():
        """Menghasilkan ID_USERS baru berdasarkan urutan terakhir di database."""
        last_users = users_col.find_one(sort=[("ID_USERS", -1)])  
        if last_users:
            last_id = int(last_users["ID_USERS"][1:])  
            new_id = f"D{last_id + 1:02d}" 
        else:
            new_id = "D01" 
        return new_id

    @staticmethod
    def get_all():
        return list(users_col.find({}))

    @staticmethod
    def get_by_id(ID_USERS):
        return users_col.find_one({"ID_USERS": ID_USERS})

    @staticmethod
    def insert(data):
        data["ID_USERS"] = UserModel.generate_users_id()
        result = users_col.insert_one(data)
        return result.inserted_id if result.inserted_id else None
    @staticmethod
    def update(ID_USERS, data):
        return users_col.update_one({"ID_USERS": ID_USERS}, {"$set": data})

    @staticmethod
    def delete(ID_USERS):
        return users_col.delete_one({"ID_USERS": ID_USERS})
