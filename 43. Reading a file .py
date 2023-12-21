# file_take = open('43. file for py test .txt','r') # just for read file
# file_take = open('43. file for py test .txt','w') # just for write file
file_take = open('43. file for py test .txt','r+') # for both read & write files
# print(file_take.readable()); print(file_take.writable())

 #### read the inner text of that file
#inner_text = file_take.read()
#print(inner_text)

#### find the length of the inner text
#inner_text_size = len(inner_text) 
#print(inner_text_size)

#### read the lines from the file

#inner_lines = file_take.readlines() # read all lines
#inner_lines = file_take.readlines()[0] # read one specific line
#print(inner_lines)

#### read the lines from the file using for loop
for line in file_take:
  print(line)

file_take.close()