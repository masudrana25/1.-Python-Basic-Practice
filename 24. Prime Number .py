a =44

for x in range(2,a,1) :
  if a == 2 :
    print(a,'is a Prime Number')
    break
  elif a%x ==0 :
    print(a,'is not a Prime Number')
    break
else :
  print(a,'is a Prime Number')
