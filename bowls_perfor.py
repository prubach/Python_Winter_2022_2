from time import time
from bowls import *


def time_func(func, n):
    t0 = time()
    print('Calling: {} for n={}'.format(func, n))
    print('Res={}'.format(func(n)))
    t1 = time()
    elapsed = t1 - t0
    print(f'It took {elapsed}')


#n = 998
n = 100000000
time_func(sum_bowls_loop, n)
time_func(sum_bowls_loop2, n)
#time_func(sum_bowls_recursive, n)
time_func(sum_bowls_seq, n)
