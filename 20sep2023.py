import multiprocessing as mp
import time
import numpy as np
from itertools import filterfalse


class PRIME_GEN():
    def __init__(self,to = 100) -> None:
        self.to = to
    
    def prime_gen(self,list):
        max_of_list = max(list)
        min_of_list = min(list)
        
        difference = (max_of_list - min_of_list) // 10
        
        primes = []
        
        for i in range(min_of_list, max_of_list):
            for j in range(2,11):  
                primes.append(i*j)
        
        return primes
            
        
           
    def find_prime(self):
        number_of_cores = mp.cpu_count()
        self.block = self.to//number_of_cores
        
        blocks = []
        for i in range(1,number_of_cores+1):
            temp = []
            for j in range(i , (i*self.block)+1):
                temp.append(j)
            blocks.append(temp)
        
        with mp.Pool(processes=number_of_cores) as pool:
            res = pool.map(self.prime_gen,blocks)
        
        temp = []
        for r in res:
            for l in r:
                temp.append(l)
        
        res = temp
        res = list(set(res))
        del temp
        
        all_ = [i for i in range(1,self.to+1)]
        
        #  copy one list elements to other one 

        all = all_ + res
        all_ = list(set(all))
        return all_
        
prime = PRIME_GEN(1_0_000)
start = time.time()
print(prime.find_prime())
print(time.time() - start)

def prime(x):
    data = []
    for i in range(1,x):
        if i == 1:
            continue
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            data.append(i)
            print(i)
    return data
start = time.time()
print(prime(1_0_000))
print(time.time() - start)
    