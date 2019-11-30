from random import randint
def random_list(largest,size):
  l = []
  for i in range(size):
    n = randint(0,largest -1)
    l.append(n)
    
  return(l)

def sort(array): 
  n = len(array)
  for i in range(n):
    for j in range(0, n-i-1):
      if array[j] > array[j+1] :
        array[j], array[j+1] = array[j+1], array[j]
  return array
  
l = random_list(10,10)
print ("List: ", end =" ")
print(l)
print ("Sorted: ", end =" ")
print(sort(l))
