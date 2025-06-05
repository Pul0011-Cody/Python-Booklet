# Is the password
password = 2345
# Asks for the password
input_password = int(input("What is the password? "))
# If password is correct it does this:
if input_password == password:
    pictures = int(input("How many pictures have you taken this month? "))
    texts = int(input("How many texts have you send this month? "))
    data = int(input("How much data have you used this month? (Mb) "))
    picture_cost = pictures * 0.35
    text_cost = texts * 0.10
    data_cost = data * 0.05
    total_cost = picture_cost + text_cost + data_cost
    if total_cost > 10:
        print("You should consider upgrading your current plan")
    else:
        print("You are doing good")
    print("You have spent", total_cost, "dollars this month")
# If password is wrong it does this:
else:
    print("Password is Incorrect")