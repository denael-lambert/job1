L = [9,5,14,77,12,987,30,-1,6,6]


def longueur(liste):
    n = 0                    
    for loops in L:
        n += 1
    return n
    
def sorter(liste):
    n = longueur(liste)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

print("Avant :", L)
print("Après :", sorter(L))
    
















