# Write a program using functions to find greatest of three numbers

def greatestOfThree(a, b, c):
    if(a > b and a > c):
        print(f"Greatest number is {a}")
    elif(b > c and b > a):
        print(f"Greatest number is {b}")
    else:
        print(f"Greatest number is {c}")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

greatestOfThree(num1, num2, num3)



        