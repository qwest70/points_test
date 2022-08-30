# техника по эквивалентным классам(выбираем 50, 160, 380, 870)
import main
file = open('data.md')
dfile = open('discount.md')
def test_equivalent():
    count = 0
    for i in file:
        for j in dfile:
            b = main.main_menu(score=int(i))
            if int(b) == int(j):
                count += 1
                break
    return count

if test_equivalent() == 4:
    print('Name_test - Test equivalent class || Result - Passed')
else:
    print('Name_test - Test equivalent class || Result - False')