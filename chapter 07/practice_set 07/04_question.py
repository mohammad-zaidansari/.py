# Write a program to find whether a given number is prime or not.

num = int(input("Enter a number check whether it is prime or not: "))

# if (num % 2) == 0:
#     print("This number is prime")
# else:
#     print("This number is not prime")

for i in range(2, num):
    if (num%i) == 0:
        print("Number is not prime")
        break
else: 
    print("Number is prime")
