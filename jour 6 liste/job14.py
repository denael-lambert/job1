def longueur(chaine):
    n = 0                    
    for loops in chaine:
        n += 1
    return n


def my_long_word(n, texte):
    resultat = []
    for mot in texte.split():
        mot = mot.strip(",.;:!?")      
        if longueur(mot) > n:
            resultat.append(mot)
    return " ".join(resultat)





phrase = ("La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")

print(my_long_word(3,phrase))


