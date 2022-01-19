def occurs(number, array):
    
    for i in array:
      if i == number: return True 
    return False
       
occurs(int(input("Enter number: ")),[15, 38, 7, 23, 14])
       