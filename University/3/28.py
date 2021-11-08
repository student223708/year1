last1=0
last2=1
i=1
print("0 1")
while i<=48:
    fib=last1+last2
    print(fib)
    last2=last1
    last1=fib
    i=i+1