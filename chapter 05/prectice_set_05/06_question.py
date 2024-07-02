fav_lang = {}

name1 = input("enter you name: ")
lang1 = input("enter your fav language: ")
fav_lang.update({name1: lang1})
 
name2 = input("enter you name: ")
lang2 = input("enter your fav language: ")
fav_lang.update({name2: lang2})
 
name3 = input("enter you name: ")
lang3 = input("enter your fav language: ")
fav_lang.update({name3: lang3})
 
name4 = input("enter you name: ")
lang4 = input("enter your fav language: ")
fav_lang.update({name4: lang4})
 
print(fav_lang)


# If the names of 2 friends are same; what will happen to the program in problem 6? 

# enter you name: zaid
# enter your fav language: english
# enter you name: zaid
# enter your fav language: hindi
# enter you name: talha
# enter your fav language: urdu 
# enter you name: adif
# enter your fav language: thisl
# Output : {'zaid': 'hindi', 'talha': 'urdu', 'adif': 'thisl'}


# . If languages of two friends are same; what will happen to the program in problem 6?

# enter you name: zaie
# enter your fav language: hindi
# enter you name: asif
# enter your fav language: hindi
# enter you name: talha
# enter your fav language: english
# enter you name: ahad
# enter your fav language: urdu
# Output :  {'zaie': 'hindi', 'asif': 'hindi', 'talha': 'english', 'ahad': 'urdu'}  