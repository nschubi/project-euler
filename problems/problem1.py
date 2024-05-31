# Find all numbers who can be divided by 3 or 5 between 1 and 1000
numbers = []

for i in range(1,1000):
    if i % 3 == 0:
        numbers.append(i)
    elif i % 5 == 0:
        numbers.append(i)

sum = 0
for i in numbers:
    sum += i

print(sum)


