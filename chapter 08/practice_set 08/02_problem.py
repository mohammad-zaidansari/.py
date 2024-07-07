# Write a python program using function to convert Celsius to Fahrenheit.

def FtoC(val):
    cal = ( val - 32 ) * 5/9
    return cal

num = int(input("Enter fahrenheit value: "))
cal = FtoC(num)
print(f"{num}°F = {cal}°C")
print(f"{num}°F = {round(cal, 2)}°C")