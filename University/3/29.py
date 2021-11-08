numbers=0
sum=0
while True:
    guess=input("Enter number: ")
    if guess!='0':
        numbers=numbers+1
        guess=int(guess)
        sum=sum+guess
        
    if guess=='0':print("RESULT: Quantity:",numbers,"Sum:",sum,"Mean:",sum/numbers)
      
