import random
def get_user_choice():
    user_choice = str(input("alright nice!! k pick your choice. (rock, paper, or scissors):  ")).lower()
    while user_choice not in ['rock','paper','scissors','gun']:
        print("hey uh you cant pick that between the options i given you, if you need a reminder, its rock paper and scissors..")
        user_choice = (input("pick your choice again. (rock, paper, or scissors):  ")).lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def play_game():
    print("yoo uh wanna play a game of rock paper scissors?")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"so uh recap, you chose {user_choice},")
    print(f"and i chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "oh.. we tied"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "aww.. hey atleast you won!"
    elif (user_choice == 'gun' and computer_choice == 'scissors') or \
         (user_choice == 'gun' and computer_choice == 'rock') or \
         (user_choice == 'gun' and computer_choice == 'paper'):
        return "WHY DO YOU HAVE A GUN?!?!?! OKAY FINE YOU WIN JUST DONT SHOOT ME--"
    else:
        return "YAYYY I WON!!!"





if __name__ == "__main__":
    play_game()