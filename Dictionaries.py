Dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(Dict)

# method

print(Dict['year'])  # accessing value with key
print(Dict.get('test', 'tested'))
print(Dict.keys())  # print all key in dict
Dict[8] = 'nine'
print(Dict)
Dict[8] = 'eight'  # changing value using key
print(Dict)
Dict.update({8:'nine'}) # to change value using key and can add new key and value
Dict.update({9:'nine'})
print(Dict)
Dict.pop(9) # remove dict by value
print(Dict)

Dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in Dict:  # accessing key
  print(x)

for x in Dict.values():  # accessing value. can also access key with .key
  print(x)

for x, y in Dict.items():  # accessing both value and key with .item
  print(x, ":",y)