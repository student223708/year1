def power(x,n):
    if n == 0: return 1
    elif n == 1: return x
    else: return (x*power(x,n-1))
    
x = int(input("Enter base of the power: "))
n = int(input("Enter power value: "))

print (power(x,n))