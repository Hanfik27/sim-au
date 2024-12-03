from models.user import UserModel

class UserController:

    @staticmethod
    def list_user():
        return UserModel.get_all()

    @staticmethod
    def find_user(ID_USERS):
        return UserModel.get_by_id(ID_USERS)

    @staticmethod
    def add_user(NAMA, EMAIL, PASSWORD, ROLE):
        ID_USERS = UserModel.generate_users_id()
        data = {
            "ID_USERS": ID_USERS,
            "NAMA": NAMA,
            "EMAIL": EMAIL,
            "PASSWORD": PASSWORD,
            "ROLE": ROLE
        }
        UserModel.insert(data)
        print(f"user {NAMA} berhasil ditambahkan dengan ID {ID_USERS}.")

    @staticmethod
    def update_user(ID_USERS,  NAMA=None, EMAIL=None, PASSWORD=None, ROLE=None):
        data = {}
        if NAMA:
            data["NAMA"] = NAMA
        if EMAIL:
            data["EMAIL"] = EMAIL
        if PASSWORD:
            data["PASSWORD"] = PASSWORD
        if ROLE:
            data["ROLE"] = ROLE        
        if data:
            UserModel.update(ID_USERS, data)
            print(f"user dengan ID {ID_USERS} berhasil diperbarui.")
        else:
            print("Tidak ada data yang diubah.")

    @staticmethod
    def delete_user(ID_USERS):
        data = UserModel.get_by_id(ID_USERS)
        if data:
            UserModel.delete(ID_USERS)
            print(f"user dengan ID {ID_USERS} berhasil dihapus.")
        else:
            print(f"Tidak ada data yang ditemukan dengan ID {ID_USERS}.")