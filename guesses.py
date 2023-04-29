from random import *



user_name = (input("Enter you Name: "))
user_age = int(input("Enter your age: ")) 

def welcome_message():
    print(f"Welcome {user_name} , lets get started: ")
    


def game_play():
    guess_attempts = 3
    actual_number_r1 = randint(1, 15)
    
    while guess_attempts > 0:
      guess = int(input("Enter your guess between 1-15: "))
      print(actual_number_r1)
      if guess != actual_number_r1:
        print("Incorrect")
        guess_attempts -= 1
        print(f"Remaining attempts: {guess_attempts}")
      else:
        print("You guessed correctly. Move to the next round")
        break
    print("Game Over")



        
def results_list():
    print("list_test")
    
def challenge_game():
    print("challenge_test")
    

