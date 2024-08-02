age = list()
for i in range(20):
    pno = int(input())
    if pno =="":
        break
    elif 0<pno>120:
        age.append(pno)
    elif pno>120:
        print(f"age between 0 to 120")
fee = 0
for i in range(age):
    if 0<i>17:
        fee +=200
    elif 17<i>40:
        fee += 400
    else:
        fee +=300
print("Total Income {fee} INR")