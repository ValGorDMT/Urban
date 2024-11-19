import random

ROCK = 'k'
SCISSIRS = 'n'
PAPER = 'b'

score_win = 0
score_los = 0
score_n = 0

def get_user_choice():
    while True:
        choice = input('Выбирите knb: ').lower()
        if choice in [ROCK, SCISSIRS, PAPER]:
            return choice
        else:
            print("Не так")


def get_bot_choice():
    choices = [ROCK, SCISSIRS, PAPER]
    return random.choice(choices)

def winer(user_choice, bot_choice):
    global score_win, score_los, score_n
    if user_choice == bot_choice:
        score_n += 1
        return 'Ничья'
    elif (
        (user_choice == ROCK and bot_choice == SCISSIRS) or
        (user_choice == SCISSIRS and bot_choice == PAPER) or
        (user_choice == PAPER and bot_choice == ROCK)
        ):
        score_win += 1
        return 'Вы победили'
    else:
        score_los += 1
        return 'Вы проиграли'

def play_game():
    while True:
        user_choice = get_user_choice()
        bot_choice = get_bot_choice()

        print(f'Вы выбрали: {user_choice}')
        print(f'Бот выбрал: {bot_choice}')

        winner = winer(user_choice, bot_choice)
        print(f'Итог: {winner}')

        play_again =input('Еще раз? y/n: ').lower()
        if play_again != 'y':
            break
        
    print(f"Спасибо за игру!")
    print(f'побед: {score_win}')
    print(f'поражений: {score_los}')
    print(f'ничьих: {score_n}')


play_game()