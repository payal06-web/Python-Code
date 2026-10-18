# 2) Tuple: it is heterogeneous nature 
#  it is immutable nature 

#  a = (1,2,3,4)
#  a[1] = 10     this is not applicable

# Tuple unpacking
# a,b,c = (1,2,3)
# a = ()
# print(type(a))    tuple 
# a=(1)
# print(type(a))    int 
# a = (1,)
# print(type(a))    int 

# indexing and slicing:  
# a=(1,2,3,4,5,6)
# print(a[1])  2
# print(a[:3])  (1,2,3)

# Tuple traversing:
# method1:
# a = (10,20,30,40)
# for i in a:
#     print(i)

# method2: 
# a=(10,20,30,40)
# for i in range(len(a)):
#     print(i)   1,2,3,4
#     print(a[i])  10,20,30,40

# Tuple method: Only 2 meyhod
# first: a = (1,2,3,4,4,5)
#        print(a.count(4))   2
# second: a = (1,2,3,4)
#         print(a.index(1))  0

# 3) Set 
# s = {}
# print(type(s))  dict  

# s = {10,1}
# print(type(s))  set 

# you can only store hash values in set 

# list has no hash value 
# not store duplicate values 
# unordered nature 
# no indexing and no slicing 

# s={1,2,2,3,4}
# print(s)  {1,2,3,4}

# Set traversing: run on the basis of hash values 
# s = {1,24,6,87}
# 1) for i in s:
#     print(i)

# Set Methods:  set semi-mutable nature 

# add: s = {1,2,3,4,5,6}
#      s.add(7)
#      print(s) 

# clear : s.clear()
#         print(s) 

# difference: s1 = {10,20,30,40}
#             s2 = {30,40,50,60}
#             print(s1.difference(s2))     {10,20}             
#             print(s2.difference(s1))     {50,60}         
#             print(s2 - s1)        
#             s2 -= s1
#             print(s2)   {50,60}              

# intersection: print(s1 & s2)      {30,40}
 
# etc  
# help(Set) : to see other methods which is not discuss in this 