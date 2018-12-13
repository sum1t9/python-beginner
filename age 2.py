age = eval(input("Enter the Age "))
if (age<5):
    print("Too early")

elif(age == 5):
    print("Go to Kindergarten")

elif(age>5)and(age <=17):
    grade = age - 5
    if(grade == 1):
            print("usually {} years old go to {}st grade".format(age,grade))
    elif(grade == 2):
            print("usually {} years old go to {}nd grade".format(age, grade))
    elif(grade == 3):
            print("usually {} years old go to {}rd grade".format(age, grade))
    else:
            print("usually {} years old go to {}th grade".format(age,grade))
else:
    print("usually {} yr olds go to college".format(age))