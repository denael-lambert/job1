nom = "Cookies" 
prix_unitaire = 12.99
quantité_en_stock = 1345

print("Il y a ", quantité_en_stock,nom,"en stock au prix de ", prix_unitaire)

print ("Combien de" ,nom, "voulez vous acheter ?")
x = int(input())
quantité_en_stock-=x
print ("vous avez acheté",x,nom, ",le stock est maintenant",quantité_en_stock)