import random
for x in range(1,6,1) :
  random_number = random.randint(1,6)
  guess_number = int(input('Enter a Guess Number : '))

  if guess_number == random_number :
    print('You Have Won')
  else : 
    print('You Have Loss');print('The random number Was : ',random_number)