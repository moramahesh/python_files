def bit(n):
    x = ""
    y = ""
    s=0
    while n!=0:
        x += str(n%2)
        n = n//2
    # x= str(bin(n))
    
    x = x[::-1]
    
    for i in range(len(x)):
        if x[i]=="1":
            y+="0"
        else:
            y+=str(1)
    for i in y[::-1]:
        if i=="1":
            s += 2**int(i)
    return s
if __name__ =="__main__":
    n = int(input())   
    print(bit(n))
     