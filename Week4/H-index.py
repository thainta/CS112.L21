n = int(input())
l = list(map(int,input().split()))
l.sort()
c = 0
for i in range(len(l)+1):
  c+=l[i]
  if l[i] >= len(l) - i:
    print(len(l)-i)
    break
  if c == 0 and i == len(l) -1:
    print(0)
    break
