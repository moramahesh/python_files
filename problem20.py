lis = []
avg = []
for i in range(3):
    lis.append(list(map(int,input().split(",")))) 
for i in range(3):
    avg.append((lis[0][i]+lis[1][i]+lis[2][i])//3)
maxvalue = max(avg)
for i in range(3):
    if avg[i]<70:
        print(f"Trainee {i+1} is unfit")
    elif avg[i]==maxvalue:
        print(f"Trainee number:{i+1}")       