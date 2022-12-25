# While loop

check = 0

while check == 1:
    name = input("L or K: ").lower()
    if name == 'L' or name == 'K':
        check += 1

print("done")

command = ""
car_status = True
while True:

    command = input(">").lower()
    if command == 'start' or command == 'stop' or command == 'quit' or command == 'help':
        if command == 'start':
            if car_status :
                print('car started')
                car_status = False
            else:
                print('car already started')
        elif command == 'stop':
            if car_status :
                print('car already stopped')
            else:
                print('car stopped')
                car_status = True
        elif command == 'help':
            print(''' test''')
        elif command == 'quit':
            print('game exited')
            break
    else:
        print('invalid entry plz enter help for info ')

# For loop

num = [2,5,6,8]
total = 0
for i in num:
    total += i # augmented assignment
# print(total)

# nested loop

for i in range(2):
    for y in range(3):
        print(f'({i},{y})')

numbers = [2,2,2,2,5]
for i in numbers:
    string = ''
    for j in range(i):
        string += ("x")
    print(string)

