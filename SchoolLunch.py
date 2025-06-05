# Gets amount brought
Amountbring = int(input("How much money did you bring to school today? "))
# Gets amount spent
Amountspent = int(input('How much money did you spend on your school lunch? '))
# Subtracks amount brought with amount spent
Moneyleft = Amountbring - Amountspent
# Prints the data
print('You have spent', Amountspent, "dollars from your", Amountbring, "dollars")
print("You still have", Moneyleft, "dollars to spend")  
