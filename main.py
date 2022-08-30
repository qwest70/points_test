def main_menu(score):
    if 0 < float(score) <= 100:
        percent = 1
        # print('Ваша скидка составляет ', percent, '%')
    elif 100 < float(score) <= 200:
        percent = 3
        # print('Ваша скидка составляет ', percent, '%')
    elif 200 < float(score) <= 500:
        percent = 5
        # print('Ваша скидка составляет ', percent, '%')
    elif 500 < float(score):
        percent = 10
        # print('Ваша скидка составляет ', percent, '%')
    return percent

