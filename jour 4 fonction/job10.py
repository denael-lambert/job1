def detector(x):
    if x%2 == 0:
        print("pair")
    if x%2 == 1:
        print("impair")

x = int(input("entre un nombre: "))

detector(x)