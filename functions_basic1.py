#1 
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# will print 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#error number of days not defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# will print 5 after 1st return code end

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# will print 5 its told to return 5 code ends

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# function is 5 so code ends x is none value of function has already been printed indentation shows its a new block of code

#6
def add(b,c):
    print(b+c)
print(add(1,2) + addcopy(2,3))
# will print 3 and for add(b,c) and error because addcopy is not defined

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#will print 25 because str() turns int into strings so its will combine 2 and 5

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# will print 100 and 10 because 100 is < than 10 becasue of indentation still same block of code

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# will print 7 and 14 and 21 because first print 2 < 3 and second print 5 > 2 and the third 2 < 3 so its 7 and 5 > 3 so returns 14 and adds both 7 + 14 = 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# will print 8 after first return code ends

#11
b = 500
print(b)
def foobar():
    b ="keyword operator from-rainbow">= 300
    print(b)
print(b)
foobar()
print(b)
# will print 500 and 500 and error because >= does not work with a string and an int 

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#will print 500 and 500 and 300 and 500 line 91 500 line 96 500 line 94 , line 97 300 line 98 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# will print 500 and 500 and 300 and 300 line 103 500 line 108 500 line 109, 106 300 line 110, 109 300

#14
def foo():
    print(1)
    barcopy()
    print(2)
def bar():
    print(3)
foo()
# will print 1 error barcopy not defined 

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#will print 1 and 3 and 5 and 10  stores the two functions not called yet foo() bar() then prints 1 after x = bar() for function bar() print 3 then stores return 5 in x and prints it in line 127 then stores return 10 and prints it with line 133