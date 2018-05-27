
def add(p):
    r=0;
    for i,val in enumerate(p):
        r+=p[i][1];
    return r;

def goUp(p,t,n,u) :
   i=1;z=0;
   while(i<n):
      if(t>0 and add(p)!=0):
         print("p[i][2] {} p[1][2] {}".format(p[i][1],p[1][2]))
         t-=p[i][2]
         if(t<0):
            t=0
         t+=p[i][1]
         
         print("wtf {} ".format(t))
         if(t>T):
            p[i][1]=t-T
            t=T
         else:
            p[i][1]=0
         print("{} {}".format(p[i][1],t))
         print(p[i][0])
      else:
         z=i+1
      i+=1
   u+=1
   return z

def goDown(p,t,n,d) :
   i=n-2;z=0;
   while(i>=0):
      if(t>0 and add(p)!=0):
         t-=p[i][2]
         if(t<0):
            t=0
         t+=p[i][1]
         
         
         if(t>T):
            p[i][1]=t-T
            t=T
         else:
            p[i][1]=0
         print("{} {}".format(p[i][1],t))
         print(p[i][0])
      else:
         z=i+1
      i-=1
   d+=1
   return z

u=0;d=0;
p=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
n=int(input()) #Number of floor stops
init=int(input()) #Initial floor number

l=len(p)
for i in range(n,l):
    del(p[l-1])
    l-=1
    
T=int(input());
for i,val in enumerate(p): #Sequence of floors 
    p[i][0]=int(input())
    p[i][1]=int(input())
    p[i][2]=int(input())
    
p.sort()

pos=0
t=0;
for i,val in enumerate(p):
    if(val[0]>init):
        pos=i
        break

for i,val in enumerate(p):
    if(val[0]==init):
        for i,val in enumerate(p):
            if(i!=l-1 and i>=pos-1):
                p[i][0]=p[i+1][0]
                p[i][1]=p[i+1][1]
                p[i][2]=p[i+1][2]
        del p[l-1]
        l-=1
        pos-=1
        
#print(pos)
print(init)

for i,val in enumerate(p):
   if(i>=pos):
      t-=p[i][2]
      if(t<0):
         t=0
      t+=p[i][1]
      if(t>T):
         p[i][1]=t-T
         t=T
      else:
         p[i][1]=0
      print("{} {}".format(p[i][1],t))
      print(p[i][0])
c=0;z1=0;z2=0;
#print(p[1][1])
while True:
   c+=1
   z1=goDown(p,t,n,d)
   if(z1!=0):break;
   z2=goUp(p,t,n,u)
   if(z2!=0):break;
   
   
   
'''for i,val in enumerate(p):
   if(i<pos):
      t+=p[i][1]-p[i][2]
      if(t>T):
         p[i][1]-=T-t #might not work.... !!!
         print("{} ".format(p[i][1]))
      else:
         p[i][1]=0
      print(p[i][0])
   if(t<=0):break;


3
25  
20
1
50 
20
27
40    
10
100
50 
10
        
3
25  
20
1
50 0
20
27
40 0    10
10
100
50 10
10

3
25
10
2
10       
5
5
30       
15
30
20      
20

3
25
10
------2
10       0
5
------5
30       0
15
------30
20       0      10
20
'''

print("c is {}".format(c))
print("z1 is {}".format(z1))
print("z2 is {}".format(z2))
print("u is {}".format(u))
print("d is {}".format(d))


'''print("p[n-1][0] is {}".format(p[n-1][0]))
print("init is {}".format(init))
print("p[0][0] is {}".format(p[0][0]))
print("p[z1-1][0] is {}".format(p[z1-1][0]))
print("p[n-1][0]-init is {}".format(p[n-1][0]-init))
print("2*(c-1)*(p[n-1][0]-p[0][0]) is {}".format(2*(c-1)*(p[n-1][0]-p[0][0])))
print("p[n-1][0]-p[z1-1][0] is {}".format(p[n-1][0]-p[z1-1][0]))
'''
if(z1!=0):
   dist = p[n-1][0]-init + 2*(c-1)*(p[n-1][0]-p[0][0]) + p[n-1][0]-p[z1-1][0];
else:
   dist = p[n-1][0]-init + 2*(c-1)*(p[n-1][0]-p[0][0]) + p[z1-1][0]-p[0][0] + p[n-1][0]-p[0][0];
print(dist);

