'''
try:

  ### j kaj a error asty parey , sei part ta k ai try block er moddhy rakhbo 
  list1 = [30,0,45]
  div = list1[0]/list1[1] # div = list[0]/ list1[3] #div = list[1]/ '22'
  # print(div)
  # print('Done')

#### somvabbo error gula handle and known the issues
except TypeError :
  print('Type Error is Occurred')
except ZeroDivisionError : 
  print('ZeroDivision Error is Occurred')
except IndexError :
  print('Index Error is Occurred')
except ValueError :
 print('Value Error is Occurred')

#### multiple errors handle in one exception
#except (ValueError, IndexError, ZeroDivisionError, TypeError) :
#  print('Multiple errors occurred')

#### uporer code run koruk or na koruk, ai finally block er kaj korbei
finally : 
  print('Printed from Finally section')
'''

#### raise exception
'''
def vote(age) :
  if age <18 :
    raise ValueError('Invalid Age')
  return 'You are Allowed to vote'

try :
  print(vote(19))
  print(vote(17))
except ValueError as error :
  print(error)
'''