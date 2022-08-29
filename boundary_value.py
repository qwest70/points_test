# техника анализа граничных значений(выбираем 100, 101, 200, 201, 500, 501)
import main

def test_border():
    count = 0
    if main.main_menu(score=100) == 1:
        count += 1
    if main.main_menu(score=101) == 3:
        count += 1
    if main.main_menu(score=200) == 3:
        count += 1
    if main.main_menu(score=201) == 5:
        count += 1
    if main.main_menu(score=500) == 5:
        count += 1
    if main.main_menu(score=501) == 10:
        count += 1
    return count


if test_border() == 6:
    print('Test boundary value - Passed')
else:
    print('Test boundary value - False')