import math
route = [["TH","GA", "IC", "HA", "TE", "LU", "NI","CA"],[800, 600, 750, 900, 1400, 1200, 1100, 1500]]
sorc = input()
dest = input()
fare = 0.0
if sorc in route[0] and dest in route[0]:
    if route[0].index(sorc)< route[0].index(dest):
        for i in range(route[0].indesx(sorc),route[0].index(dest)+1):
            fare+=route[1][i]
    elif route[0].index(sorc) > route[0].index(dest):
        for i in range(route[0].index(sorc)+1,len(route[0])):
            fare+=route[1][i]
        for i in range(0,route[0].index(dest)+1):
            fare+=route[1][i]            
else:
    print("INVALID INPUT")
if fare!=0:
    print("fare:{}".format(float(math.ceil(fare*0.005))))
else:
    print("invalid input")