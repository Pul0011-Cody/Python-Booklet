# gets the amount spent 
spent = int(input("How much did customer spent? "))
# If the amount spent is between 10 and 20 then they get a $1 voucher
if 10 < spent < 20:
    print("Customer gets a $1 voucher")
# If the amount spent is greater than 20 then they get a $3 voucher
elif spent > 20:
    print("Customer gets a $3 voucher")
# If they spent below $10 they get nothing
else:
    print("No voucher today")