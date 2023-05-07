from guesses import welcome_message, game_play, results_list, challenge_game


print("Welcome to Guess The Number \n")

welcome_message() 

file_name = "results.csv"

try:
    results_file = open(file_name, "r") # Opens file as readable if it exixts
    results_file.close()
except FileNotFoundError as e:
    results_file = open(file_name, "w") # If file is not found create the file as writable
    results_file.write("Name, Age, Rd 1 Win, Rd 2 Win, Rd 3 Win, Challenge Win\n") # Create the coloums in the file
    results_file.close()
 
def menu():
    print("1. Enter 1 to start the game")
    print("2. Enter 2 to view your results")
    print("3. Enter 3 for the daily challenge")
    print("4. Enter 4 to exit")
    choice = input("Enter your selection: ") 
    return choice


user_choice = ""

while user_choice != "4": # The program will exit
    user_choice = menu()

    if (user_choice == "1"):
        game_play(file_name)
    elif (user_choice == "2"):
       results_list(file_name)
    elif (user_choice == "3"):
        challenge_game(file_name)
    elif (user_choice == "4"):
        continue
    else:
        print("Invalid Input")

    input("Press Enter to continue....")


print("Thank you for playing, see you soon!") # Exit Message
