# lambda expression: it is a kind of short function
# Ex: 
# 1) s = lambda a:a*2
# print(s(2))

# 2) add = lambda x,y:x+y
# print(add(1,6))

# Map: apply function to every item of an iterable and return a new iterable
# syntax : map(function , iterable)

# a = [1,2,3,4]
# l = []
# for i in a:
#     l.append(i**2)
# print(l)    

# OR 

# a = [1,2,3,4]
# l = map(lambda x:x**2, a)
# print(list(l)) 

# and

# def square(x):
#     return x**2
# a = [1,2,3,4,5,6]

# l = map(square, a)
# print(list(l))


# Filter
# a= [1,2,3,4,5,6,7,8]
# l = filter(lambda i:i%2 == 0, a) 
# print(list(l)) 

# zip: combine multiple iterables into pairs of elements 
# name = ["payal","pihu","priya"]
# ages = [24,22,23]
# combined = zip(name , age)
# print(list(combined))
# print(dict(list(combined)))

