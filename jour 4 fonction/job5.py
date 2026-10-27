def calcule(num1,operator,num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Erreur : division par zéro"
        return num1 / num2
    elif operator == "%":
        if num2 == 0:
            return "Erreur : modulo par zéro"
        return num1 % num2
    else:
        return "Erreur : opérateur invalide"

num1 = int(input("num 1: "))
operator = str(input("operator: "))
num2 = int(input("num 2: "))

print(calcule(num1,operator,num2))