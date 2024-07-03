name = input("Enter you name: ")

if(len(name) < 10):
    print("This name contain less then 10 characters", name)
elif(len(name) == 10 ):
    print("This name contain equal to 10 characters")
else:
    print("This name contain more then 10 characters")
