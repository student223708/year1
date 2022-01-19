def function(array):
    
    urray=[]
    i=0
    
    while i < len(array):
        check=True
        j=0
        while j< len(array):
            if (array[i] == array[j]) and (i!=j):
                check=False
                break
            j=j+1
        if check :
            urray.append(array[i])
        i=i+1
        
    for i in urray:
        print (i)
        
        
function([2,3,2,5,8,1,9,8])