type = str(input("fruit ou légume ?: "))
saison = str(input("été ou hiver ?: "))

def job8(type,saison):
    if type == "fruit" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruit" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaut, aubergine,navet")
    else:
        print("t nul")

job8(type,saison)