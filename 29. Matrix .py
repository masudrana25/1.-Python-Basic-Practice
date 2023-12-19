# index = 0,1,2,3,4,5,6,7,8,9.........
new_matrix = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]
]
new_matrix[2][0]=222 # value change
#print(new_matrix[2][0])

for row in new_matrix :
  for col in row : 
    print(col)

