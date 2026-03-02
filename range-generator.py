# Replicate Range function using Generator. author: Jothiswarooban k 
def myrange(start,end=None,step = 1):

    if step == 0:
        raise ValueError("step count should be non zero")
    
    if end == None:
        start_value = 0
        end_value = start
    else:
        start_value =start
        end_value = end
    
    if step > 0:
        if start_value > end_value:
            return
        while start_value < end_value:
            yield start_value
            start_value += step
    if step < 0:
        if start_value < end_value:
            return
        while start_value > end_value:
            yield start_value
            start_value += step
            
from itertools import zip_longest

f = myrange(10)
for i in zip_longest(f, range(10)):
    print(i)

f = myrange(0,10)
for i in zip_longest(f, range(0,10)):
    print(i)

f = myrange(10,0)
for i in zip_longest(f, range(10,0)):
    print(i)

f = myrange(0,10,2)
for i in zip_longest(f, range(0,10,2)):
    print(i)

f = myrange(0,10,-2)
for i in zip_longest(f, range(0,10,-2)):
    print(i)

f = myrange(10,0,2)
for i in zip_longest(f, range(10,0,2)):
    print(i)

f = myrange(10,0,-2)
for i in zip_longest(f, range(10,0,-2)):
    print(i)