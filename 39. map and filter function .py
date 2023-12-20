#### map function
'''
def square(a):
  result = a*a
  return result

list1 = [1,2,3,4,5,6,7,8,9]

square_result=list(map(square,list1))

print(square_result)
'''

#### filter function
#filter function--1
'''
def even(a):
  if a%2 == 0:
    return a

list1= [1,2,3,4,5,6,7,8]

even_result = list(filter(even,list1))

print(list1)
print(even_result)
'''

#filter function---2
list1= [1,2,3,4,5,6,7,8]

even_result = list(filter(lambda a : a%2 == 0,list1))
# true return korley oi element ta k new list a rakhbey
print(even_result)