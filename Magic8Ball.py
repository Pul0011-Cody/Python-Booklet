import random
# 8 Ball Answers
answer1=("Absolutely!")
answer2=("No way Pedro!")
answer3=("Go for it tiger.")
# Welcome message
print("Welcome to the Magic 8 Ball game—use it to answer your questions...")
# Asks for the question
question = input("Ask me for any advice and I’ll help you out.  Type in your question and then press Enter for an answer.")
# Prints 4x shaking
print("shaking.... \n" * 4)
choice=random.randint(1,3)
# Chooses a random choice from the answers
if choice == 1:
    answer=answer1
elif choice == 2:
    answer=answer2
else:
    answer=answer3
# Prints the choice
print(answer)
