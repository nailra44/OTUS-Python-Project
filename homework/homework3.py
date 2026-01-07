"""

TODO - написать функцию, которая принимает N целых чисел и возвращает список квадратов эих чисел.
Бонусом будет сделать keyword аргумент для выбора степени, в которую будут возводиться числа
TODO - написать функцию, которая на вход принимает список из целых чисел, и возвращает только чётные/нечётные/простые числа (выбор производится передачей дополнительного аргумента)
TODO - создать декоратор для замера времени выполнения функции

"""
from functools import wraps
from time import time
import time


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
# decorator раз
def decorators(func):
    def wrapper():
        print(f"начало")
        func()
        print("конец")
    return wrapper
@decorators
def hello():
    print("hello чувак")

def counter_dec(func):
    counter = 0
    def rap():
        nonlocal counter
        counter += 1
        print(f"вызов функции {func.__name__} количество вызовов {counter} ")
        return func()
    return rap

@counter_dec
def show_text():
    print("Сколько раз меня вызвали?")

def log_decorators(func):
    def wrapper():
        result = func()
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f" {func.__name__} вызвана в {time.ctime()} \n" )
        print("запись добавлена в лог файл")
        return result
    return wrapper
@log_decorators
def write_sumi():
    print("выполняю суммирование")
    return "Done"

def measure(func):
    @wraps(func) # сохраняет метаданные оригинальной функции
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        stop = time.perf_counter()
        elapsed = stop - start
        print(f"время выполнения функции {func.__name__} равно {elapsed}")
        return result
    return wrapper


@measure
def power3(*args, p=3):
    lol = []
    orig = []
    for arg in args:
        lol.append(arg ** p)
        orig.append(arg)
    return lol, orig

power3(5,8,p=2)




write_sumi()




show_text()
show_text()
show_text()
show_text()
hello()

kol = numerik2(2,8,6,5,4,7,8,9,filters='even')



numerik(2,8,6,5,4,7,8,9)
num = power2(1,2,3,4, p=6)
print(num)
#num2 = power(5, 15)
#print("num2 = ", num2)






