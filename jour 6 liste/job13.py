liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
 
sans_doublons = []
 
for nombre in liste:
    deja_present = False
    for element in sans_doublons:
        if element == nombre:
            deja_present = True
    if not deja_present:
        sans_doublons = sans_doublons + [nombre]
 
print(sans_doublons)
