mylist = ["apple", "banana", "cherry"]
print(mylist.index('apple'))
print(mylist)
mylist[1:2] = ["blackcurrant", "watermelon"]  # replacing item to list using index
print(mylist)
mylist.insert(0,'instered') # adding item to list without replacing item
print(mylist)
mylist.append('trigger') # adding item to list at end
print(mylist)
take_me = ['i am in']
mylist.extend(take_me) # to append item from another list to current list
print(mylist)
mylist.remove('blackcurrant') # remove item using item name
print(mylist)
mylist.pop(0) # remove item using item index, if item index is not given it will remove last item
print(mylist)
# mylist.clear() clear all item in list

# list comprehension

new_list = [x for x in mylist if "e" in x]
print(new_list)

num  = [x for x in range(20) if x <= 10]
print(num)
even_list = [x for x in num if x % 2 == 0]
print(even_list)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)