file = open("imie.txt" , "w")

data =""
data = input("Podaj imie: ")
file.write(data + '\n')

data = input("Podaj nazwisko: ")
file.write(data + '\n')

data = input("Podaj uniwersytet: ")
file.write(data + '\n')

data = input("Podaj kierunek: ")
file.write(data + '\n')

file.close()