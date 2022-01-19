def function(array):
    x=max(array)
    y=array.count(x)
    
    i=0
    
    while i != y:
        array.remove(x)
        i=i+1
    
    return max(array)
        