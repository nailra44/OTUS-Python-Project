class Point:

    def __init__(self, x, y):
       """
       можно обращаться к этим методам из вне
       :param x:
       :param y:
       """
       self.x = x
       self.y = y
    def __str__(self):
        return f"{self.__class__.__name__} (x = {self.x},y = {self.y})"

p = Point(4, 5)
print(type(p))
print(type(Point))
print(Point.__mro__) # показывает наследование
def my_func():
   pass
print(type(my_func))
print(p.__class__.__name__)
print(type(Point.__init__))
print(lambda x: x)
#p.x = 0
#p.y = 0

f_type = print(type(my_func))
print(f_type )
print(p)

print(isinstance(type, object))

00:24
