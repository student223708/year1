a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

if   (a>=0) and (b>=0):print("Point P(",a,",",b,") is in the first quadrant of the coordinate system")
elif (a<0) and (b>=0):print("Point P(",a,",",b,") is in the second quadrant of the coordinate system")
elif (a<0) and (b<0):print("Point P(",a,",",b,") is in the third quadrant of the coordinate system")
elif (a>=0) and (b<0):print("Point P(",a,",",b,") is in the fourth quadrant of the coordinate system")