import time
import random


character = "0123456789abcdefghijklmnopqrstuvwxyz"
character_list = list(character)
password = input("PLease enter your password")
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
print("The time it take to crack your password is " + elapsed_time)
