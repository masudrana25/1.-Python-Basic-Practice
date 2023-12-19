# xargs = x arguments
'''
def students( *details) : # take all the input arguments
  print(details) # print(details[0])
students(100,'AminuL iSLAM')
students(101,'Masud',2.34,'Chapainawabganj')
'''
'''
def add(*numbers) : # take all the input arguments
  sum =0
  for num in numbers :
    sum = sum + num
  return sum
print(add(10,20)); print(add(10,20,30)); print(add(10,20,30,40,))
'''

#### xxargs = xx arguments
'''
def students (id,name) :
  print(id,name)
students(id = 101, name = 'Masud')
'''

def students(**details) :
  print(details) # print(details['id']) #print(details['name'])
students(id = 101, name = 'Masud')


