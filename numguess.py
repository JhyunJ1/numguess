from random import randint

answer = randint(1, 100)
print(f"answer is {answer}")

username = input("What's your name? ")
user_answer = int(input("Guess number > "))

print(f"{username}'s answer is {user_answer}")
