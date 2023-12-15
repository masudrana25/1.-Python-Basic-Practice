#Basic if Statement
'''
mark = 55
if mark>=33 :
  print('Passed')
else :
  print('Failed')
'''

# Complete if--elif--else statement
'''
a =55
if a>0 :
  print('Positive Number')
elif a<0 :
  print('Negative Number')
else :
  print('Zero')
'''

#odd-even number find
'''
a= 21
if a%2 == 0 :
  print('Even')
else :
  print('Odd')
'''

# max between 3 number 
num1 = 77
num2 = 5
num3 = 6

if num1 > num2 :
  if num1 > num3 :
    print('Max is ',num1)
  else :
    print('Max is ',num3)
else :
  if num2 > num3 :
    print('Max is ',num2)
  else :
    print('Max is ',num3)