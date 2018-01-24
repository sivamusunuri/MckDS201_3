# Lists
# order is important, change
odds = [5 , 7, 9]
sum(odds)
total = 0
for num in odds:
    total = total + num

total = 0
for i, num in enumerate(odds):
    total = total + (i * num)

#list comprehension -- taking an old list and prducing a new list
squareroots = [n**0.5 for n in odds]
divisibleby5 = [n**91 / 3) for n in range (31) if n % 5 ==0]
list(map(lambda n: n**(1 /3), odds)
list(filter(lambda n: n<5, [3,4,5,6,7]))
from functools import reduce
reduce(lambda total, n: total * n, odds, 1)

#2 - tuple
#order is good, immutable
tup1 = (3,4)

#3 - set
#no order, iterable,unique
s1 = {3,4}

#4 - dict
#no order, iterbale, unique keys
d = {}
for n in range(5):
