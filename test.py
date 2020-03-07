"""
このファイルに解答コードを書いてください
"""
path = 'input.txt'
with open(path) as f:
	l = [s.strip() for s in f.readlines()]

d = {}
for i in range(len(l)-1):
	x = l[i].split(':')
	d[int(x[0])] = x[1]

d = sorted(d.items())

m = int(l[len(l)-1])

ans = ""

for i in range(len(d)):
	if m % d[i][0] == 0:
		ans += d[i][1]

if ans == "":
	print(m)
else:
	print(ans)