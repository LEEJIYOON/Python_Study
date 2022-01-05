n=input()

half=int(len(n)/2)

front=n[:half]
end=n[half:]


front_sum=0
end_sum=0

for i in front:
    front_sum+=int(i)

for j in end:
    end_sum+=int(j)

if front_sum==end_sum:
    print("LUCKY")
else:
    print("READY")
