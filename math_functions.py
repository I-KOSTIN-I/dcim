def name_function(func):
    def status(*args):
        """
        Выводит имя вызываемой функции
        """
        print(f"Function {str(func.__name__)} was called.")
        return func(*args)

    return status


"""Коэфициент на которое будет умножен последний переданный в функцию аргумент"""
cof_of_change = 5
"""Определите порядок в котором произведутся математические операции: "straight" - прямой, "reverse" - обратный"""
order_argument = 'straight'


def change_last_argument(func):
    def change(*args):
        """
        Умножает последний переданный в функцию аргумент.
        """
        numbers = []
        for i in args:
            numbers.append(i)
        numbers[3] = numbers[3] * cof_of_change
        #print('Переданные аргументы', *args)
        #print(f'Аргумент d умножен на {cof_of_change} | {numbers}')
        return func(*numbers)

    return change


@change_last_argument
@name_function
def first_function(*args):
    numbers = []
    for i in args:
        numbers.append(i)

    if order_argument == 'straight':
        a = numbers[3]
        b = numbers[2]
        c = numbers[1]
        d = numbers[0]
    else:
        a = numbers[0]
        b = numbers[1]
        c = numbers[2]
        d = numbers[3]

    return 0 + ((a - b) + c) + d


@change_last_argument
@name_function
def second_function(*args):
    numbers = []
    for i in args:
        numbers.append(i)

    if order_argument == 'straight':
        a = numbers[3]
        b = numbers[2]
        c = numbers[1]
        d = numbers[0]
    else:
        a = numbers[0]
        b = numbers[1]
        c = numbers[2]
        d = numbers[3]

    return 67 - ((a + b) - c) - d


@change_last_argument
@name_function
def third_function(*args):
    numbers = []
    for i in args:
        numbers.append(i)

    if order_argument == 'straight':
        a = numbers[3]
        b = numbers[2]
        c = numbers[1]
        d = numbers[0]
    else:
        a = numbers[0]
        b = numbers[1]
        c = numbers[2]
        d = numbers[3]

    return 10 * ((a + b) * c) * d


@change_last_argument
@name_function
def fourth_function(*args):
    numbers = []
    for i in args:
        numbers.append(i)

    if order_argument == 'straight':
        a = numbers[3]
        b = numbers[2]
        c = numbers[1]
        d = numbers[0]
    else:
        a = numbers[0]
        b = numbers[1]
        c = numbers[2]
        d = numbers[3]

    if a == 0:
        return print('a=0. Не дели на 0, брат!')
    if b == 0:
        return print('b=0. Не дели на 0, брат!')
    if c == 0:
        return print('c=0. Не дели на 0, брат!')
    if d == 0:
        return print('d=0. Не дели на 0, брат!')

    return 1000 / ((a + b) / c) / d


#print(first_function(5, 4, 3, 2, 9, 10))
#print(second_function(6, 1, 2, 4))
#print(third_function(5, 7, 9, 17, 12))
#print(fourth_function(5, 7, 9, 67, 12))

