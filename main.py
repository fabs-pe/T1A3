from guesses import welcome_message, game_play, results_list, challenge_game


print("Welcome to Guess The Number \n")

welcome_message()

print("Game Rules")
print("> Enter your name and age.")
print("> A random number will be selected for you to guess within a range on you age group.")
print("> You will have 3 guesses to get the correct number and move on to the next round.")
print("> Each round has a larger range, must win pervious to move on")
print("> Almost forgot!! There is a timer. \n")


def menu():
    print("1. Enter 1 to start the game")
    print("2. Enter 2 to view your results")
    print("3. Enter 3 for the daily challenge")
    print("4. Enter 4 to exit")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""

while user_choice != "4":
    user_choice = menu()

    if (user_choice == "1"):
        game_play()
    elif (user_choice == "2"):
       results_list()
    elif (user_choice == "3"):
        challenge_game()
    elif (user_choice == "4"):
        continue
    else:
        print("Invalid Input")

    input("Press Enter to continue....")


print("Thank you for playing, see you soon!")


# under_age()
# countdown(0,0,6)