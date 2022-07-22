# Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def func1():
  x = "fantastic"
  print("Python is " + x)

func1()

print("Python is " + x)



# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global y
  y = "global"

myfunc()

print("Python is " + y)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
v = "awesome"

def vfunc():
  global v
  v = "changed"

vfunc()

print("Python is " + v)