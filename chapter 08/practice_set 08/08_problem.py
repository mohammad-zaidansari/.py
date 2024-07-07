#  Write a python function to print multiplication table of a given number.

def table(num):
    for i in range(1, 11):
        cal = print(f"{num} X {i} = { num * i}")
   

a = int(input("Enter a number: "))
table(a)

