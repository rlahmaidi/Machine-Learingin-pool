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
            return x[int(len(x) / 2)]
       

if __name__ == "__main__":
    # print("@@@@@@@@@@@@ mean @@@@@@@@@")
    # lst = [1,2,3]
    # array = np.array([1,2,3])
    # print(TinyStatistician().mean(lst))
    # print(TinyStatistician().mean(array))
    print("@@@@@@@@@@@@@ median @@@@@@")
    lst = [1,2,4,1]
    array = np.array([1,2,4,1]) #[1,1,2,4]
    print(TinyStatistician().median(lst))
    print(TinyStatistician().median(array))

