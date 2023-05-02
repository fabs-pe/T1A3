from random import *
import csv


user_name = (input("Enter you Name: "))
user_age = int(input("Enter your age: ")) 

def welcome_message():
    print(f"Welcome {user_name} , lets get started: ")
    


def game_play(file_name):
    guess_attempts_r1 = 3
    guess_attempts_r2 = 3
    guess_attempts_r3 = 3
    actual_number_r1 = randint(1, 15)
    actual_number_r2 = randint(1, 30)
    actual_number_r3 = randint(1, 50)
    result_r1 = False
    result_r2 =False
    
    while guess_attempts_r1 > 0:
      guess = int(input("Enter your guess between 1-15: "))
      print(actual_number_r1) #testing only
      if guess != actual_number_r1:
        print("Incorrect")
        guess_attempts_r1 -= 1
        print(f"Remaining attempts: {guess_attempts_r1}")
      else:
        print("You guessed correctly. Move to the next round") 
        result_r1 = True
        break
    
    
    
    while guess_attempts_r2 > 0 and  result_r1:
      guess = int(input("Enter your guess between 1-30: "))
      print(actual_number_r2) #testing only
      if guess != actual_number_r2:
        print("Incorrect")
        guess_attempts_r2 -= 1
        print(f"Remaining attempts: {guess_attempts_r2}")
      else:
        print("You guessed correctly. Move to the next round")
        result_r2 = True
        break
    
    while guess_attempts_r3 > 0 and result_r2:
      guess = int(input("Enter your guess between 1-50: "))
      print(actual_number_r3) #testing only
      if guess != actual_number_r3:
        print("Incorrect")
        guess_attempts_r3 -= 1
        print(f"Remaining attempts: {guess_attempts_r3}")
      else:
        print("You guessed correctly.")
        result_r3 = True
        break
    
    print("Game Over")
    with open(file_name, "a") as results_file:
        writer = csv.writer(results_file)
        writer.writerow([user_name, user_age, result_r1, result_r2, result_r3, "N/A "])
        
def results_list(file_name):
    print("Here are the results")
    with open(file_name, "r") as results_file:
         csv.reader(results_file)
        
    
def challenge_game(file_name):
    num_to_guess = [31, 22, 83, 94, 335, 62, 709, 81, 19, 130, 17, 124]
    print(f"From this list pick one number that i have picked")
    print(num_to_guess)
    
    user_guess = int(input("Whats you guess: "))
    random_num = sample(num_to_guess,  1)   # Pick a random item from the list
    
    if user_guess != random_num:
        print(f"Sorry, thats incorrect, try again next time. The correct number was  {random_num[0]}")
        result = False
    else:
        print(f"Well done, correct guess")
        result = True
    with open(file_name, "a") as results_file:
        writer = csv.writer(results_file)
        writer.writerow([user_name, user_age, "N/A ", "N/A ", "N/A ", result])

    

