money=int(input("Enter the amount in PLN:" ))

m1=0
m2=0
m5=0
while money-5>=0: 
    m5=m5+1
    money=money-5
    
while money-2>=0:
    m2=m2+1
    money=money-2
    
while money-1>=0:
    m1=m1+1
    money=money-1

print("The amount of",money,"in coins: ")
print("5zl -",m5)
print("2zl -",m2)
print("1zl -",m1)