import re

class Data:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        self.products.append({"name": name, "price": price, "quantity": quantity})

    def get_all(self):
        return self.products

    def calculate_total(self):
        return sum(product['price'] * product['quantity'] for product in self.products)


class View:
    @staticmethod
    def display_table(data):
        print("+----------------+---------+----------+")
        print("| Produk         | Harga   | Jumlah   |")
        print("+----------------+---------+----------+")
        for entry in data:
            print(f"| {entry['name']:<14} | {entry['price']:<7} | {entry['quantity']:<8} |")
        print("+----------------+---------+----------+")

    @staticmethod
    def display_total(total):
        print(f"Total harga: Rp{total}")

    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def display_message(message):
        print(message)


class Process:
    def __init__(self, data, view):
        self.data = data
        self.view = view

    def add_product_data(self):
        while True:
            try:
                name = self.view.get_input("Masukkan nama produk: ")
                if not name.strip():
                    raise ValueError("Nama produk tidak boleh kosong.")

                price = self.view.get_input("Masukkan harga produk (angka positif): ")
                if not price.isdigit() or int(price) <= 0:
                    raise ValueError("Harga harus berupa angka positif.")

                quantity = self.view.get_input("Masukkan jumlah produk (angka positif): ")
                if not quantity.isdigit() or int(quantity) <= 0:
                    raise ValueError("Jumlah harus berupa angka positif.")

                self.data.add_product(name, int(price), int(quantity))
                self.view.display_message("Produk berhasil ditambahkan.")

                add_more = self.view.get_input("Apakah ingin menambahkan produk lagi? (ya/tidak): ").strip().lower()
                if add_more != "ya":
                    break

            except ValueError as e:
                self.view.display_message(f"Kesalahan: {e}")

    def show_products_data(self):
        all_data = self.data.get_all()
        if not all_data:
            self.view.display_message("Belum ada data produk yang tersedia.")
        else:
            self.view.display_table(all_data)
            total = self.data.calculate_total()
            self.view.display_total(total)


# Main program
def main():
    data = Data()
    view = View()
    process = Process(data, view)

    while True:
        view.display_message("\n1. Tambah Produk\n2. Tampilkan Data Produk\n3. Keluar")
        choice = view.get_input("Pilih opsi: ")

        if choice == "1":
            process.add_product_data()
        elif choice == "2":
            process.show_products_data()
        elif choice == "3":
            view.display_message("Keluar dari program. Terima kasih!")
            break
        else:
            view.display_message("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
