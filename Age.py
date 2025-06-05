# Gets the name
Name = input("What is your name? ")
# Gets the age
Age = int(input("What is you age? "))
# Works out Hours, minutes and seconds lived
Hourslived = Age * 365 * 24
Minuteslived = Hourslived * 60
Secondslived = Minuteslived * 60
# Prints out Hours, minutes and seconds lived
print(Name, "has lived for", Hourslived, 'Hours')
print(Name, "has lived for", Minuteslived, 'Minutes')
print(Name, "has lived for", Secondslived, 'Seconds')