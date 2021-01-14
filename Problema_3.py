with open("globulete.txt", 'w') as f:
    f.write(input("Dati numarul de globulete albe: "))
with open("globulete.txt", 'r') as k:
    a = k.read()
a = int(a)
r = a +3
alb = (a + r) - 2
suma = str(a + r + alb)
with open('bradut.txt', 'w') as i:
    i.write(suma)

