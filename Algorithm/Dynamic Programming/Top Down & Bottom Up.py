#python

#fibo

#top down

d=[0]*100

def pibo(x):
  if x==1 or x==2:
    return 1
  
  if d[x]!=0:
    return d[x]
  
  d[x]=pibo(x-1) + pibo(x-2)


#bottom up

d=[0]*100
d[1]=1
d[2]=1
n=00

for i in range(3,n+1):
  d[i]=d[i-1]+d[i-2]
