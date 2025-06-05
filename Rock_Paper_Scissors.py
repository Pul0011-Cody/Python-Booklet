import random
#What is user's name
name = input("What is your name? ")
#Asks for amount of rounds. Must be between 3 and 10 rounds
rounds = int(input("How many rounds do you want to play? (3-10) "))
while rounds not in range(3, 11):
    print("You need to choose a number between 3 and 10")
    rounds = int(input("How many rounds do you want to play? (3-10) "))
number = 10 - rounds
rounds = number
player_win_count = 0
code_win_count = 0
while rounds in range(10):
    # Makes computer choose rock, paper or scissors
    choice = random.randint(1,3)
    if choice == 1:
        answer = "Paper"
    elif choice == 2:
        answer = "Rock"
    elif choice == 3:
        answer = "Scissors"
    # Asks for users input of rock, paper or scissors
    looper = "Hi"
    player_chose = "A"
    while player_chose not in looper:
        Name_choice = input("Rock, Paper or Scissors? ")
        player_chose = Name_choice.lower()
        looper = player_chose
    
    if answer == "Paper":
        if player_chose == "paper":
            print("I also chose Paper, we tied!")
        elif player_chose == "rock":
            print("I chose Paper!, You Lose")
            code_win_count = code_win_count + 1
        else:
            print("I chose Paper, You won!")
            player_win_count = player_win_count + 1
    if answer == "Rock":
        if player_chose == "paper":
            print("I chose Rock, You won!")
            player_win_count = player_win_count + 1
        elif player_chose == "rock":
            print("I also chose Rock, we tied!")
        else:
            print("I chose Rock!, You Lose")
            code_win_count = code_win_count + 1
    if answer == "Scissors":
        if player_chose == "paper":
            print("I chose Scissors!, You Lose")
            code_win_count = code_win_count + 1
        elif player_chose == "rock":
            print("I chose Scizzors, You won!")
            player_win_count = player_win_count + 1
        else:
            print("I also chose Scissors, we tied!")
    counter = rounds + 1
    rounds = counter
# Prints the answers
print("The score was", code_win_count, "to", player_win_count)
if code_win_count > player_win_count:
    print("I win!")
elif code_win_count < player_win_count:
    print("You won", name + "!")
else:
    print("We tied!")