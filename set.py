#--------diff------

# a = {1,2,3}
# b = {3,4,5}
# print("Union:", a | b)
# print("Intersection:", a & b)
# print("Difference:", a - b)
# print("Symmetric Difference:", a ^ b)

#-------remove elements from 2 set--------
# a = {1,2,3}
# b = {2,3,4}
# print(a & b)

#-----check for subset------
# a = {1,2}
# b = {1,2,3}
# print(a.issubset(b))

#-----element greater then ---------

# s = {10, 20, 30, 5}
# n = 15
# for i in s:
#     if i > n:
#         print(i)

#-------convert back-------
lst = [1,2,2,3,3,4]
lst = list(set(lst))
print(lst)

