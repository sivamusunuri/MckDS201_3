import math

#compute the volume of cube

def volume(side):
    vol = side*side*side
    return vol

def mean(numbers):
    a = sum(numbers) / len(numbers)
    return a

def median(numbers):
    sort = sorted(numbers)
    middle = len(numbers)//2
    if len(numbers) % 2:
        return sort[middle]
    else:
        med = (sort[middle] + sort[middle-1]) / 2
        return med
from collections import defaultdict
def mode(numbers):
    """FInd the most common value in the list
    argument : list of numbers
    return: the mode

    >>>mode([1,2,2,2,3,3,4])
    2
    """
    pass

    number_counts = defaultdict(int)
    for num in ordered_numbers:
    number_counts[num] += 1

    mode = ordered_numbers[0]
    mode_freq = 0
    for num, freq in number_counts.items():
        if freq > mode_freq:
        mode, mode_freq = num, freq
        return (mode)
