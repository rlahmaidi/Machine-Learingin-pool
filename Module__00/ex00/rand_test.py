## a way to initialize a list
# lst = []
# for i in range(4):
#     lst.append([9] * 3)

# print(lst)

## compare to tuples
# t = (1,2)
# t1 = (1,1)
# if t == t1:
#     print("yes")
# else:
#     print("no")

### testing zip and enumurate
# lst = [["a", "b", "c"], ["d","e","f"]]
# lst1 = [["first", "second", "third"], "fourth", "fifth", "sixth"]
# # for i,(letter, string) in enumerate(zip(lst, lst1)):
# #     print(i)
# #     print(letter)
# #     print(string)
# print(lst + lst1)

## list multiplied by a scalar
# lst = [[1,2],[3,4]]
# tmp = [second * 2 for first in lst for second in first]
# print(tmp)

## zip and enumerate
# lst = [[1,2,3],[4,5,6], [7,8,9]]
# for z in zip(lst[i] for i in range(len(lst))):
#     print(z)
# tmp = [lst[i] for i in range(len(lst))]
# print(tmp)
# lst = [1,2,3,4,5,6,7,8,9]
# lst1 = [1,2,3,4,5,6,7,8,9]
# lst2 = [[1,2,3],[4,5,6],[7,8,9]]
# for z in zip(lst, lst1):
#     print(z)

# my own solution to transpose
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]
#           ]
# lst = []
# for i in range(len(matrix)):
#     tmp_lst = []
#     for line in matrix:
#         tmp_lst.append(line[i])
#     lst.append(tmp_lst)
# print(lst)

lst = [2,1,1]
lst2 = [2,3,4]
s = 0
for i in range(len(lst)):
    s += lst[i] * lst2[i]
print(s)

print(sum([lst[i] * lst2[i] for i in range(len(lst))]))