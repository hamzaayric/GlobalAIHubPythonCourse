SatırSayısı = 3
SütunSayısı = 3


matrix = []


for i in range(SatırSayısı):
    a = []
    for j in range(SütunSayısı):
        AsalSayı = int(input("Asal sayı giriniz : "))
        a.append(AsalSayı)
    matrix.append(a)


for i in range(SatırSayısı):
    for j in range(SütunSayısı):
        print(matrix[i][j], end=" ")
    print()
