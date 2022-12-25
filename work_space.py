# y = "awesome"
# counter = 4
#
# print("Python is " + y)
# for i in range(1,11,2):
#     print(counter*' ',"%"*i)
#     counter -= 1
#

# x = 0
# y = 0
# def myfunc():
#   global x
#   x = x +1
#   y = y+1
#   print("Python is " , x,y)
#
# myfunc()

#
#
# userInput = 5
# lst = [x for x in range(userInput) ]
# print(lst)
#
# user = input(">")
# if type(user) == str:
#     print('its a string')

# listed = ['i','sad']    # strr = str(listed)
# happy = False
# sad = False
# for i in listed:
#     print(i)
#     if i == 'sad':
#         sad = True
#
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
#
# class S1(Person):
#     def printer(self):
#         print(self.firstname)
#
#
# s = S1('r', 't')
# s.printer()

#
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)

# from datetime import date
#
# # import copy
#
# DoB = input('Enter ur DOB(ex:dd/mm/yyyy): ')
# # timez = input('Enter ur time of birth(ex: 12pm): ')
# Day = int(DoB[0:2])
# Month = int(DoB[3:5])
# Imonth = Month - 1
# year = int(DoB[6:10])
#
# today = str(date.today())
# print(today)
# # To change the class type from datetime to other class, copied datetime into list and changed list to string class
#
# # Tday = [copy.copy(today)]
# string = str(Tday)
# print(string)
# year_of_the_day = int(today[:4])
# Month_of_the_day = int(today[5:7])
# date_of_the_day = int(today[8:])
# print('**********', year_of_the_day, Month_of_the_day, date_of_the_day)
#
# No_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print('nor of days in year', sum(No_days))
#
# D_counter = 0
# M_counter = Imonth
# Y_counter = year
#
# year_counter = 0
# Month_counter = 0
# while True:
#     if Y_counter == year_of_the_day:
#         Days_left = No_days[Month_of_the_day - 1] - date_of_the_day
#         D_counter = D_counter + sum(No_days[:Month_of_the_day]) - Days_left
#         Month_counter = Month_counter + Month_of_the_day
#         break
#
# leap_year = 0
#
# for i in range(year, year_of_the_day):
#     if i % 4 == 0:
#         leap_year += 1
#
# print(f'''You lived
# Days: {D_counter + leap_year},
# Month:{Month_counter - 1},
# year: {year_counter}''')


# import platform
#
# x = platform.system()
# print(x)
#
# m = int(input('enter a number'))
#
# def test(e):
#     root = e * e
#     return root
#
# print(test(m))

# from ecommerce.shipping import counter
#
# print(counter(50))
#
# import random
#
#
# class Dice:
#     def Roller(self):
#         p1 = random.randint(1, 5)
#         p2 = random.randint(1, 5)
#         result = (p1, p2)
#         return result
#
#
# roll = Dice
# print(roll.Roller(0))
#
# lst = [1,2]
# print(len(lst))
# # for i in lst[len(lst)-1]:
# #     print(i)
#
#
# dicto = {
#     '1':'one',
#     'dic':{
#         "2":'two'
#     }
# }
#
# dicto['dic']['2'] = 'five'
# print(dicto['dic']['2'])

import json

# json.dumps(dicto)
# with open('test.json', 'w') as m:
#     json.dump(dicto, m)

from qgis.PyQt import QtGui, QtWidgets, uic



