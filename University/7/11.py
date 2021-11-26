film_titles = ["Shrek", "Shrek 2", "Shrek 3", "Leon the proffesionl", "Scarface"]

file = open("films.txt", "w")

for i in film_titles:
    file.write(i + "\n")
file.close()