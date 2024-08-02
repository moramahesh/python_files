def  pal(s):
    steps = 0
    if s==s[::-1]:
        return 0
    for i in range(len(s)//2):
        steps += abs(ord(s[i])-ord(s[len(s)-i-1]))
    return steps
    
if __name__ =="__main__":
    n = int(input())
    for _ in range(n):
        s =input().strip()
        print(pal(s))