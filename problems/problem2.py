def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

sum = 0
inRange = True
index = 1
while inRange:
    fibNum = fib(index)
    index = index + 1
    if fibNum > 4000000:
        inRange = False
        break
    if fibNum % 2 == 0:
        sum += fibNum

print(sum)
