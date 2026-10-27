n = 1 + int(input("taille du tapis: ")) 
j=0


bord = ("+" + "-" * (n+1) + "+")

print(bord) 

for i in range(n):
    print("|" + "#"*(n) + " " + "#"*(j) + "|")
    n-=1
    j+=1

print(bord) 

