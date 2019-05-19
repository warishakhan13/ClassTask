user_input=int(input("What was your score?"))
if user_input <=4.0 and user_input >= 3.5:
    print("your grade is A and your gpa is " +str(user_input))
elif user_input <3.5 and user_input >= 3.0:
    print("your grade is B your gpa is " +str(user_input))
elif user_input <3.0 and user_input >=2.5:
    print("your grade is C your gpa is " +str(user_input))
else:
    print("Sorry you are fail")
