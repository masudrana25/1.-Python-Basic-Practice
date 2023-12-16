a = 12; b=4

#### GCD Finding
gcd = 1
small_number = a if a<b else b
for x in range(2,small_number+1,1) :
  #print(x)
  if a%x ==0 and b%x ==0:
    gcd =x
print(gcd)

#### LCM finding
lcd = int((a*b)/gcd)
print(lcd)