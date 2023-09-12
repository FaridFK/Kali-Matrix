def getmatriks():
    datamatriks = []
    for matriks in range(1, 3):
        baris = int(input("Masukkan jumlah baris matriks ke-{0} : ".format(matriks)))
        kolom = int(input("Masukkan jumlah kolom matriks ke-{0} : ".format(matriks)))
        datamatriks.append(isimatriks(matriks,baris,kolom))
    print(datamatriks)
    perkalianmatriks(datamatriks[0], datamatriks[1])
    
def isimatriks(indexmatriks, barismatriks, kolommatriks):
    matriks = []
    for baris in range(barismatriks):
        datamatriks = []
        for kolom in range(kolommatriks):
            datamatriks.append(int(input("Matriks ke -[0] [{1}, {2}] = ".format(indexmatriks,baris,kolom))))
        matriks.append(datamatriks)
    print(matriks)
    return matriks

def perkalianmatriks(matrikspertama, matrikskedua):
    hasil = []
    for x in range(len(matrikspertama)):
        baris = []
        for y in range(len(matrikspertama[0])):
            jumlah = 0
            for z in range(len(matrikspertama)):
                jumlah += (matrikspertama[x][z] * matrikskedua[z][y])
                
                print(x,y,z)
            baris.append(jumlah)
        hasil.append(baris)
    
    print(hasil)
getmatriks()
