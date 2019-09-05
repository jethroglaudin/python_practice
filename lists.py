names = ['John', 'Bob', 'Mary','Sara','Sam']


# this returns a new list when we use square brackets with a colon
names[0] = 'Jon'
print(names[2:])


numbers = [10, 20, 8, 35, 40, 2]

total = numbers[0]
for i in numbers:
    if i > total:
        total = i

print(total)
