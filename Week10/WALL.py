from sys import stdin, stdout
n, wall, m, panel = int(stdin.readline()), list(map(int, stdin.readline().split())), int(stdin.readline()), list(map(int, stdin.readline().split()))
def ping_pong(min_height):
  u = 0
  for x in wall:
    if x < min_height:
      while (u < m) and (x + panel[u] < min_height):
        u += 1
      if u == m:
        return False
      u += 1
  return True
s_wall, s_panel = sorted(wall), sorted(panel)
low, high = s_wall[0], s_wall[-1] + s_panel[-1] + 1
if m >= n:
  low += s_panel[m - n]
else:
  high = min(s_wall[-1], min(s_wall[0] + s_panel[-1], s_wall[m - 1] + s_panel[0])) + 1
while high - low > 1:
  middle = low + (high - low) // 2
  if ping_pong(middle):
    low = middle
  else:
    high = middle
min_height, answer_list, u = low, list(), 0
for i, x in enumerate(wall, start=1):
  if x < min_height:
    while (u < m) and (x + panel[u] < min_height):
      u += 1
    u += 1
    answer_list.append((i, u))
stdout.write(str(min_height) + ' ' + str(len(answer_list)) + '\n')
for x in answer_list:
  stdout.write(str(x[0]) + ' ' + str(x[1]) + '\n')
