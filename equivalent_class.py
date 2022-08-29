# техника по эквивалентным классам(выбираем 50, 160, 380, 870)
import pexpect.popen_spawn
import pexpect
import main


# a = pexpect.popen_spawn.PopenSpawn('python C:/Users/kosov.as/Documents/Обучение/python/points_test/points.py')
# bite = bytes('Введите количество баллов цифрами:', 'utf-8')
# # a.expect(b'Введите количество баллов цифрами:')
# a.expect(bite)
# a.sendline('50')
# b = a.read().decode(encoding='UTF-8')
# print(b == 1)
# if a.read().decode(encoding='UTF-8') != 1:
#     print('123454')

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