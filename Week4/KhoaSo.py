s1 = sorted(input().strip(), reverse = False)
d_1, d_2 = [], []
for i in s1:
    if int(i) % 3 == 2:
        d_2.append(i)
    if int(i) %3 == 1:
        d_1.append(i)
t = (len(d_1) + 2*len(d_2))%3
if t == 1:
    if len(d_1) != 0:
        s1.remove(d_1[0])
    else:
        s1.remove(d_2[0])
        s1.remove(d_2[1])
if t == 2:
    if len(d_2) !=0:
        s1.remove(d_2[0])
    else:
        s1.remove(d_1[0])
        s1.remove(d_1[1])
print(''.join(sorted(s1, reverse = True)))
