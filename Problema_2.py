with open("numere.txt", 'w') as f:
    f.write(input("Dati 2 numere: "))
with open("numere.txt", 'r') as k:
    var = k.read()
    a, b = var.split()
a = int(a)
b = int(b)
min_ = str(min(a, b) * 3)
max_ = str(max(a, b) * 2)
with open('produs.txt', 'w') as i:
    i.write(min_)
    i.write(" ")
    i.write(max_)
