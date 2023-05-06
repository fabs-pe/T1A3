from random import *
import csv
import time
from colored import fg, bg, attr


user_name = str(input("Enter your Name: "))
user_age = int(input("Enter your Age: ")) 

def welcome_message():
    print(f'{fg(184)}Welcome {user_name} , lets get started: {attr(0)} ')


if user_age >= 12:
  def game_play(file_name):
      print(f'{fg(1)} Game Rules\n {attr(0)}')
      print(f'{fg(113)}> Enter your name and age.{attr(0)}')
      print(f'{fg(113)}> A random number will be selected for you to guess within a range on you age group.{attr(0)}')
      print(f'{fg(113)}> You will have 3 guesses to get the correct number and move on to the next round.{attr(0)}')
      print(f'{fg(113)}> Each round has a larger range, must win pervious to move on {attr(0)}')
      print(f'{fg(113)}> The number range is based on age, over or under 12\n {attr(0)}')
        
      guess_attempts_r1 = 3
      guess_attempts_r2 = 3
      guess_attempts_r3 = 3
      actual_number_r1 = randint(1, 15)
      actual_number_r2 = randint(1, 30)
      actual_number_r3 = randint(1, 50)
      result_r1 = False
      result_r2 = False
      result_r3 = False
      
      while guess_attempts_r1 > 0:
        guess = int(input(f'{bg(127)}Enter your guess between 1-15:{attr(0)}' ))
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
        guess = int(input(f'{bg(127)}Enter your guess between 1-30:{attr(0)}'))
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
        guess = int(input(f'{bg(127)}Enter your guess between 1-50:{attr(0)}'))
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
        
if user_age < 12:
  def game_play(file_name):
      print(f'{fg(1)} Game Rules\n {attr(0)}')
      print(f'{fg(113)}> Enter your name and age.{attr(0)}')
      print(f'{fg(113)}> A random number will be selected for you to guess within a range on you age group.{attr(0)}')
      print(f'{fg(113)}> You will have 3 guesses to get the correct number and move on to the next round.{attr(0)}')
      print(f'{fg(113)}> Each round has a larger range, must win pervious to move on {attr(0)}')
      print(f'{fg(113)}> The number range is based on age, over or under 12\n {attr(0)}')
        
      guess_attempts_r1 = 3
      guess_attempts_r2 = 3
      guess_attempts_r3 = 3
      actual_number_r1 = randint(1, 10)
      actual_number_r2 = randint(1, 20)
      actual_number_r3 = randint(1, 35)
      result_r1 = False
      result_r2 = False
      result_r3 = False
      
      while guess_attempts_r1 > 0:
        guess = int(input(f'{bg(127)}Enter your guess between 1-10:{attr(0)}' ))
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
        guess = int(input(f'{bg(127)}Enter your guess between 5-20:{attr(0)}'))
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
        guess = int(input(f'{bg(127)}Enter your guess between 10-35:{attr(0)}'))
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
    print(f'{bg(11)}Here are the results{attr(0)}')
    with open(file_name, "r") as results_file:
        reader = csv.reader(results_file)
        for row in reader:
            print(row)
    
def challenge_game(file_name):
    print(f'{bg(11)}Game Rules\n{attr(0)}')
    print(f'{fg(230)}Pick the secret number and beat the secret timer {attr(0)}')
    print(f'{fg(230)}The timer is anywhere between 3-8 seconds {attr(0)}')
    print(f'{fg(230)}Timer is only revealed after selection {attr(0)}')
    print(f'{fg(230)}Be quick, but accurate\n {attr(0)}')
    num_to_guess = [31, 22, 83, 94, 335, 62, 709, 81, 19, 130, 17, 124]
    print(f"From this list pick one number that i have picked")
    print(num_to_guess)
    
    timeout = randint(3,8)  # Timeout after 5 seconds
    start_time = time.time()  # Record the start time
    print(f'{fg(1)} {user_name} you have {timeout} secs to answer {attr(0)}')
    user_guess = int(input("Whats you guess: "))
    random_num = sample(num_to_guess,  1)   # Pick a random item from the list
    
    
    while True:
        if time.time() - start_time > timeout:
            print(f'{bg(1)}Timeout reached, better luck next time!{attr(0)}')
            result = False
            break
        elif user_guess != random_num:
            print(f'{bg(1)}Sorry, thats incorrect, try again next time. The correct number was  {random_num[0]} {attr(0)}')
            result = False
            break
        elif user_guess == random_num:
            print(f'{bg(28)}"Well done, correct guess{attr(0)}')
            result = True
            break


    with open(file_name, "a") as results_file:
        writer = csv.writer(results_file)
        writer.writerow([user_name, user_age, "N/A ", "N/A ", "N/A ", result])
