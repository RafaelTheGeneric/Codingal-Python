import random

lower_bound = 1
upper_bound = 10
max_attempts = 12
secret_number = random.randint(lower_bound, upper_bound)






def get_guess():
    while True:
        guess = int(input("Guess a number between 1 to 10: "))
        if lower_bound <= guess <= upper_bound:
            return guess
        else:
            print("Invalid Input. Please enter a number within the specified range that is 1 to 10.")

        


def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Yoo you got it correct!"
    elif guess < secret_number:
        return "Thats a bit too low.."
    else:
        return "Hey the number might be a bit lower"


def play_game():
    attempts = 0
    won = false

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)
        if result == "Yoo you got it correct!":
            print(f"AYYY GOOD JOBB YOU GOT IT CORRECT, i think the secret number was {secret_number} and the attempts it took you were {attempts}")
            won = True
            break
        else:
            print(f"{result} hey you should try again rq.")
    if not won:
        print(f"heyy sorry but you kinda lost, gl next time tho, also the secret number is {secret_number}")




    if __name__ == "__main__":
        print("YOO WELCOME TO THE NUMBER GUESSING GAME")
        play_game()