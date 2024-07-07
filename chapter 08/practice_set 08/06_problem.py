# Write a python function which converts inches to cms.

def inches_to_cms(inch):
    cms =  inch * 2.54 
    return cms

num = float(input("Inches = "))
print(f"{num} inches = {inches_to_cms(num)} cms")

