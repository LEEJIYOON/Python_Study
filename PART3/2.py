s=input()



answer=0


def find_notzero(sss):  # find first position of not zero.
    for i in range(len(sss)):
        if int(sss[i])!=0:
            return i   
    return -1

def sum(a,b):
    return a+b

def product(a,b):
    return a*b

start=find_notzero(s)  #

if start==-1:
    print("no answer")

elif start==len(s)-1:
    answer=int(s[start])
    print(answer)

else:
    answer=int(s[start])
    for i in s[start+1:]:
        if int(i)==0:
            answer=sum(answer,int(i))
        else:
            answer=product(answer,int(i))
    
    print(answer)

