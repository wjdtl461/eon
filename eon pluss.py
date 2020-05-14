three = 0
five = 0
for i in range(1001):
    if (i % 3 == 0):
        three += i
    if (i % 5 == 0):
        five += i
sum = three + five
print(sum)