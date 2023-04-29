user_name = (input("Enter you Name: "))
user_age = int(input("Enter your age: ")) 

def welcome_message():
    print(f"Welcome {user_name} ")

def game_play():
    if user_age >= 15:
        print(f"Welcome {user_name} Please Choose a number between 1-15:  ")
    else:
        print(f"Welcome {user_name} ")
        
def results_list():
    print("list_test")
    
def challenge_game():
    print("challenge_test")
    

