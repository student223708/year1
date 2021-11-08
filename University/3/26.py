block=0
pin='0805'
while block!=3:
    guess=input("Enter the PIN code: ")
    if(guess==pin):
        print("Correct")
    else:
        print("Incorrect")
        block=block+1
print("Sorry, your payment card has been blocked.")