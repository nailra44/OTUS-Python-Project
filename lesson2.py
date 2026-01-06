"""
1.08.14
interetion, genegetion, comprehentions

"""
from time import time
from functools import wraps, reduce
from operator import mul

def secondary():
    print("secondary")

def add(a, b):
    return a + b

def add2(a, b):
    print("Add", a, b)
    res = a + b
    print("Result: ", res)
    return res
def div(a, b):
    if b ==0:
       return      #pass pass действия которые не выполняем
    return a /b

'''def rain_today():
    res = ... # Элипсис -какой-то объект
    if res.status == "OK":
        return res.data.will_rain #True/False
    print("status not ok")
    return None'''
def demo_lines():
    multiline = """Zero line
    First line
    Second line
    123456789
    """
    print(multiline)


def greed(name):
    print("hello", name)

def greed2(name="World"): # строчка неизменяемая, а список изменяемый
    print("hello", name)

def multiplay_lines(input_line, times, lines=None):
    if lines is None:
        lines = {}
        print('id of dict: ', id(lines))
    for i in range(1, times + 1): # range делает диапазон, если в times пришло например 3, то
        lines[i] = input_line * i
    return lines

#def counter(a):
#    return a

def power(a, p=2):
    return a ** p



def count_values(counter, *args, as_list=False): # * означает что в args может быть передано неограниченное количество аргументов
    print(counter) #
    print(args)
    if as_list:
        #без comprehations
        l = []
        for v in args:
            l.append(counter(v))
        return l

        #return [counter(v) for v in args] # при условии выполняется list comprehantions
        # выводит только список
    return {v: counter(v)  for v in args} # dif comprehantion


def count_values2(counter, *args): # * означает что в args может быть передано неограниченное количество аргументов
    print(counter)
    print(args)
    return {v: counter(v)  for v in args} # dif comprehantion

def my_range(start, end=None, step=1): # end=None - необязательный параметр
    if end is None:
        end = start
        start = 0

    print("entering cycle")
    while  start < end:

        print("yielding", start)
        yield start  # когда python видит в функции yield, то она становится генератором
        start += step # генератор возвращает значения по одному
        print("increased v to", start) #  вывод генератора можно сделать один раз




def main():
    secondary()
    print("Hello main!!!")
    secondary()
    #add2(5, 6)
    #rain_today()
    #div_res = div(10, 2)
    #print("div_res: ",  div_res)
    #div_res = div(10, 0)
    #print("div_res 0: ", div_res)
    #greed("John")
    #greed2()#
    lines = multiplay_lines('foo', 5)
    print('id of return dict: ', id(lines))
    print(lines)
    print(multiplay_lines('spam', 4, lines))
    #print(multiplay_lines('foo', 3))
    #print(multiplay_lines('spam', 4))
    print(multiplay_lines('spam and eggs', 2))
    #count_values(None, 7, 1,2,3,4,5,6) # args тип данных tuple
    res = count_values(power, 7, 1, 2, 3, 4, 5, 6)
    res2 = count_values(power, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, as_list=True)
    print(res)
    print(res2)
    r = range(10)
    print(r)
    print(list(r)) # преобразовать в список
    print(tuple(r)) # преобразовать в tuple
    for i in r:
        print(i, end=" ") # по умолчанию and это перенос строки
    print("be")
    s = {v for v in r}
    s.add(7) # для типа данных set не прибавится, так как 7 уже есть
    #s.add('r')
    print(s) # получается set
    t = (power(v, 3) for v in r)
    print(t) # это генератор
    print('first',next(t))
    print('second',next(t))
    print('tree', next(t))
    for i in t:
       print(i, end=" ")
    #print('after last', next(t))


    range_g = my_range(10)
    print(next(range_g))
    print(next(range_g))
    print(next(range_g))
    print(list(range_g))

#main()
def time_func(func, *args):
    print("timing func", func, "with args", args)
    start_time = time()
    print("time before", time())
    res= func(*args) # * позволяет разпаковать аргументы не как tuple, как позиционные аргументы
    end_time = time()
    print("time after", time())
    print("computed in", end_time - start_time)
    print("returning resusl", res)
    return res

def timing_dec(func): # сделан декоратор
    print("entering decorator with", func)
    @wraps(func)
    def wrapper(*args):
        return time_func(func, *args)

    print("returning decorated")
    return wrapper

def demo_wo_decorators():

    res = time_func(power, 10_000_000_000, 50)
    print ("got res", res )


    res = time_func(power, 10_000_000_000)
    print("got res", res)

    res = time_func(div, 1000, 20)
    print("got res", res)
@timing_dec # декоратор нужен для переопределения функции
def new_power(a, p=2):
    return a ** p

#print('new_power',  new_power.__name__)
#demo_wo_decorators()

#new_power = timing_dec(new_power)
#new_div = timing_dec(div)

#print(new_power(10_034500, 5))
#print(new_div(100, 5))

#
#
#

values = list(range(10))
print("values", values)
powered_gen = map(new_power, values)
print("powered_gen", powered_gen)
print("res", list(powered_gen))

only_even = filter(lambda v: v % 2 == 0, values)
print("only_even", list(only_even))

print(sum(values))
values_to_mul = values[1:]
print("values_to_mul: ",  values_to_mul)
print(sum(values_to_mul))
res = 1
for v in values_to_mul[1:]:
    res *= v
print(res)


res = reduce(mul, values_to_mul, 10)
print("reduce result: ", res)

def accept_kwargs(**kwargs): # это словарь
    print(kwargs)
accept_kwargs(foo="bar", spam="eggs", bax=123) # печать словаря
