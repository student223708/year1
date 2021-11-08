a=int(input("Width: "))
b=int(input("Height: "))
      
i=1
j=1

if b>=1:
    text=a*'*'
    print(text)
    text=''
      
while i<=b-2:
    text='*'+(a-2)*' '+'*'
    print(text)
    text=''
    i=i+1
      
if b>=2:
    text=a*'*'
    print(text)
    text=''
    