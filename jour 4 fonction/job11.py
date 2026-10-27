def time_to_text(nombre):
    heures = nombre // 60
    minutes = nombre % 60
    print(heures, "heures et ", minutes, "minutes")

nombre = int(input("Entre un nombre de mnutes: "))
time_to_text(nombre)