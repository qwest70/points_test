# техника по эквивалентным классам(выбираем 50, 160, 380, 870)
import main

def test_equivalent():
    count = 0
    if main.main_menu(score=50) == 1:
        count += 1
    if main.main_menu(score=160) == 3:
        count += 1
    if main.main_menu(score=380) == 5:
        count += 1
    if main.main_menu(score=870) == 10:
        count += 1
    return count

print(test_equivalent())
if test_equivalent() == 4:
    print('Test equivalent class - Passed')
else:
    print('Test equivalent class - False')
