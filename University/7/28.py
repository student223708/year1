import re

avg=float(0)    

file = open("grades.txt","r")

grade=""

for i in file:
    if i[0]=='G':
        grade=re.findall("\d\.\d",i)
        for x in grade:
            avg =avg+float(x)
        avg=avg/float(len(grade))
file.close()
    
    
print(avg)

