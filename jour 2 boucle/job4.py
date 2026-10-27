nombre = int(input("saisir un nombre entier supérieur à 0: "))
if nombre <=0:
    print("erreur, besoin d'un entier supérieur à 0")
else:
    for table in range (1,nombre+1):
        print(f"Table de {table} :")
        for i in range(1, 11):              
            print(f"{table} x {i} = {table * i}")
    
