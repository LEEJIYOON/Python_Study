from itertools import combinations

n,m=map(int,input().split())
weight_list=list(map(int,input().split()))

all_case=list(combinations(weight_list,2))
max_case=len(all_case)
duplicated_case=0

for i in all_case:
    if i[0]==i[1]:
        duplicated_case+=1

result=max_case-duplicated_case

print(result)

