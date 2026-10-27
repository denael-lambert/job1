width = int(input("base width: "))
n=0

gauche = width // 2 - 1 

for i in range(width // 2 - 1):
    bord = " " * gauche + "/" + " " * n + "\\"
    print(bord)
    gauche -= 1
    n += 2

base = ("/" + "_" * (width - 2) + "\\")
print(base)

