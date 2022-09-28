x = 5
y = "John"
print(x)
print(y)


v = 4       # x is of type int
v = "Sally" # x is now of type str
print(v)

# Type Print
print(type(x))
print(type(y))

a = 4
A = "Sally"
# A will not overwrite a
print(a)
print(A)

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
x1, y1, z1 = "Orange", "Banana", "Cherry"
print(x1)
print(y1)
print(z1)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:
x2 = y2 = z2 = "Orange"
print(x2)
print(y2)
print(z2)


# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
numbers = [11111, 22222, 33333]
x3, y3, z3 = numbers
print(x3)
print(y3)
print(z3)

# Output Variables
x4 = "Python"
y4 = "is"
z4 = "awesome"
print(x4, y4, z4)