# Country data
countryPop = { "Japan":"127000000", "Germany":"81000000", "Iran":"77000000","UK":"64000000","Canada":"33000000","Australia":"23000000","USA":"317000000","Bulgaria":"7000000","Sweden":"10000000"}
# Gets the first country and it repeats untill something from the list is typed
first = input("What is your first country? ")
while first not in countryPop:
    print("Sorry can't find that information. Please try again")
    first = input("What is your first country? ")
# Gets the second country and it repeats untill something from the list is typed
second = input("What is your second country? ")
while second not in countryPop:
    print("Sorry can't find that information. Please try again")
    second = input("What is your second country? ")
# Gets the first country's value
first_value = int(countryPop[first])
# Gets the second country's value
second_value = int(countryPop[second])
# Adds the 2 values together
total_pop = first_value + second_value
# Prints the total value
print("The total population of", first, "and", second, "is", total_pop)
    