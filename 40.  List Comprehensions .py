num = [1,2,3,4,5,6,7,8,9,10]

#map function in Comprehension
#square_results = [ x*x for x in num] # [expression for element in list]
#print(square_results)

#filter function in Comprehension
even_results = [ x for x in num if x%2 ==0] 
# [expression for element in list if condition]
print(even_results)