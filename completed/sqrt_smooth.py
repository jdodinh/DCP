# A positive integer is called square root smooth if all of its prime factors are strictly less than its square root.
# Including the number 1, there are 29 square root smooth numbers not exceeding 100.

# How many square root smooth numbers are there not exceeding 10000000000?

import numpy as np
import pandas as pd
import math


gen_num = 100000

def find_primes(number):

    primes = list(range(2, number))
    for num in primes:
        i = num**2
        while i < number:
            try:
                primes.remove(i)
                i = i + num
            except:
                i = i + num
                continue
    # print(primes)
    return primes    

def find_smooth_roots(number):
    find_primes(number)


def main():
    gen_lst = list(range(4, gen_num + 1))
    count = 1
    for ing in gen_lst:
        num = ing
        # while num < gen_num:
        up_bd = int(num**0.5)
        if float(up_bd) == num**0.5:
            primes_lt = find_primes(int(num**0.5))
        else:
            primes_lt = find_primes(up_bd+1)
        if len(primes_lt) == 0:
            continue
        for el in primes_lt:
            while num%el==0:
                num = int(num / el)
        if (num in primes_lt) or (num == 1):
            print(ing)
            gen_lst.remove(ing)
            count += 1
            for el in primes_lt:
                num = ing * el
                while num < gen_num:
                    try:
                        print(num)
                        gen_lst.remove(num)
                        num = num * el
                        count += 1
                    except:
                        num = num * el
    print(count)




if __name__=="__main__":
    main()
