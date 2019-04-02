#1
def a():
    return 5
print(a())

#My predicition:
#5

#2
def a():
    return 5
print(a()+a())

#My predicition:
#10

#3
def a():
    return 5
    return 10
print(a())

#My predicition:
#5
#10 <--WRONG! I forgot that "return ends running code within the function!

#Actual output:
#5

#4
def a():
    return 5
    print(10)
print(a())

#My predicition:
#5

#5
def a():
    print(5)
x = a()
print(x)

#My predicition:
#5

#Actual Output:
#5
#None <--I got this part wrong. But when a function doesn't "return" anything, Python will have none as an output.

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

#My predicition:
#3
#5
#8 <---WRONG. Instead of adding strings as integers, Python gives a warning. 

#Actual Output:
#3
#5

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#My predicition:
#25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#My predicition:
#100
#10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#My predicition:
#7
#14
#21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#My predicition:
#8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#My predicition:
#500
#500
#300
#None <---I thought that when a function didn't return anything, it printed none. However, this isn't the case here...I guess because we aren't storing its value in variable.
#500

#Actual output:
#500
#500
#300
#500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#My predicition:
#500
#500
#300
#300 <--- WRONG! only print outputs something, whereas return takes note of a value. 
#300 <--- WRONG! The value of b is still 500 as defined outside of the function.

#Actual output:
#500
#500
#300
#500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#My predicition:
#500
#500
#300
#300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#My predicition:
#1
#3
#2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

#My predicition:
#1
#3
#5
#10




