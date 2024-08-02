from collections import Counter
def fre(n):
    d =Counter(s)
    for i in d:
        if d[i]==1:
            print(i)
if __name__=="__main__":
    n = int(input())
    for i in range(n):
        s=list(map(int,input().split(',')))
        fre(s)            