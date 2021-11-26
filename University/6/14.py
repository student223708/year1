array = ["Genowefa","Onufry", "Celestyna", "Alojzy", "Pankracy"]

i = 0
max =""

while i < (len(array)):
    if len(max) < len(array[i]):
        max=array[i]
    i=i+1
print(max)