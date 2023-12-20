### Named Function 
'''
def square(a,b):
  square=a*a+2*a*b + b*b
  return square
print(square(4,3))
'''
###Lamda or Anonymous Function

square = (lambda a,b : a*a + 2*a*b + b*b)(3,4)
print(square)
