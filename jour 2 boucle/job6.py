nombre = int(input("saisir un nombre entier supérieur à 0: "))
if nombre <=0:
    print("erreur, besoin d'un entier supérieur à 0")
else:
    x=0
    while x<nombre+1:
     print("7 * ",x, "=", 7*x)     
     x+=1
