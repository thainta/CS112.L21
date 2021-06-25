c = 10**9 + 7
n, k = map(int, input().split())
res = 1
temp = 0
for i in range(k):
    temp = temp + res 
    res = temp + res
print((res*n) % c)
