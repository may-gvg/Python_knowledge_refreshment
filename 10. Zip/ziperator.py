imiona = ["maciek", "adam", "jarek", "zbyszek", "zbyszek"]
working = ['lakma', 'polifarb', 'firany', "krzesla", "krzesla"]

zipped = zip(imiona, working)

print(zipped)

for i in zipped:
    print(i)

list_zipped = list(zip(imiona, working))
print(f"list zipped: {list_zipped}")

set_zipped = set(zip(imiona, working))
print(f"set zipped: {set_zipped}")

dict_zipped = dict(zip(imiona, working))
print(f"dict zipped: {dict_zipped}")

# Example 2: Different number of iterable elements

numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

result2 = zip(numbersList, str_list, numbers_tuple)

result_list = list(result2)
print(result_list)

result3 = zip(numbersList, str_list, numbers_tuple)

# The * operator can be used in conjunction with zip() to unzip the list.
# zip(*zippedList)
# Example 3: Unzipping the Value Using zip()

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

list1, list2 = zip(*result_list)
print("list1 =", list1)
print('list2 =', list2)
