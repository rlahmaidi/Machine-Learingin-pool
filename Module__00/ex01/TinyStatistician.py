import numpy as np
import sys


class TinyStatistician:
    def __init__(self):
        pass
    
    def mean(self,x):
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

    def median(self,x): 
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
        
    def quartile(self,x):
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
            print("the sort is", sort)
            first = sort[:int(len(sort) / 2)]
            third = sort[int(len(sort) / 2) - 1:]
            print("the len(sort) is ", len(sort))
            print("the first data is ", first)
            print("the third data is ", third)
        else:
            print("the sort is", sort)
            first = sort[:int(len(sort) / 2)]
            third = sort[int(len(sort) / 2) - 1:]
            # first = sort[:int(len(sort) / 2)]
            # third = sort[int(len(sort) / 2) + 1:]
            print("the len(sort) is ", len(sort))
            print("the first data is ", first)
            print("the third data is ", third)
        first_quartile = self.median(first) 
        third_quartile = self.median(third)
        return[first_quartile, third_quartile]


        # if len(sort) % 4 != 0:
        #     first_quartile = sort[int(len(sort) / 4) - 1]
        # else:
        #     first_quartile = (sort[int(len(sort) / 4) - 1] + sort[int(len(sort) / 4)]) / 2
        # if len(sort) * 3 % 4 == 0:
        #     third_quartile = sort[l - 1]
        # else:
        #     print("number of element is ", len(sort))
        #     # print("3/4 of it is ", len(sort) * 3 / 4)
        #     # print("third quartile ", sort[int(l) -1], sort[int(l)])
        #     # print("their indices are:", int(l) - 1, int(l))
        #     third_quartile = (sort[int(l)- 1] + sort[int(l)]) / 2
        return [first_quartile, third_quartile]
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
    print("@@@@@@@@@@@@@ quaritles @@@@@@")
    a = [6, 1, 9, 4]


    lst = [7, 2, 9, 1, 5, 6]
    array = np.array([13, 16, 23, 26, 26, 35, 35, 37])  # 9 *3 /4 27 /4
    # print(TinyStatistician().quartile(a))
    # print(TinyStatistician().quartile(array))
    # print("correcto result is",array.quaritles)
    print(TinyStatistician().median(a))
    print(np.median(np.array(a)))
