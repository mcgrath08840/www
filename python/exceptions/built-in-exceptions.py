# https://docs.python.org/3/library/exceptions.html

# AttributeError   When access property does not have.

class MyClass:
    def __init__(self):
        self.my_property = 5  # Added to fix AttributeError

x = MyClass()
x.my_property     #AttributeError: 'MyClass' object has no attribute 'my_property'



# ImportError
# import my_awesome_module   #  ModuleNotFoundError: No module named 'my_awesome_module'


# KeyError

my_dict = {'x': 5, 'y': 10}
#print(my_dict['z'])    # KeyError: 'z'


# RunTimeError

# TypeError
#int([])    #TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'


# ValueError
# int('a')    # ValueError: invalid literal for int() with base 10: 'a'


# IOError
#open('my_file.txt', 'r')   # FileNotFoundError: [Errno 2] No such file or directory: 'my_file.txt'
