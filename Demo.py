# print("hello world"); print("perkenalkan")
# name="Farizd"
# print("My name is " + name)
# print("""Triple tanda petik""")
# if  name == "Farizd" :
#     print("Benar namanya")
# # for i in range(10):
# #     print(i)
# umur = int(input("Umur berapa Anda: "))
# print("Umur Anda adalah %d" % umur)
# if umur >= 18:
#     print("Anda sudah cukup umur")
# elif umur >=10 and umur < 18:
#     print("Anda harus tunggu sebentar lagi")
# else:
#     print("Anda belum cukup umur")
# print("Nama Anda %s, dengan umur %d tahun" % (name, umur))
# type(name)
# type(umur)
# aku = "bocah" if umur < 10 else "dewasa"
# print(aku)
# # lulus = raw_input("apakah kamu lulus? [ya/tidak]: ")
# # if lulus == "ya":
# #     print("kamu lulus")
#
# item = ["kopi","gula","teh"]
# for isi in item:
#     print(isi)
#
# jawab = "ya"
# hitung = 0
# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("Apakah tetap dilanjutkan? [ya/tidak] ")
# print("Total perulangan " + str(hitung))

#variable global untuk menyimpan data buku
buku = []

def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))

def insert_data():
    buku_baru = input("Judul buku: ")
    buku.append(buku_baru)

def edit_data():
    show_data()
    indeks = int(input("Input ID buku: "))
    if indeks > len(buku):
        print("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

def delete_data():
    show_data()
    indeks = int(input("Input ID buku "))
    if indeks > len(buku):
        print("ID salah")
    else:
        buku.remove(buku[indeks])

def show_menu():
    print("\n")
    print("---------- MENU -----------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")

    menu = int(input("PILIH MENU "))
    print("\n")
    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Menu yang dipilih tidak ditemukan")

if __name__ == "__main__":
    while(True):
        show_menu()
