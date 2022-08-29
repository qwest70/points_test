def main_menu(score):
    if 0 < int(score) <= 100:
        percent = 1
        # print('Ваша скидка составляет ', percent, '%')
    elif 100 < int(score) <= 200:
        percent = 3
        # print('Ваша скидка составляет ', percent, '%')
    elif 200 < int(score) <= 500:
        percent = 5
        # print('Ваша скидка составляет ', percent, '%')
    elif 500 < int(score):
        percent = 10
        # print('Ваша скидка составляет ', percent, '%')
    return percent

