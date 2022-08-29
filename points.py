import check
import main

points = check.digit('Введите количество баллов цифрами:')
a = main.main_menu(score=points)
print('Ваша скидка составляет ', main.main_menu(points), '%')
