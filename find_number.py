from random import randint
def random_list(largest,size):
  l = []
  for i in range(size):
    n = randint(0,largest -1)
    l.append(n)
    
  return(l)

def find_number(l):
  count = 0
  for i in l:
    if (i == num):
      count +=1
  return (count)

l = random_list(10,10)
print (l)
num = int(input("Type a number from 0 to 10"))
print('{} has occurred {} times'.format(num,find_number(l)))
