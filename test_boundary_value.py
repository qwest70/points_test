import main
file = open('float_data.md')
dfile = open('float_discount.md')
def test_border():
    count = 0
    for i in file:
        for j in dfile:
            b = main.main_menu(score=float(i))
            if float(b) == float(j):
                count += 1
                break
    return count

if test_border() == 13:
    print('Name_test - Test boundary value || Result - Passed')
else:
    print('Name_test - Test boundary value || Result - False')