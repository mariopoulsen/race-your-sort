#import the function from mysort.py


import random, time 
from mysort import my_sort 

def clock(sort_fn, data):
    start = time.perf_counter()
    sort_fn(list(data))
    end = time.perf_counter()
    return time.perf_counter - start