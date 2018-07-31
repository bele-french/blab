import random

classes=['Science', 'English', 'Math', 'History']
firstname= input("What is your first name?")
lastname= input("What is your last name?")
for school in classes:
    gpa = random.randint(255,400)/100
    if gpa <= 2.5:
        print("You failed this classes")
    elif gpa >= 2.6 and gpa <= 3.0:
        print("You got a B")
    else:
        print("You got an A")
