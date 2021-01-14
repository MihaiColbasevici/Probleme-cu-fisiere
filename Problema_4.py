with open("input.txt", 'w') as f:
    f.write(input("Ce numar a spus Ion?   "))
with open("input.txt", 'r') as k:
    num = k.read()
num = int(num)
vasile = [str(num - 2) + " ", str(num - 1) + " ", str(num) + " ", str(num + 1) + " ", str(num + 2)]
with open('output.txt', 'w') as i:
    i.write(vasile[0])
    i.write(vasile[1])
    i.write(vasile[2])
    i.write(vasile[3])
    i.write(vasile[4])