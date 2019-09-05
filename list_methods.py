numbers = [2, 3, 4, 6, 3, 4, 6, 1]
# append adds to the end of the list
# numbers.append(20)
# insert allows us to insert new items at the index we set
# second value is the value we wish to add to the list
# numbers.insert(0, 10)
# .remove will remove the value we want which we pass through
# numbers.remove(5)
# to remove all items in the list
# numbers.clear()
# pop remove last item in a list
# numbers.pop()
# print(numbers.index(5))

# print(50 in numbers)
# will return a boolean
# count will give you how many times a value is within a list
# print(numbers.count(5))

# sort will sort our list
# numbers.sort()
# numbers.reverse()
# copies list
# numbers2 = numbers.copy()
# print(numbers)

for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number)
print(numbers)

uniques = list()

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)