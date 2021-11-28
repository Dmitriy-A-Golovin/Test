n = int(input())
m = int(input())
otvet = []
krug_mass = m * [int(i) for i in range(1, n + 1)]
first = 0
while first != 1:
    otvet.append(krug_mass[0])
    first = krug_mass[m - 1]
    for i in range(m - 2, -1, -1):
        krug_mass.pop(i)
for i in range(len(otvet)):
    print(otvet[i], end='')
