L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

minimum = L[0]
maximum = L[0]
for nombre in L:
    if nombre < minimum:
        minimum = nombre
    elif nombre > maximum:
        maximum = nombre

print("la valeur min est: ",minimum,"\nla valeur max est: ",maximum)

