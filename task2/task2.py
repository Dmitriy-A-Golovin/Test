data1 = []
with open("файл1.txt") as f:
    for line in f:
        data1.append([float(x) for x in line.split()])
centr = data1[0]
rad1 = data1[1][0]
otvet = []
with open("файл2.txt") as f:
    for line in f:
        tochka = [float(x) for x in line.split()]
        rad2 = ((centr[0] - tochka[0]) ** 2 +  (centr[1] - tochka[1]) ** 2) ** (0.5)
        if rad1 > rad2:
            otvet.append(1)
        elif rad1 < rad2:
            otvet.append(2)
        else:
            otvet.append(0)
        
for i in range(len(otvet)):
    print(otvet[i])
