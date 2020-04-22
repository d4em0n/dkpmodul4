from string import capwords # berfungsi untuk mengubah awal huruf pada setiap kata menjadi huruf besar

MAKANAN = 1
MINUMAN = 2
daftar_makanan = []
daftar_minuman = []
class Menu:
  def __init__(self, nama, harga, stok, desc, tipe):
    self.nama = nama
    self.harga = harga
    self.stok = stok
    self.desc = desc
    self.tipe = tipe

  def tampil(self):
    if self.tipe == MAKANAN:
      tipe = "Deskripsi makanan " + self.nama
    elif self.tipe == MINUMAN:
      tipe = "Deskripsi minuman " + self.nama
    else:
      print(self.nama + " bukan makanan atau minuman :/")
      return
    deskripsi = capwords(self.nama) + " adalah " + self.desc
    print(tipe)
    print(deskripsi)
    print("Harga: {}".format(self.harga))

def tambah_makanan(nama, harga, stok, desc):
  daftar_makanan.append(Menu(nama, harga, stok, desc, MAKANAN))

def tambah_minuman(nama, harga, stok, desc):
  daftar_minuman.append(Menu(nama, harga, stok, desc, MINUMAN))

tambah_makanan("soto ayam", 20000, 200, "makanan khas Indonesia yang berupa sejenis sup ayam dengan kuah yang berwarna kekuningan")
tambah_makanan("sate ayam", 30000, 200, "makanan khas Indonesia. Sate Ayam dibuat dari daging ayam. Pada umumnya sate ayam dimasak dengan cara dipanggang dengan menggunakan arang dan disajikan dengan pilihan bumbu kacang atau bumbu kecap")
tambah_makanan("sate kambing", 35000, 100, "sejenis makanan sate terbuat dari daging kambing. Daging kambing tersebut disate dan dibumbui dengan rempah-rempah dan bumbu dapur, kemudian dibakar. Penyajiannya disajikan bersama lalapan kubis, tomat, dan bawang merah yang diiris tipis kemudian diberi kecap dan ditambahkan taburan merica.")
tambah_makanan("ketoprak", 18000, 300, "makanan yang berisi lontong nasi dan disausi dengan bumbu saus kacang, ditaburi dengan kerupuk")

tambah_minuman("es cincau", 12000, 200, "minuman penyegar dengan bahan utama gel yang mirip agar-agar yang dikenal sebagai cincau. Potongan cincau ditambah dengan sirup, santan dan es serut sehingga menjadi minuman penyegar.")
tambah_minuman("es cendol", 12000, 200, "minuman tradisional khas Indonesia yang dahulunya terbuat dari tepung hunkwe, tetapi kini cendol terbuat dari tepung beras, disajikan dengan es parut serta gula merah cair dan santan. Minuman ini memiliki rasa yang manis dan gurih.")
tambah_minuman("es kelapa muda", 12000, 200, "minuman segar penyejuk dahaga yang terbuat dari daging dan air kelapa yang masih muda")
tambah_minuman("es campur", 15000, 200, "salah satu minuman khas Indonesia yang cara membuat nya dengan mencampurkan berbagai jenis bahan dalam sirup manis. Bahan yang dijadikan bahan biasanya berasa manis atau masam")

keranjang = []
def menu(daftar_item):
  print("Menampilkan daftar menu yang tersedia, ketik 0 untuk kembali")
  while True:
    # menampilkan semua makanan yang ada di daftar makanan
    print("0. Kembali")
    for i in range(len(daftar_item)):
      print("{}. {}".format(i+1, capwords(daftar_item[i].nama)))
    pilih = int(input("Pilih> "))
    if pilih == 0:
      return
    pilih = pilih - 1 # Kurangi menu yang dipilih dengan 1 untuk mengakses list
    if pilih not in range(len(daftar_item)):
      print("Item yang anda pilih tidak terdapat pada menu")
      continue
    daftar_item[pilih].tampil()
    while True:
      p = input("Apakah anda ingin memilih ini? Y/N> ")
      if p == 'Y':
        keranjang.append(daftar_item[i])
        print("Item ini telah ditambahkan ke keranjang")
        break
      elif p == 'N':
        break
def lihat_keranjang():
  i = 1
  total = 0
  for item in keranjang:
    print("{}. {} = {}".format(i, item.nama.ljust(20, " "), item.harga))
    total += item.harga
    i += 1
  print("Harga total = {}".format(total))
  
while True:
  print("[1] Lihat menu makanan")
  print("[2] Lihat menu minuman")
  print("[3] Lihat keranjang")
  print("[4] Tutup menu")
  pilih = int(input("Pilih> "))
  if pilih == 1:
    menu(daftar_makanan)
  elif pilih == 2:
    menu(daftar_minuman)
  elif pilih == 3:
    lihat_keranjang()
  else:
    break
