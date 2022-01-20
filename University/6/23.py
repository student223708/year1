def median(array):
    if len(array)%2==0:
        return ((array[(len(array)/2)-1] + array[len(array)/2])/2)
    else:
        return array[int((len(array)-1)/2)]
    
print(median([1,0,9,4,6]))
print(median([6,8,3,1,0,5,7]))