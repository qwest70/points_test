def digit(message):
    while True:
        print(message)
        d = input()
        if d.isdigit():
            print()
            break
        print('ОШИБКА: можно вводить только цифры.')
    return int(d)