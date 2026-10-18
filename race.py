
#import the function from mysort.py
import random, time
from mysort import my_sort 

# messure the seconds to take to order the data
def clock(sort_fn, data):
    start = time.perf_counter()   
    sort_fn(list(data))           
    end = time.perf_counter()     
    return end - start            

# create 20,000 random numbers between 0 and 999,999
nums = [random.randint(0, 999_999) for _ in range(20_000)]

# 3 types of data
shapes = [
    ("shuffled", nums),                          # mixed
    ("already sorted", sorted(nums)),            # ordered
    ("reversed", sorted(nums, reverse=True)),    # backwards
]

#fro each way, run both of them and print the resaults
for name, data in shapes:
    print(f"{name:>14}: mine {clock(my_sort, data):8.3f} s   sorted() {clock(sorted, data):8.3f} s")