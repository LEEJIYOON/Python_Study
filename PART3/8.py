n=input()

new=sorted(n)
sum_number=0

answer=""


for i in new:
    if i.isdigit():
        sum_number+=int(i)
    else:
        answer+=i

str_sum_number=str(sum_number)

print(answer+str_sum_number)
