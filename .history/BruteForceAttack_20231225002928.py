import time
import random

#you can define the numbers of character you want to add
character = "0123456789abcdefghijklmnopqrstuvwxyz"
character_list = list(character)
password = input("PLease enter your password ")
start = time.time()
guess = ""
while(guess != password):
    guess = random.choices(character_list, k=len(password))
    print(guess)
    guess = "".join(guess)
    print(guess)
print("your password is  " + guess)
end = time.time()
elapsed_time = end-start
#The time it will take to crack your password
print(elapsed_time)

