width = int(input("width: "))
height = int(input("height: "))

bord = ("|" + "-" * (width - 2) + "|")
millieu = ("|" + " " * (width - 2) + "|")

print(bord) 
for i in range(height):
    print(millieu)
print(bord) 

