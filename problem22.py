N = int(input())
c=0
for _ in range(N):
    c = list(map(int,input().split()))
for i in c:
    if c.count(i)==1:
        c+=1
print(c)