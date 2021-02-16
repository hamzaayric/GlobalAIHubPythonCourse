SatırSayısı = 3
SütunSayısı = 3

print("\n Rastgele 9 tane asal sayı girin \n")
matrix = []


for i in range(SatırSayısı):
    a = []
    for j in range(SütunSayısı):
        AsalSayı = int(input("Asal sayı : "))
        a.append(AsalSayı)
    matrix.append(a)


for i in range(SatırSayısı):
    for j in range(SütunSayısı):
        print(matrix[i][j], end=" ")
    print()
