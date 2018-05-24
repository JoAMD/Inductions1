def quickSort(p):
   quickSortHelper(p,0,len(p)-1)

def quickSortHelper(p,first,last):
   if first<last:

       splitpoint = partition(p,first,last)

       quickSortHelper(p,first,splitpoint-1)
       quickSortHelper(p,splitpoint+1,last)


def partition(p,first,last):
   pivotvalue = p[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and p[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while p[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = p[leftmark]
           p[leftmark] = p[rightmark]
           p[rightmark] = temp

   temp = p[first]
   p[first] = p[rightmark]
   p[rightmark] = temp


   return rightmark


p=[0,0,0,0,0]
init=int(input())
for i,val in enumerate(p):
    #if(i>=n):break
    p[i]=int(input())
quickSort(p)

for i,val in enumerate(p):
    if(val>init):
        pos=i
        break
print (pos)
print(init)
for i,val in enumerate(p):
    if(i>=pos):
        print(val)
    
for i,val in enumerate(p):
    if(i<pos):
        print(val)
dist=2*(p[4]-init)+init-p[0];
print(dist);
