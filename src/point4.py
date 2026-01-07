def my_func():
    """
    My demo func
    :return:
    """
    pass
my_func.extra_value = 123
print(my_func.__name__, my_func.__doc__, my_func.extra_value)

def _get_conn(*args):
    print("creating conn", args)
    return...

def get_connection(*args):
    if get_connection._conn is None:
        get_connection._conn = _get_conn(*args)
    return get_connection._conn

get_connection._conn = None
conn2 = get_connection([],{},set())
conn1 = get_connection(1,2,4)

print("conn1 is conn2", conn1 is conn2)