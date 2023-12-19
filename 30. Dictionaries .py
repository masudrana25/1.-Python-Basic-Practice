# stored data # order style # changeable data # not allow duplication # can use boolian # can use list/array
students = {
  101 : 'Aminul Islam',
  102 : 'Masud Rana',
  103 : 'Firdous Rana',
  104 : 'Farhan Rana',
  105: ['Abdul ALim', 'Alam','Jibon'],
  106: True,
  107 : False
}
#print(students[101])
#print(students[109]) # give error as 109 is not available

#print(students.get(101))
#print(students.get(109)) # as item is not available, it will return "None" value

#print(students.get(103,'Not a Valid ID')) 
# jodi ID er value thakey, tobey value return korby , r na thakley 2nd a deya text ta dekhabey
#print(students.get(109,'Not a Valid ID')) 
