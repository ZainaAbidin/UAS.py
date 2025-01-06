# Kelas Data
Kelas ini bertanggung jawab untuk menyimpan dan mengelola 
data produk. Kelas ini memiliki metode berikut:
__init__: Inisialisasi daftar kosong products yang akan menyimpan data produk.
add_product: Menambahkan produk ke dalam daftar products dengan 
format dictionary yang mencakup name, price, dan quantity.
get_all: Mengembalikan semua data produk yang tersimpan dalam daftar products.
calculate_total: Menghitung total harga semua produk dalam daftar 
dengan mengalikan harga (price) dengan jumlah (quantity) untuk 
setiap produk dan menjumlahkan hasilnya.

# Kelas View
Kelas ini bertanggung jawab untuk berinteraksi dengan pengguna, seperti 
menampilkan data dan menerima input. Metode yang ada meliputi:
display_table: Menampilkan tabel produk dalam format rapi dengan kolom: "Produk", "Harga", dan "Jumlah".
display_total: Menampilkan total harga dari semua produk.
get_input: Menerima input dari pengguna dengan pesan tertentu.
display_message: Menampilkan pesan tertentu kepada pengguna.

# Kelas Process
Kelas ini bertindak sebagai penghubung antara Data dan View. Fungsinya adalah untuk mengatur alur kerja program:
add_product_data: Mengelola proses penambahan produk baru dengan langkah-langkah berikut:
Meminta input nama, harga, dan jumlah produk dari pengguna.
Memvalidasi bahwa semua input adalah valid (nama tidak kosong, harga dan jumlah adalah angka positif).
Menambahkan data produk ke kelas Data jika valid.
Menampilkan pesan sukses atau kesalahan kepada pengguna.
Memberikan opsi kepada pengguna untuk menambah produk lagi atau tidak.
show_products_data: Mengelola tampilan data produk. Jika tidak ada data, akan menampilkan
pesan bahwa data belum tersedia. Jika ada data, akan 
menampilkan tabel produk beserta total harga.
