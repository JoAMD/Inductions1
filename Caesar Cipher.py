//Final code
r=""
r1=""

st=input()

n=int(st[0])
k=int(st[2])
p=["-","-","-","-","-","-","-","-","-","-","-","-","-"]
c=["-","-","-","-","-","-","-","-","-","-","-","-","-"]
for j,val in enumerate(p):
    if(j>=n):break
    p[j]=input()
    
for j,val in enumerate(c):
    if(j>=n):break
    c[j]=input()
 
for j,value in enumerate(p):
    if(j>=n):break
    r=""
    for i,val in enumerate(value) :
        o=ord((val))
        if(o>=65 and o<=90):
            if(o+k>90):
                r+=chr(o+k-26)
            else:
                r+=chr(o+k)

        elif(o>=97 and o<=122):
            if((o+k)>122):
                r+=chr(o+k-26)
            else:
                r+=chr(o+k)
        else:
            r+=(val)
           
    print(r)

for j,value in enumerate(c):
    if(j>=n):break
    r=""
    for i,val in enumerate(value) :
        o=ord(val)
        if(o>=65 and o<=90): 
            if(o-k<65):
                r+=chr(o-k+26)
            else:
                r+=chr(o-k)

        elif(o>=97 and o<=122):
            if((o-k)<97):
                r+=chr(o-k+26)
            else:
                r+=chr(o-k)
        else:
           r+=val
    print(r) 

