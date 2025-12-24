#-------------List duplicate----------

# list1=[1,1,2,2,3,3,4,5]
# newList=[]
# for i in list1:
#     if i not in newList:
#         newList.append(i)
# print(newList)

#-------------list comprehension--------
# list1=[1,2,3,4,5,6,7,8]
# newList=[]

# for i in list1:
#     if i%2==0:
#         newList.append(i)
# print(newList)

#-----------second largest element in list----------
# list1=[1,2,3,4,5,6,7,8]
# largest=max(list1)
# list1.remove(largest)
# secondlargest=max(list1)
# print("the second largest element is ",secondlargest)


#----------sum of the lists---------
# lst = [[1,2],[3,4],[5,6]]
# total = 0
# lst2=[]
# for sub in lst:
#     for i in sub:
#         total += i
#     lst2.append(total)
# print(lst2)

#--------copy-------------
import copy

lst = [[1,2],[3,4]]
shallow = lst.copy()
deep = copy.deepcopy(lst)

lst[0][0] = 100

print("Original:", lst)
print("Shallow:", shallow)
print("Deep:", deep)

