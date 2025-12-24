
#----------tuple----------
# t = (10, 20, 5, 30)
# print("Max:", max(t))
# print("Min:", min(t))

#----------convert to dict-----
# lst = (("a",1), ("b",2))
# d = dict(lst)
# print(d)

#----------count the occurancy--------
# lst=(1,1,2,2,3,3,4,4,5)
# lst2={}
# for i in lst:
#     if i in lst2:
#         lst2[i]+=1
#     else:
#          lst2[i]=1
# print(lst2)

#---------mutuable--------
# t = (1, 2, [10, 20, 30], 4)
# print(t)
# #t[0] = 100  
# t[2].append(40)
# print(t)

#-------swipe tuple---------
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t1, t2 = t2, t1
print(t1)
print(t2)
