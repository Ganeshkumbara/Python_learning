from datetime import date
import copy

DoB = input('Enter ur DOB(ex:dd/mm/yyyy): ')
# timez = input('Enter ur time of birth(ex: 12pm): ')
Day = int(DoB[0:2])
Month = int(DoB[3:5])
Imonth = Month-1
year = int(DoB[6:10])

today = str(date.today())
print(today)
# To change the class type from datetime to other class, copied datetime into list and changed list to string class

# Tday = [copy.copy(today)]
# string = str(Tday)
# print(string)
year_of_the_day = int(today[:4])
Month_of_the_day = int(today[5:7])
date_of_the_day = int(today[8:])
# print('**********',year_of_the_day,Month_of_the_day,date_of_the_day)



No_days = [31,28,31,30,31,30,31,31,30,31,30,31]
# print('nor of days in year',sum(No_days))

D_counter = 0
M_counter = Imonth
Y_counter = year

year_counter = 0
Month_counter = 0
Days_counter = 0
while True:
  if D_counter == 0 and M_counter == Imonth:
    D_counter += No_days[M_counter]-Day
    M_counter += 1
    Month_counter +=1
    print('***',M_counter,D_counter,Month_counter-1)
  elif M_counter != 12 and Y_counter != year_of_the_day:
    D_counter += No_days[M_counter]
    M_counter +=1
    Month_counter += 1
    print('*****',M_counter,D_counter,Month_counter-1)
  elif M_counter == 12 and Y_counter != year_of_the_day:
    M_counter = 0
    Y_counter += 1
    year_counter +=1
    print(M_counter,Y_counter,Month_counter-1)
  elif Y_counter == year_of_the_day:
    Days_left = No_days[Month_of_the_day-1] - date_of_the_day
    D_counter = D_counter+sum(No_days[:Month_of_the_day])
    Month_counter = Month_counter+Month_of_the_day
    print('working')
    break
    #D_counter = D_counter + sum(No_days[:10])-22
    #Month_counter = Month_counter + 10
    #  break

leap_year = 0

for i in range(year,year_of_the_day):
  if i % 4 == 0:
    leap_year += 1

print(f'''You lived
Days: {D_counter+leap_year}, 
Month:{Month_counter-2},
year: {year_counter}''')



