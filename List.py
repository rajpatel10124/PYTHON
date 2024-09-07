# # marks = [45,78,63,59,85] 
# # print(marks)
# # print(type(marks))
# # print(marks[0])
# # print(marks[1])
# # print(len(marks))

# # student = ["karan",86.4,"rajkot"] #this is list, list are mutable
# # print(student)
# # print(student[1])

# # student.append(45) # add elemate at the last point 
# # print(student)

# # list = [5,2,8] 
# # print(list)
# # print(list.sort())
# # print(list)
# # list.reverse() # reevrse the list
# # print(list)

# # list.insert(0,4) # add element at any point
# # print(list)


# l= list(range(9,-1,-1))
# print(l)

# l1=[47,64,33]
# l2=[88,77,99]
# print(l1)
# print(l2)
# l1.extend(l2)
# print(l1)
# l1.sort()
# print(l1)


# name=["raj","kathan"]
# surname=[ "tala", "kansagara"]
# fullname=list(zip(name,surname))
# print(fullname)

list_oflist = [[1,2],
               [3,4],
               [4,5],
               [5,6],
               [6,7]]
mylist=[item for list in list_oflist for item in list]
print(mylist)

matrix =[[3,4,5],[5,6,7,8]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      print(matrix[i][j]) 