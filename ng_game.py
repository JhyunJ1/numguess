import ng_input
import ng_output

from random import randint


diff_dict = {
        'easy':[20, 10]
        'normal':[50, 15]
        'hard':[100, 10]
    }

def game():
    username = ng_input.username()
    diff = ng_input.diff(username)

    _range = diff_dict[diff][0]
    chance = diff_dict[diff][1]

    answer = randint(1, _range)

    for i in range(_range):
        user_answer = ng_input.user_answer()
        isright = ng_output.isRight(username, answer, user_answer)

        if isright:
            exit(1)
        else:
            if chance == 0:
                GameOver(username)
                exit(1)
    
    
if __name__ == '__maiin__'
    game()
    
