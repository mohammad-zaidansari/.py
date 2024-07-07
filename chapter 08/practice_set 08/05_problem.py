# Write a program to print the following star pattern.
# *
# ***
# ***** for n = 3

def pattern(n):
    if(n==0):
        return
    print("*" *n)
    pattern(n-1)

a = int(input("Enter a number: "))
pattern(a)

# n = 3 
# for i in range(n, 0, -1):
#     print("*"* i)


'''
Syntax of range:

range(start, stop, step)
start: The starting value of the sequence.
stop: The endpoint of the sequence (not included in the range).
step: The increment (or decrement) between each value in the sequence.

Usage in for i in range(n, 0, -1):
start = n: The loop starts at n (in this case, 3).
stop = 0: The loop stops before reaching 0 (so it will include 1 but not 0).
step = -1: The loop decrements i by 1 in each iteration.
'''


