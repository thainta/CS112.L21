n = int(input())
a = list(map(int, input().split()))
p = l = r = summ = 0
res = sum(a)
for i in range(n):
    if summ + a[i] < a[i] :
        p = i
        summ = a[i]
    else:
        summ = summ + a[i]
    if res < summ:
        res = summ
        l = p
        r = i
print(l+1, r+1, res)
