 
# print("This is the start of the program.")
# time.sleep(5)
# print("This prints five seconds later.")

user_name = (input("Enter you Name: "))
user_age = int(input("Enter your age: ")) 

def guesses():
    if user_age >= 15:
        print(f"Welcome {user_name} Please Choose a number between 1-15:  ")
    else:
        print(f"Welcome {user_name} ")
        
def under_age():
    if user_age <= 15:
        print("Please Choose a number between 1-10:")