n=int(input())

coin_list=list(map(int,input().split()))

coin_list.sort(reverse=True)

min_value=0


print(coin_list)

while True:
    min_value+=1
    temp=min_value

    for i in coin_list:
        if temp - i >=0:
            temp=temp-i
            if temp==0:
                continue

    if temp>0:
        break

print(min_value)
