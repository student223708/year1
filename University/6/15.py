array = ["red","yellow","green"]
file = open("file.txt", "x")
file.close()

file = open("file.txt", "a")
file.write(array[0])
file.write('\n')
file.write(array[1])
file.write('\n')
file.write(array[2])
file.close()