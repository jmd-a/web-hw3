import time
from multiprocessing import Pool, cpu_count

def factorize(*numbers):
    result = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        result.append(factors)
    return result


def factorize_list(numbers):
    with Pool(cpu_count()) as pool:
        return pool.map(factorize, numbers)
    