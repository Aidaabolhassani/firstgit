x = "hello world"
print(x[2:5])
# starts from 0
x = "hello world"
print(x[5:])

x = "hello world"
print(x[:])
x = "hello world"
print(x[-3:-8])
# use - to strat from the end
# why it is not working

y = "hi my name is Aida"
print(y.upper())
y = "hi my name is Aida"
print(y.lower())
y = "   hi my name is Aida"
print(y.strip())
print(y.replace("a", "c"))
# can we have both strip and replace in one sentence????
# print(y.split("name", "aida"))
# why it is not working
# how we split???we splpt by ","
# y = "   hi my name is Aida"
# print(y.split(", "))
# why not working???
y = 5
x = "apple"
c = str(y) + " " + x
print(c)
# why it is not working?????
x = 1378
y = 22
order = "i am {} years old and i am born at {}"
print(order.format(x, y))
x = 'We are the so-called  \\  "Vikings" from the north.'
print(x)
x = 'We are the so-called \n "Vikings" from the north.'
print(x)
# there is no space between  \ and n
x = 'We are the so-called  \r  "Vikings" from the north.'
print(x)
x = 'We are the so-called  \b  "Vikings" from the north.'
print(x)
x = 'We are the so-called  \f  "Vikings" from the north.'
print(x)
x = 'We are the so-called  \ooo  "Vikings" from the north.'
print(x)
txt = "hello world."
print(txt.capitalize())
x = "hello my name is aida and aida is a student"
y = x.count("aida")
print(y)
# why it is not work ????
