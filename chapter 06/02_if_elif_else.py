age = int(input("Enter you age : "))

if( age >= 18): 
    print("You are above the age of consent")

elif( age < 0):
    print("You are enter negative age this is not valid")

elif( age == 0 ):
    print("0 is invalid syntax")
    
else: 
    print("You are below the age of consent")