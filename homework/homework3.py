"""

TODO - написать функцию, которая принимает N целых чисел и возвращает список квадратов эих чисел.
Бонусом будет сделать keyword аргумент для выбора степени, в которую будут возводиться числа
TODO - написать функцию, которая на вход принимает список из целых чисел, и возвращает только чётные/нечётные/простые числа (выбор производится передачей дополнительного аргумента)
TODO - создать декоратор для замера времени выполнения функции

"""

def power(*args, p=2):
    total = []
    enter_number = []
    for arg in args:
        enter_number.append(arg)
        result = arg * p
        print(f"{arg} = {result}")
        print(f"{result}")

        total.append(result)
    return enter_number, total

num = power(1,2,3,4, p=5)
print(num)
#num2 = power(5, 15)
#print("num2 = ", num2)