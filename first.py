from re import X


x = "Python is "
y = "awesome"
z = x + y
print(z)
x = 5
y = "awesome"
z = str(x) + " " + y
print(z)
x = "awesome"


def myfunc(x):
    print("Python is " + x)


myfunc("ssss")


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
y = 5
print((y))
print((x))
