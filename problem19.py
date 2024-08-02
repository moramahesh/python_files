n = int(input())
pl = []
for i in range(n):
    ps = int(input())
    pl.append(ps)
pl.sort()
maxn = max(pl)
maxcount = pl.count(max)