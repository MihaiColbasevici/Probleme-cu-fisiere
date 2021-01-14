with open("numere.txt", 'w') as f:
    f.write(input("Dati 2 numere: "))
with open("numere.txt", 'r') as k:
    var = k.read()
    a, b = var.split()
c = min(a, b)
with open('minim.txt', 'w') as i:
    i.write(c)