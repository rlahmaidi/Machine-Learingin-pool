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
lst = [["a", "b", "c"], ["d","e","f"]]
lst1 = [["first", "second", "third"], "fourth", "fifth", "sixth"]
# for i,(letter, string) in enumerate(zip(lst, lst1)):
#     print(i)
#     print(letter)
#     print(string)
print(lst + lst1)