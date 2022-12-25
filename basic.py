print('check check')

name = ('<>/' * 10)
print(name[0:3])

# interpreter interprets line by line of code
check = 25
checkz = str(35)
print(check)
print(type(check))
print("  ")

# variables

x, y, z = "test", 'check', 3
print(x, y, z, '\n')

x = z = y = "test" \
            "t ext"
print(x)

####  Built-in data type

# Number

'''int number are whole number, without any decimal, it can be either + or -'''
X = 5
Y = -5

'''Float is a number, containing one or two decimal numbers'''
Xy = 5.0
Yx = -5.0

print(int(Yx))

'''complex numeric include j in value'''

com = 123232314j

# String

string = 'i am a string'
strings = '''i am a multi
                string'''

# string slicing

print(string[0], '&', string[-4:], ',printing 1st and lasst 4letter of the variable ',
      '\n')  # \n used for print empty line

a = 'Testing, testing'.lower()
print(a)

a = a[:].upper().split(',')
print(a, '\n')

# exercise: patient details

name = 'Elon'
age = str(51)
disease = 'admitted on 16/10/2022 Suffering from Space travel'

print('Name       : ' + name)
print('Age        : ' + age)
print('disease    : ' + disease)
print("  ")

# receiving input from end user ****
# name = input('Enter ur name: ')
# interest = input('your interested in? ')
# print(name, 'thanks for choosing', interest, 'will provide our best for YOU ^^')

counter = 0

for i in range(2000, 2022):
    if i % 4 == 0:
        # print(i)
        counter = counter + 1  # augmented assignment operator
        # print(counter)

# Weight_lbs = int(input('weight (lbs): '))
# kilogram = Weight_lbs/2.205
# print(" Kilogram = %1.2f " % kilogram) # *************

num = 2.353536353
print(round(num, 3))

# string index accessing

text = 'copy the text'
copied = text[:]
print(copied)

# formatted string

name = 'gusto'
age = 35
print(f'Hi {name} u look pretty young even at {age}')

# string methods (Functions)

text = 'copy the text'
text = text + ' formate'
print(text)
print(len(text))
print(text.find('copy'))  # print the index for the text entered
print(text.replace('copy', 'topy'))  # replace the text in the string
print(text.title())  #
if 'copy' in text:
    print('file is there')

# Arthimetic operation

x = 10
x += 3  # augmented assignment Operator
print(x)
y = 10
y *= 2
print(y,'*************')

# operator precedence order
# exponentiation 2 ** 3
# Multiplication or division
# addition or subtraction

z = 10 + 3 * 2 ** 2
print(z)
z = (10 + 3) * 2 ** 2  # parenthesis takes prioritize over operator precedence
print(z)

# math functions

xa = abs(-2.9)
multi = xa - 2
print(round(multi))

import math

print(min(20, 10))  # min and max to find lowest and highest number
print('power', pow(2, 2))
L = 1.1  # round the integer upwards to the numberF
H = 1.9  # round the integer downwards to the number
print(math.ceil(L))  # round the integer upwards to the number
print(math.floor(H))  # round the integer downwards to the number

# if statement
price = 100000
good_credit = False

if good_credit:
    down_payment = round(0.1 * price)
else:
    down_payment = round(0.2 * price)
print(f'pay ${down_payment} down payment')

# if statement with logical operators and conditions
# AND : both logical should be

re_height = 6
re_weight = 70
weight = 70
height = 6

if weight >= re_weight and height >= re_height:
    print("Hurry u r selected")

# if, elif, else example

name = ("ga")
if len(name) < 3:
    print('name must be more then 3 characters')
elif len(name) > 10:
    print('name must be maximum of 10 characters')
else:
    print('loverly name', name[:])

# List

list = [1, 2, 3, 4, 5, 4]
list[5] = 6
largest = 0
for i in list:
    if i > largest:
        largest = i
print(f'largest number in list: {largest}')

# 2D list

matrix = [
    [2, 3, 4],
    [7, 8, 9],
    [4, 5, 6]
]
print(matrix)
print(matrix[0][0], '777777777')

for raw in matrix:
    for item in raw:
        pass
        # print(item)

# list methods or functions

number = [5, 2, 4, 6, 7]
number.append(20)
print(number)
number.insert(0, 20)
print(number)
number.remove(5)
print(number)
print(type(number.count(20)))
number.sort()
print(number)
number.reverse()
print(number)
number.clear()
print(number)

num = [1, 5, 10, 1, 5, 6, 8, 10]
for i in num:
    counter = num.count(i)
    if counter > 1:
        num.remove(i)
    else:
        pass

numbers = [1, 5, 10, 1, 5, 6, 8, 10]
uniques = []
for number in numbers:
    if number in uniques:
        continue
    uniques.append(number)
print(uniques, '#############')

# tuple  tuple are unmountable we cant chang or modify the tupe

tuple = (1, 2, 3)
print(type(tuple), tuple)

# unpacking

co_ordinats = [1, 2, 3]
x, y, z = co_ordinats
print('unpacking list', x, y, z)

# Dictionary

book = {'names': 'gana', 'age': '23', 'DoB': '23', 5: "check"}
print(book['names'], book['age'])

# To print Alphabet number

# user = str(input('Num > '))
output = ''
dict = {'1': 'one', '2': 'two'}
# for i in user:
#     output += dict.get(i,'!')+ " "
#     pass

print(output)

# nested if statement

x = 15

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


# Function


def calling_out(name, last_name):  # given 2 parameters t0 functions
    print(f'hello {name} {last_name}')


print("testing")
calling_out(last_name='maddy', name='brock')  # keyword arguments
calling_out("geddy", 'greek')  # argument  for function


# return Function

def factorial(number):
    store = 1  # anything multiply by 0 will 0
    for i in range(1, number + 1):
        store *= i
    return f"factorial of {number} ", store


save = str(factorial(5))
print(save)


# exception error

# try:
#     inputs = int(input("age:"))
#     risk = 20000/inputs
#     print(inputs)
# except ZeroDivisionError:
#     print("age can't be zero")
# except ValueError:
#     print('invalid Error')
#

# Classes

class Fruit:  # Class is blueprint of work
    def __init__(self, name, colour, tasty):  # parameters will in given while assign class to variable
        self.names = name
        self.colour = colour
        self.taste = tasty
        self.exp_date = '24'

    def details(self):
        print("The colour of " + self.names + ' is ' + self.colour)
        print(self.names + ' expires on ' + self.exp_date)


apple = Fruit('apple', 'red', 'yummy')  # when u assign variable to class, it will become object
print(apple.taste)  # can call the attribute, by object.attribute
banana = Fruit('bana', 'yellow', 'huu')  # apple and banana are two instance of class Fruit
apple.details()  # calling out method of the class

'''Methods:-
            Functions inside a class
    Attributes:-
            variables with the self.prefix
    Objects:-
            variables assigned to classes
    instance:-
            assigning class to multiple variable with varying of values'''


class Person:
    def __init__(self, peru):
        self.name = peru

    def NamePrinter(self):
        print('Hello ' + self.name)


zack = Person("zack")  # first instance
zack.NamePrinter()
mark = Person("mark")
mark.NamePrinter()


# Inheritance

class Mammals:
    def walk(self):
        printr = 'walkable'
        return printr


class Dog(Mammals):
    pass


dog = Dog()
print(dog.walk())

# random

import random


class Dice:
    def roller(self):
        p1 = random.randint(1, 5)
        p2 = random.randint(1, 5)
        result = (p1, p2)
        return result


roll = Dice
print(roll.roller())
