"""

TODO - написать функцию, которая принимает N целых чисел и возвращает список квадратов эих чисел.
Бонусом будет сделать keyword аргумент для выбора степени, в которую будут возводиться числа
TODO - написать функцию, которая на вход принимает список из целых чисел, и возвращает только чётные/нечётные/простые числа (выбор производится передачей дополнительного аргумента)
TODO - создать декоратор для замера времени выполнения функции

"""

def power2(*args, p=2):
    lol = []
    orig = []
    for arg in args:
        lol.append(arg ** p)
        orig.append(arg)
    return lol, orig


def numerik(*args):
    for num in args:
        if num % 2 == 0:
            print(f"{num} : четное число")
        else:
            print(f"{num} : нечетное число")

def numerik2(*args, filters='even'):
    if filters == 'even':
     for num in args:
         if num % 2 == 0:
             print(f"{num} : четное")
    elif filters == 'odd':
        for num in args:
            if num % 2 != 0:
                print(f"{num} : нечетое")




numerik2(2,8,6,5,4,7,8,9,filters='even')

#numerik(2,8,6,5,4,7,8,9,)
num = power2(1,2,3,4, p=6)
print(num)
#num2 = power(5, 15)
#print("num2 = ", num2)