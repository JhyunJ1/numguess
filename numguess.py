from random import randint
from time import isleep

answer = randint(1, 100)
print(f"answer is {answer}")

username = input("What's your name? ")
user_answer = int(input("Guess number > "))

print(f"{username}'s answer is {user_answer}")

if answer == username:
    print("****************")
    sleep(1)
    print("****************")
    sleep(1)
    print("****************")
    sleep(1)
    print(f"You got it right!! The answer is {answer}")
elif guess > answer:
    print(f"Keep going, man~! That was too high, {username}...")
elif guess < answer:
    print(f"Keep going, man~! That was too low, {username}...")

