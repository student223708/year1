array_a = [4,36,12,28,9,44,5]
array_b = [5,1,36]

a = array_a[0]
b = array_b[0]
i=0
j=0

while i < len(array_a):
    
    while array_a[i] != array_b[j]:
        j=j+1
        if j > len(array_b):break
    if j > len(array_b):print(array_a[i])
    i=i+1
    j=0