# gets the amount of pictures
pictures = int(input("How many pictures have you taken this month? "))
# gets the amount of texts
texts = int(input("How many texts have you send this month? "))
# gets the amount of data used
data = int(input("How much data have you used this month? (Mb) "))
# Times them by the cost
picture_cost = pictures * 0.35
text_cost = texts * 0.10
data_cost = data * 0.05
# Adds them together
total_cost = picture_cost + text_cost + data_cost
# If it is greater than 10 then it prints:
if total_cost > 10:
    print("You should consider upgrading your current plan")
# If it is below 10 it prints this:
else:
    print("You are doing good")
print("You have spent", total_cost, "dollars this month")