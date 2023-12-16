#### take input number as a string , convert to int number and find summation
# number_in_text = input('Enter some number as text : ')

# list_number = number_in_text.split()
# sum =0
# for x in list_number :
#   sum =sum+ int(x)
# print('Sum is =',sum)

#### take input as a string , find number of digits, number of letters and number of words
input_text = input('Enter Your Text : ')

numberOfDigits = 0; NumberOfLetters = 0; NumberOfWords =0
for x in input_text:
  x=x.lower()
  if x >= 'a' and x <= 'z' :
    NumberOfLetters = NumberOfLetters+1
  elif x>='1' and x<='9' :
    numberOfDigits = numberOfDigits +1
  elif x == ' ':
    NumberOfWords =NumberOfWords +1

print('Number of letters : ', NumberOfLetters)
print('Number of words : ', NumberOfWords+1)
print('Number of digits : ', numberOfDigits)
