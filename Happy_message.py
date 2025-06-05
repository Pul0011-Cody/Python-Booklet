# Gets happiness on a scale of 1 to 10
happiness = int(input("How happy are you today on a scale of 1 to 10? "))
# If the happiness is less than 3 then it prints this
if happiness < 3:
    print("I hope your day becomes better!")
# If happiness is between 4 and 7 then it prints this
elif 4 < happiness < 7:
    print("It's an average day")
# If happiness is anything else it prints this
else:
    print("I hope your day continues to be as great!")

