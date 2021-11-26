x=[1,2,3]

def function(x):
    odd=0
    even=0
    i=0
    for i in x:
        if(i%2==0):odd=odd+1
        else:even=even+1
        i=i+1           
    print(odd)
    print(even)