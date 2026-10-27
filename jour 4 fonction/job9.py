def moyenne(n1,n2,n3):
    moyenne_etudiant = (n1+n2+n3)/3
    if moyenne_etudiant >= 15:
        print("Très bon élève, ",moyenne_etudiant,"de moyenne")
    elif moyenne_etudiant >= 11 and moyenne_etudiant <= 15: 
        print("Bon élève, ",moyenne_etudiant,"de moyenne")
    elif moyenne_etudiant >= 8 and moyenne_etudiant <= 10:
        print("Élève moyen, ",moyenne_etudiant,"de moyenne")
    elif  moyenne_etudiant <= 7:
        print("Élève devant faire des efforts, ",moyenne_etudiant,"de moyenne")

n1 = float(input("note n°1: "))
n2 = float(input("note n°2: "))
n3 = float(input("note n°3: "))

moyenne(n1,n2,n3)