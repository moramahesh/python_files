main_menu = input()
# sub_menu = input()
# items = {"c":['Espresso Coffee','Cappuucino Coffee','Latte Coffee'],
#          "T":['PlainTea','Assam Tea','Ginger Tea','Cardamom Tea','Masala Tea','Lemon Tea','Green Tea','Organic Darjeeling Tea'],
#          "S":['Hot and Sour Soup','Veg Corn Soup','Tomato Soup','Spicy Tomato Soup'],
#          "B":['Hot Chocolate Drink', 'Badam Drink','Badam-Pista Drink']
#          }
s="AABACBADA"
s =list(s)
k = 3
j,ml,l= 0,[],k
for m in range(len(s)//k):
    for i in s[j:k]:
        ml.append(i)
    for i in ml:
        mc = ml.count(i)
        if mc>1:
            ml.remove(i)
        else:
            print(ml)  
    ml.clear()
    j=k
    k += l  