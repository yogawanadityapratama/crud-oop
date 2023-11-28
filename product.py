class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def product_info(self):
        print("Id Produk: {}, Nama Produk: {}, Harga Produk: {}".format(
            self.id,
            self.nama,
            self.price
        ))