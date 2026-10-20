# Dictionary : key-value pairs
#  d={}
#  print(type(d))    dict 

# order maintained 

# d={10:100, 20:200}
# print(d[10])    100 

# key can be any data type 

# you can change value but you can not change key 

# first way to create dict: 
# d = {"hello":100 , "bro":200}
# d["hello"] = 1000

# no duplicate keys but have duplicate values 

# second way to create dict :
# d = dict(name="payal" , age=24, gender = "female")
# print(d)

# third way to create dict: 
# d = dict([("name","payal"),("age",24)])
# print(d)

# Dic Traversing: 
# 1) a={10:100, 20:200, 30:300, 40:400}
# for i in a :
#  print(i)  Keys 
#  print(d[i]) values

# 2)by method
    # for i in a.values():           it give only values
    #       print(i)    

# Dic Methods: 
# .get : a={10:100,20:200}
#        print(a.get(10))  100

# you see another methods with help(Dict)

# setdefault: a={10:100, 20:200, 30:300, 40:400}
#             a.setdefault(12)
#             print(a)      {10:100,20:200,30:300,40:400,12:None}


# update: 
# a = {10:100,20:200}
# b = {30:300, 40:400}

# a.update(b) 
# print(a)