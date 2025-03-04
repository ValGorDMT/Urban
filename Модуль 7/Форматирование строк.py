
def print_team_num(team1_num, team2_num):
    print('В команде "Мастера кода" участников: %d ! ' % team1_num)
    print('В команде "Волшебники Данных" участников: %d ! ' % team2_num)
    print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))

def print_via_format(score_2, team1_time):
    print('Команда Волшебники данных решила задач: {} !'.format(score_2))
    print('Волшебники данных решили задачи за {:.2f} с !'.format(team1_time))

def fprint(score_1, score_2, challenge_result, tasks_total, time_avg):
    print(f'Команды решили {score_1} и {score_2} задач.')
    print(f'Результат битвы: {challenge_result}!')
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

def main():
    team1_num = 6
    team2_num = 7
    score_1 = 40
    score_2 = 42
    team1_time = 1552.512
    team2_time = 2153.31451
    tasks_total = 82
    time_avg = 45.2

    print_team_num(team1_num, team2_num)
    print_via_format(score_2, team1_time)

    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        challenge_result = 'Победа команды Мастера кода'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        challenge_result = 'Победа команды Волшебники Данных'
    else:
        challenge_result = 'Ничья'

    fprint(score_1, score_2, challenge_result, tasks_total, time_avg)

if __name__ == '__main__':
    main()