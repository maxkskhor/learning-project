"""
reduce() takes a function and apply cumulatively to all items in an iterable, and generate a single final value
filter(P, S) is equivalent to [x for x in S if P(x)]
map(F, S) is equivalent to [F(x) for x in S]
"""

# ##### reduce #####

from functools import reduce


def my_add(r, s):
    result = r + s
    print(f"{r} + {s} = {result}")
    return result


"""
1st arg: a callable with two arguments
2nd arg: an iterable
3rd arg: initialiser
"""
numbers = [0, 1, 2, 3, 4]

reduce(my_add, numbers)
reduce(my_add, numbers, 100)  # add initialiser

numbers = [3, 5, 2, 4, 7, 1]
# Minimum
x = reduce(lambda r, s: r if r < s else s, numbers)
print(x)
# Maximum
y = reduce(lambda r, s: r if r > s else s, numbers)
print(y)


# ##### map #####

def myfunc(n):
    return len(n)


a = map(myfunc, ('apple', 'banana', 'cherry'))


def myfunc(r, s):
    return r + s


b = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

# ##### filter #####

ages = [5, 12, 17, 18, 24, 32]


def myfunc(i):
    if i < 18:
        return False
    else:
        return True


adults = filter(myfunc, ages)

for x in adults:
    print(x)
