DataNamaAslab = ["Arsel","Avivah","Daiva",["Wahyu","Wibi"]]

def linearsearch(Array,x):
    for l in range(len(Array)):
        if type(Array[l]) == list:
            hasil_x = linearsearch(Array[l],x)
            if hasil_x == -1:
                return -1
            else:
                print(f"{x} Ditemukan pada indeks {l} kolom {hasil_x}")
                exit()
        elif Array[l] == x:
            return l
    return -1

print(f"Data Nama Aslab : {DataNamaAslab}")
x = input("Masukan nama aslab yang ingin dicari : ")

Hasil_y = linearsearch(DataNamaAslab,x)

if Hasil_y == -1:
    print("Data tidak ditemukan")

else:
    print(f"{x} Ditemukan pada indeks {Hasil_y}")