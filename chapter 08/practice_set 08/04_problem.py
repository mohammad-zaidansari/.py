# Write a recursive function to calculate the sum of first n natural numbers.

'''
sum(1)=  1
sum(2)=  1 + 2
sum(3)=  1 + 2 + 3
sum(4)=  1 + 2 + 3 + 4

sum(n)=  1 + 2 + 3 + 4 + ...n-1 + n
sum(n)= sum(n-1) + n
'''

def sum_of_first(num):
    if(num == 1):     # this is a base condition it's very importent in recursion 
        return 1
    return sum_of_first(num-1) + num

a = int(input("Enter a nuber: "))
print(f"The sum of first {a} natural number is : {sum_of_first(a)}")