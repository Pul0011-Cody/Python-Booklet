# Bill amount
bill = 100
# Ask how many people
people = int(input("How many people are splitting the bill? "))
# Ask for tip percentage
tip_percent = float(input("How much tip are you going to give? (%) ")) / 100
# Ask how many miles the taxi went
miles_cost = int(input("How many miles did the taxi travel? ")) * 0.45
# Amount of tip they have to pay
tip_amount = bill * tip_percent
# Add tip_amount to bill
tip_cost = bill + tip_amount
# Total cost
total = tip_cost + miles_cost
# Amount per person
per_person = total / people
# prints values
print("The total cost comes to", total, "dollars each person should be paying", per_person, "dollars")
