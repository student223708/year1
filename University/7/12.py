while True:
    file = open("shopping.txt", "a")
    file.write(input("Podaj nowy przedmiot: ") + '\n')
    file.close()