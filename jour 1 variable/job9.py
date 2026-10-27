montant_initial = int(input())
rendement_pourcentage = int(input())

x = montant_initial * (rendement_pourcentage / 100)
montant_initial + x
print(x)
print ("Le gain annuel est de",x, "€")

y = (montant_initial + x) 
z = y*0.9
print(z,"€ apres le retrait")
rendement_pourcentage -=1
print("rendement_pourcentage =",rendement_pourcentage,"%")

f = z*(rendement_pourcentage / 100)
p = f+z                    
print("la somme finale est de", p)
