def bubblesort(array):  
    i=0
    buffer=0
    while i<len(array):
        j=i+1
        
        while j<len(array):
            if array[i] < array[j]:
                buffer=array[i]
                array[i]=array[j]
                array[j]=buffer
                
            j=j+1
        print (array[i])
        i=i+1 
    
    
tab =[4,36,12,28,9,44,5]
    
bubblesort(tab)