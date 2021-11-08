primes=0
x=2
number=2
n=int(input("Enter N: "))


print("Prime numbers:")
while primes<n:
    while x<=number:
        if number==x:
            primes=primes+1
            print(number)
            break
        elif number%x==0:
            break
        else:
            x=x+1
    number=number+1
    x=2


           