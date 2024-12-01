def show_header(title):
    """Menampilkan header dengan title."""
    print("\n" + "=" * len(title))
    print(title.upper())
    print("=" * len(title))

def show_menu(options):
    """Menampilkan menu dan meminta input dari pengguna."""
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")
    print("0. Keluar")
    choice = input("Pilih menu: ").strip()
    return choice

class BaseView:
    @staticmethod
    def clear_screen():
        """Membersihkan layar."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def pause():
        """Pause layar."""
        input("\nTekan Enter untuk melanjutkan...")
