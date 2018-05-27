
p=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
n=int(input()) #Number of floor stops
init=int(input()) #Initial floor number

l=len(p)
for i in range(n,l):
    del(p[l-1])
    l-=1

for i,val in enumerate(p): #Sequence of floors 
    p[i]=int(input())
p.sort()


for i,val in enumerate(p):
    if(val>init):
        pos=i
        break

for i,val in enumerate(p):
    if(val==init):
        for i,val in enumerate(p):
            if(i!=l-1 and i>=pos-1):
                p[i]=p[i+1]
        del p[l-1]
        l-=1
        pos-=1
        
print("Going up first")
print(init)
for i,val in enumerate(p):
    if(i>=pos):
        print(val)
    
for i,val in enumerate(p):
    if(i<pos):
        print(val)
dist=(p[l-1]-init)+p[l-1]-p[0];
print(dist);

print("Going down first")
print(init)
for i,val in enumerate(p):
    if(i<=pos):
        print(val)
    
for i,val in enumerate(p):
    if(i>pos):
        print(val)
dist=(init-p[0])+p[l-1]-p[0];
print(dist);

