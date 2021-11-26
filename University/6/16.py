array = [12,6,4,9,3]
i=0


def display():
    text=str(array[i])
    text=text+": "
    j=0
    while j < array[i]:
        text=text+"*"
        j=j+1
    print(text)

while i < len(array):
    display()
    i=i+1