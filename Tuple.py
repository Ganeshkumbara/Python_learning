thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
thistuple = list(("apple banana cherry",))
print(thistuple)
thistuple = ("apple", "banana", "cherry")  # when string is separated by comma it will be falls under tuple
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
# since tuple or immutable/ unchangeable, by converting tuple to list we change the value. again reversed back to tuple
list = list(thistuple)
list[0] = 'i can replace u '
thistuple = tuple(list)
print(thistuple)

add_on = ('joining', 'tuple')
thistuple += add_on
print(thistuple)

# unpacking

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# unpacking with * Asterisk

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# Joining two tuple

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
