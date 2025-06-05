# Gets the 2 numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# If number 1 is greater than 2 then it prints 1 is greater than 2
if num1 > num2:
    print (num1, " is greater than ", num2)
# If number 1 is less than number 2 then it prints 1 is less than 2
elif num1 < num2:
    print (num2, " is greater than", num1)
# If number 1 is equal to number 2 then it prints number 1 is equal to number 2
else:
    print (num1, "is equal to", num2)