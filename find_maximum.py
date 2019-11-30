from random import randint
def random_list(largest,size):
  l = []
  for i in range(size):
    n = randint(0,largest -1)
    l.append(n)
    
  return(l)

def find_maximum(l):
    
 max_num = 0
 for i in l:
   if(i > max_num):
     max_num = i
    
 return max_num

l = random_list(10,10)
print (l)

print("Here is the list in ascending order:")
l.sort()
max_num = find_maximum(l)
print (l)

print("The Maximum Number is:", end=" ")
print(max_num) 
