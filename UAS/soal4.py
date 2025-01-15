class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.harga = warna
        self.rasa = rasa

    def setwarna(self, item):
        self.harga = item

    def setnama(self, item):
        self.nama = item

    def setrasa(self, item):
        self.rasa = item

    def information(self): 
        return f'Nama buah adalah : {self.nama} , warna buah adalah : {self.harga} dan rasanya adalah : {self.rasa}'
    
    # ini adalah instance objek nya hehe
buah1 = Buah('Apel', 'Merah', 'Manis')
buah2 = Buah('Jeruk', 'Orange', 'Asam')

print(buah1.information())
print(buah2.information())