class Queue:
    def __init__(self):
        """Inisialisasi antrian kosong."""
        self.items = []

    def is_empty(self):
        """Memeriksa apakah antrian kosong."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Menambahkan item ke dalam antrian (operasi Enqueue)."""
        self.items.append(item)
        print(f"{item} berhasil ditambahkan ke dalam antrian.")

    def dequeue(self):
        """Menghapus item dari antrian sesuai konsep FIFO (operasi Dequeue)."""
        if self.is_empty():
            print("Antrian kosong. Tidak ada item untuk dihapus.")
            return None
        removed_item = self.items.pop(0)
        print(f"{removed_item} berhasil dihapus dari antrian.")
        return removed_item

    def display(self):
        """Menampilkan semua item di dalam antrian."""
        if self.is_empty():
            print("Antrian kosong.")
        else:
            print("Isi antrian:", " <- ".join(map(str, self.items)))

def menu_interaktif():
    """Fungsi untuk menjalankan menu interaktif simulasi antrian."""
    queue = Queue()
    while True:
        print("\nMenu:")
        print("1. Tambahkan ke antrian (Enqueue)")
        print("2. Hapus dari antrian (Dequeue)")
        print("3. Tampilkan antrian")
        print("4. Keluar")

        try:
            pilihan = int(input("Pilih operasi (1-4): "))
        except ValueError:
            print("Harap masukkan angkat 1 sampai 3.")
            continue

        if pilihan == 1:
            item = input("Masukkan yang ingin ditambahkan: ")
            queue.enqueue(item)
        elif pilihan == 2:
            queue.dequeue()
        elif pilihan == 3:
            queue.display()
        elif pilihan == 4:
            print("Keluar mingat")
            break
        else:
            print("Patuhi peraturan yang ada.")

if __name__ == "__main__":
    menu_interaktif()
