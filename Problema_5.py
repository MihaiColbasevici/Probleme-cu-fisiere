with open("numar.txt", 'w') as f:
    f.write(input("Dati un numar: "))
with open("numar.txt", 'r') as k:
    num = k.read()
num = int(num)
with open('inmultire.txt', 'w') as i:
    for j in range(0, 11):
        inm = str(num) + " x " + str(j) + " = " + str(j * num) + '\n'
        i.write(inm)