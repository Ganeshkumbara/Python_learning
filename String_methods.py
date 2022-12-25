#  string expandtabs

name = 'ganesh'
txt = ''
for i in name:
    txt += i+'\t'

print(txt.expandtabs(3))

# Find $ index

print(name.find('e'))
print(name.index('e'))

# isdecimal

inp = input(">")
while True:
    if inp.isdigit() == True:
        print('got it')
        break
    else:
        inp = input("enter number >")

# Split
test = "g a n e s h"
name = test.split(' ')
print(name)

# Boolen

print(isinstance(test,str)) # isinstance is use for to check type of value,


