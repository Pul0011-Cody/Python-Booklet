# Asks if you go to school
do_go_school = input("Do you go to school? (yes/no) ")
# If it is yes then:
is_school = do_go_school.lower() == "yes"
if is_school:
    # Asks for transport methof
   transport_method = input("what transport method do you use to get to school (car/walking) ")
   is_car = transport_method.lower() == "car"
   # if it is car then:
   if is_car:
       print("You should consider walking as it is benefitcial for your health")
       # If it isn't car:
   else:
       distance_to_school = int(input("How far do you travel to get to school? (km) "))
       # If the distance is more or equal to 5:
       if distance_to_school >= 5:
           print("You travel a long distance to get to school")
           # If it is less than 5:
       else:
           print("You don't travel a long distance to get to school")
# If it's no:
else:
    print("Have a nice day")
