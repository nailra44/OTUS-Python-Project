class Point:
    IS_2D = True
    all_instances = []
    def __init__(self, x, y):

       """
       можно обращаться к этим методам из вне
       :param x:
       :param y:
       """
       self.x = x
       self.y = y
       self.z = None
       self.all_instances.append(self)

    def __str__(self):
        return f"{self.__class__.__name__} (x = {self.x},y = {self.y})"

    def __repr__(self):
        return str(self)

    def move_up(self):
        self.y += 1

    @classmethod
    def copy(cls, from_point):
        return cls(from_point.x, from_point.y)

    def copy_me(self):
        return self.__class__(self.x, self.y)


class AnotherPoint(Point):
    all_instabses = []


print(Point.all_instances)
p = Point(4, 5)
print(p, "IS 2d", p.IS_2D)
print("point z", p.z)
print(type(p))
print(type(Point))
print(Point.__mro__) # показывает наследование


print()
print()
print("move_upup")
p2 = p
print(p, p2)
p.x += 1
p.y -= 1
print(p, p2)

p3 = p2.copy(p)

print(p2, p3, p3 is p2, p3 is p)

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
print()
print()
print()
print("move_up")
print(p.move_up(), p)


print(isinstance(type, object))

