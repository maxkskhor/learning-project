from operator import mul
from functools import partial
triple = partial(mul, 3)
triple(7)

list(map(triple, range(1, 10)))
