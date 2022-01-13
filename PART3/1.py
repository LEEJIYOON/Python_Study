#my code


n=int(input()) # number of adventurer
member=list(map(int,input().split()))

member.sort() # 작은순으로


group_cnt=0
group=[]

for i in member:
  group.append(i)
  
  if max(group)==len(group):
    group_cnt+=1
    group=[]

print(group_cnt)
