a = [[] * x for x in range(105)]
visit = [0 * x for x in range(105)]
ans = 0
def dfs(node):
  global ans
  visit[node] = True
  num_vertex = 0
  for i in range(len(a[node])):
    if visit[a[node][i]] == False:
      num_node = dfs(a[node][i])
      if(num_node %2 == 0):
        ans+=1
      else:
        num_vertex+= num_node
  return num_vertex + 1      

n, m = map(int, input().split())
for i in range(m):
  x,y = map(int, input().split())
  a[x].append(y)
  a[y].append(x)
dfs(1)
print(ans)

  