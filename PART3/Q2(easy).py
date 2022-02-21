def sum(a,b):
    return a+b


def product(a,b):
    return a*b


s=input()

hist=0

for i in s:
    sum_result=sum(hist,int(i))
    product_hist=product(hist,int(i))
    hist=max(sum_result,product_hist)

print(hist)
