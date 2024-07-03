mark1 = float(input("Enter you marks in english: "))
mark2 = float(input("Enter you marks in hindi: "))
mark3 = float(input("Enter you marks in mathametics: "))
mark4 = float(input("Enter you marks in science: "))

prg_marks =( mark1+mark2+mark3+mark4) * 100/400

print(prg_marks)

if( prg_marks >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33 and mark4 >= 33 ):
    print("You are passed: ", prg_marks)
else: 
    print("You failed, try again next year: ", prg_marks)

# if(prg_marks <= 33):
#     print("you are fail try again next year")
# elif( prg_marks <= 44):
#     print("good")
# elif( prg_marks <= 66):
#     print("excellent")

# if(prg_marks >= 33):
#     print("PASS")
# elif(prg_marks > 44):
#     print("Good")
# elif(prg_marks <= 33):
#     print("Failed")
# else:
#     print("enter valid nubmer")