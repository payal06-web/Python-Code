# Data structures are kind of storage that store multiple values

# Inbulit data structures: List, Tuple, Set, Dictionary
# Customized data structures: Stack, Queue, Linked List, Trees, Graphs

# 1)List: it is a heterogeneous nature
# List is mutable, you can change anything
# indexing
#  example: a=[10,20,30,45,50,60]
            #  print(a[3])
#           a[3] = 40
#           print(a)
# 
# slicing : print(a[0:3:1])

# COPY:
# 1) reference copy 
# a = [1,2,3,4]
# b = a
# b[1]=10

# print(a,b)        both changes

# 2)Shallow Copy
# a = [1,2,3,4,5,6]
# b = a.copy()
# b[0] = 100
# print(a,b)        b changes only

# 3)Deep copy 
# import copy
# a = [1,2,3,4,5,6]
# b = copy.deepcopy(a)
# b[0] = 100
# print(a,b)         b changes 

# difference between shallow copy and deep copy 

# Python mein Shallow Copy aur Deep Copy ka main difference yeh hota hai ki woh nested (compound) objects—jaise ek list ke andar dusri list—ko kaise handle karte hain.
# Agar hum simple terms mein samjhein, toh Shallow copy sirf upar-upar se (top-level) copy banata hai, jabki Deep copy recursively andar tak saare levels ko completely copy kar deta hai

# ex: a = [[10,20], [30,40]]    deep copy

# List Traversing:
# method1: a=[1,2,3,4,5,6]
#          for i in a:
#             print(i) 

# method2: a = [1,2,3,4,5,6]
#          for i in range(len(a)):
#            print(i)
#            print(a[i]) 

# List methods:

# append: a=[1,2,3,4]
#         # a.append(5)
#         print(a)

# clear: a.clear()
#        print(a)

# count:a=[10,20,10,11,10,10]
#       print(a.count(10))    4

# index: a=[10,20,30,40]
#         print(a.index(10))     0

# insert: a=[10,15,20,30,15,40]
#         a.insert(3,25)
#         print(a) 

# pop: a=[10,20,30,40]
#      popped = a.pop()    it will return value 
#      print(a)      [10,20,30]
#      print(popped)  40

# sort: a =[10,20,30,40,60,50]
#       a.sort()
#       print(a)
    

# etc