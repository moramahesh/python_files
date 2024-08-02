def sub(s1,s2):
    for i in range(len(s2)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                d = True
            else:
                d = False
    if d ==True:
        print("Yes")
    else:
        print("No")
if __name__=="__main__":
    n = 2
    if n==2:
        s1 = input()
        s2 = input()
    sub(s1,s2)