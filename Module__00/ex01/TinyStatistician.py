import numpy as np
import sys
from typing import Union, List


class TinyStatistician:
    def __init__(self):
        pass

    def mean(self, x):
        if not isinstance(x, (list, np.ndarray)):
            print('Error: function only accept a list or a numpy array')
            return None
        elif isinstance(x, list) and len(x) == 0:
            return None
        elif isinstance(x, np.ndarray) and x.size == 0:
            return None
        else:
            sum = 0
            for elment in x:
                sum += elment
        return sum / len(x)

    def median(self, x):
        if not isinstance(x, (list, np.ndarray)):
            print('Error: function only accept a list or a numpy array')
            return None
        elif isinstance(x, list) and len(x) == 0:
            return None
        elif isinstance(x, np.ndarray) and x.size == 0:
            return None
        elif len(x) % 2 == 0:
            x = sorted(x)
            return (x[int(len(x) / 2) - 1] + x[int(len(x) / 2)]) / 2
        else:
            x = sorted(x)
            return float(x[int(len(x) / 2)])

    def quartile(self, x):
        if not isinstance(x, (list, np.ndarray)):
            print('Error: function only accept a list or a numpy array')
            return None
        elif isinstance(x, list) and len(x) == 0:
            return None
        elif isinstance(x, np.ndarray) and x.size == 0:
            return None
        sort = sorted(x)
        first = []
        third = []
        if len(sort) % 2 == 0:
            first = sort[:int(len(sort) / 2)]
            third = sort[int(len(sort) / 2):]
        else:
            first = sort[:int(len(sort) / 2) + 1]
            third = sort[int(len(sort) / 2):]
        first_quartile = self.median(first)
        third_quartile = self.median(third)
        return[first_quartile, third_quartile]

    def percentile(self, x, p):
        if not isinstance(x, (list, np.ndarray)):
            print('Error: function only accept a list or a numpy array')
            return None
        elif isinstance(x, list) and len(x) == 0:
            return None
        elif isinstance(x, np.ndarray) and x.size == 0:
            return None
        elif not isinstance(p,(int, float)) or p > 100 or p < 0:
            print("the percentile you want to calculate should be betwen 0 and 100")
        else:
            N = len(x)
            x = sorted(x)
            index = (N - 1) *p / 100
            if index.is_integer():
                return float(x[int(index)])
            floored_index = int(index)
            ceiled_index = int(index) + 1
            floored_value = x[floored_index]
            ceiled_value = x[ceiled_index]
            return float(floored_value + (index - floored_index) *(ceiled_value - floored_value))

    def var(self, x):
        if not isinstance(x, (list, np.ndarray)):
            print('Error: function only accept a list or a numpy array')
            return None
        elif isinstance(x, list) and len(x) == 0:
            return None
        elif isinstance(x, np.ndarray) and x.size == 0:
            return None
        else:
            mean = TinyStatistician().mean(x)
            l = len(x)
            lst = []
            for i in x:
                lst.append((i - mean)**2)
            return float(sum(lst) / (l - 1))

    
if __name__ == "__main__":
    # print("@@@@@@@@@@@@ mean @@@@@@@@@")
    # lst = [1,2,3]
    # array = np.array([1,2,3])
    # print(TinyStatistician().mean(lst))
    # print(TinyStatistician().mean(array))
    # print("@@@@@@@@@@@@@ median @@@@@@")
    # lst = [13, 16, 23, 26, 26, 35, 35, 37]
    # array = np.array([13, 16, 23, 26, 26, 35, 35, 37]) #[1,1,2,4]
    # print(TinyStatistician().median(lst))
    # print(np.median(array))
    # print("@@@@@@@@@@@@@ quaritles @@@@@@")
    # odd =  [1, 42, 300, 10, 59]
    # even = [1, 42, 300, 10, 59,60]
    # odd_array = np.array([1, 42, 300, 10, 59])
    # even_array = np.array([1, 42, 300, 10, 59, 60])
    # print("######odd number of data #####")
    # print(TinyStatistician().quartile(odd))
    # print(TinyStatistician().quartile(odd_array))
    # print("######### even number of data #####")
    # print(TinyStatistician().quartile(even))
    # print(TinyStatistician().quartile(even_array))
    # print("correcto result is",array.quaritles())
    # print("@@@@@@@@@@@@  percentile @@@@@@@@@@@")
    # a =  [1, 42, 300, 10, 59]

    # array = np.array(a)
    # print("numpy: ",np.percentile(array,100))
    # print("mine",TinyStatistician().percentile(array,100))
    # print("@@@@@@@@@@@@@@@@@@ var @@@@@@@@@@@")
    # a =  [1, 42, 300, 10, 59]
    # array = np.array(a)
    # print("the variance of ",a)
    # print("is",TinyStatistician().var(a))
    # print("for numpy aray:",TinyStatistician().var(array))
