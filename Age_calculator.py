from datetime import date
import copy

DoB = input('Enter ur DOB(ex:dd/mm/yyyy): ')
# timez = input('Enter ur time of birth(ex: 12pm): ')
day = int(DoB[0:2])
month = int(DoB[3:5])
year = int(DoB[6:10])
# print(day,month,year)

# Fetching todayz date,month and year using datetime module
today = date.today()

# To change the class type from datetime to other class, copied datetime into list and changed list to string class

Tday = [copy.copy(today)]
string = str(Tday)
year_of_the_day = int(string[15:19])
Month_of_the_day = int(string[21:23])
date_of_the_day = int(string[25:27])
print('**********',year_of_the_day,Month_of_the_day,date_of_the_day)
No_of_DM = [0,31,28,31,30,31,30,31,31,30,31,30,31]


# To find number of days $ month left out in born year with respect to DOB

# Days
D_in_MB = No_of_DM[month] # No of days in month with respect to DOB
index = month
LOD_in_M = D_in_MB-day  # No of days left out in the month with respect to DOB
RE_D_in_Y = sum(No_of_DM[index:]) # remaining days in the year from the Month of DOB
N_of_D_LE_Y = RE_D_in_Y - LOD_in_M # number of days left out in the year, from the day of birth
# print('Days left in the year DOB',N_of_D_LE_Y)

#Months

total_month_year = 12
N_of_M_LE_Y = total_month_year - month # number of month left out in the year of birth
print('Month left in the year DOB',N_of_M_LE_Y)

# To find number of days $ month completed in the present year

# Day

DA_CO_DOB = sum(No_of_DM[:Month_of_the_day])
ND_CM  = DA_CO_DOB + date_of_the_day # number of days completed in year with respect to current day
# print(ND_CM)

#Month

CE_M_in_Y = Month_of_the_day
print('number of Months completed in this year',CE_M_in_Y)

# Final step printing total No of days, month and year from the day of birth till today

# Years

total_years = year_of_the_day-year

if month < Month_of_the_day:
    LM = month
    GM = Month_of_the_day
else:
    LM = Month_of_the_day
    GM = month

print('gm',GM,'lm',LM)

current_Month = GM - LM

print(GM,LM)
print('Your Age: ',total_years,'Years',current_Month,'month',date_of_the_day-day,'days')
RE_and_CE_Month = N_of_M_LE_Y+CE_M_in_Y
# print(RE_and_CE_Month)

Full_month_year = total_years - 1
Months_of_full_years = Full_month_year * 12
total_month = Months_of_full_years + RE_and_CE_Month # Total months

# extra days by leap year
counter = 0
for i in range(year,year_of_the_day):
    if i % 4 == 0:
        counter= counter+1

print(counter)

total_day = ND_CM+N_of_D_LE_Y+(Full_month_year*365)+counter
print('you lived:)')
print(total_years,'  :Years')
print(total_month,' :Month')
print(total_day,':Days')



