s=input()


group=[0,0]

if int(s[0])==1:
    group[1]+=1
else:
    group[0]+=1

    
for i in range(1,len(s)):
    if s[i-1]!=s[i]:
        group[int(s[i])]+=1


change=min(group[0],group[1])

print(change)
