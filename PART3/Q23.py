n=int(input())


score=[]

for _ in range(n):
    a,b,c,d=input().split()
    score.append((a,int(b),int(c),int(d)))


sorted_score=sorted(score,key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in range(n):
    print(sorted_score[i][0])
