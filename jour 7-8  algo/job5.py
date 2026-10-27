def calc(nombre,hauteur):
    n = nombre*hauteur*7*10
    return n/100

x = int(input("nombre de marches: "))
y = int(input("hauteur des marches en cm: "))

resul = calc(x,y)
print("Pour",x," marches de", y," cm, le gardien parcourt", resul, "m par semaine.")
    
