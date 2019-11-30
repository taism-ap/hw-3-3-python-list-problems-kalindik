from random import randint
def random_list(largest,size):
  l = []
  for i in range(size):
    n = randint(0,largest -1)
    l.append(n)
    
  return(l)

def find_minimum(l):
    
 min_num = l[0]
 for i in l:
   if(i < min_num):
     min_num = i
    
 return min_num

l = random_list(1000,10)
print (l)

print("Here is the list in ascending order:")
l.sort()
min_num = find_minimum(l)
print (l)

print("The Minimum Number is:", end=" ")
print(min_num) 
