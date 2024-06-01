import random
def number_game(life):
    while True:
        number_to_be_guess = int(input("What's the number you are guessing\n"))
        if number_to_be_guess>number:
            print("Too High")
            life = life - 1
            print(f"You have {life} left")
        elif number_to_be_guess<number:
            print("Too Low")
            life = life - 1
            print(f"You have {life} left")
        elif life == 0:
            print("You lost")
            break
        else:
            print("You guessed the right number")
            break   
print("Welcome to the number guessing game\nI am thinking of a number between 1 and 100")
number = random.randint(1,100)
easy_or_hard = input("Do you want to play easy mode or hard mode\n").lower()
if easy_or_hard == 'easy':
    life = 10
    number_game(life)
else:
    life = 5
    number_game(life)
