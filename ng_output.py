def isRight(username: str, answer: int, user_answer: int):
    if answer == user_answer:
        print(f"Good, job {username}!! Answer is {answer}")
        return 1
    else:
        if answer > user_answer:
            print(f"Do well {username}... Answer is bigger than your answer.")
        else:
            print(f"Do well {username}... Answer is lower than your answer.")
        return 0

def GameOver(username:str,chance:int, user_chance:int):
    if user_chance > chance:
        print(f"Sorry, {username}... You lose")


