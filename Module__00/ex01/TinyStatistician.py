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

    # def percentile(self,x:Union[np.ndarray, list], p:int) -> float:
    #     """ Extracts the percentile p of each features (column of x)
    #     Parameters:
    #         x [np.ndarray]: np.ndarray containing the differents features along axis 1.
    #     Return:
    #         v_percent [np.ndarray]: array (shape[1, m]) containing the p percentile of each features.
    #     """
    #     try:
    #         l_x = len(x)
    #         x_sorted = sorted(x)
    #         idx = int(np.ceil(0.01 * p * l_x)) - 1
    #         percentiles = x_sorted[idx]
    #         return percentiles
    #     except:
    #         return None

    # def percentile(self, x: list, percentile: int) -> float:
    #     x = sorted(x)
    #     m = len(x) - 1
    #     index: float = m * percentile / 100

    #     if index.is_integer():
    #         return x[int(index)]
    #     floored, ceiled = int(index), int(index) + 1
    #     return x[floored] * (ceiled - index) + x[ceiled] * (index - floored)

    def percentile(self,data, rank):
        ''' Calculate percentile by linear interpolation between closest ranks: 
        
        - If the rank is lower or higher than the minimum or maximum possible ranks,
        one of data borders will be returned.
        - If the rank falls between two candidate ranks, linear interpolation is
        used to calculate the result.
        
        More info: http://en.wikipedia.org/wiki/Percentile
        
        Example usage: 
            percentile_linintpol([1,2,3,4,1,5,8], 15)
        
        :param data: List or tuple of numeric values (int, float)
        :param rank: Rank to calculate (values shall be from 0 - 100)
        '''
        
        data = sorted(data)
        dlen = len(data)
        ranks = [ (100.0/dlen)*(d - 0.5) for d in range(1, dlen + 1) ]
        
        # Speed up corner cases
        if rank < ranks[0]:  return data[0]
        if rank > ranks[-1]: return data[-1]
        
        for idx in range(0, dlen - 1):
            rcur, rnext = ranks[idx], ranks[idx + 1]
            if rcur == rank: 
                return data[idx]
            elif rcur < rank and rank < rnext:
                return data[idx] + dlen*(rank-rcur)*(data[idx+1]-data[idx])/100.0

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
    print("@@@@@@@@@@@@  percentile @@@@@@@@@@@")
    a =  [1, 42, 300, 10, 59]

    array = np.array(a)
    # print(np.percentile(array,20))
    print(TinyStatistician().percentile(a,20))
