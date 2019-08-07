import numpy as np
import pandas as pd
import math

number = 1000000



def find_primes(number):

    primes = []
    for num in range(2, number):
        for i in range(2, num):
            if (num % i == 0):
                break
        else:
            primes.append(num)
    # bool_array = np.ones(number, dtype=bool)
    # bool_array = bool_array.tolist()
    # max = int(number**0.5)

    # for i in range(2, max):
    #     if bool_array[i] is True:
    #         j = i**2
    #         while j < number:
    #             bool_array[j] = False
    #             j = j + i

    # primes = []
    # for i in range(len(bool_array)):
    #     if bool_array[i] is True:
    #         primes.append(i)

    print(primes)
    return primes    

def find_smooth_roots(number):
    find_primes(number)
    for i in range(int(number**0.5), number):
        pass


def main():
    find_primes(number)

if __name__=="__main__":
    main()
