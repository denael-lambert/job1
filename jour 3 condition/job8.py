a = int(input("longueur A: "))
b = int(input("longueur B: "))
c = int(input("longueur C: "))

if a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b:
    print("on ne peut pas construire ce triangle")
else:
    rectangle = a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2
    isocele = a == b or b == c or a == c

    if a == b == c:
        print("le triangle est équilatéral")
    elif rectangle and isocele:
        print("le triangle est rectangle et isocèle")
    elif rectangle:
        print("le triangle est rectangle")
    elif isocele:
        print("le triangle est isocèle")
    else:
        print("le triangle est quelconque")