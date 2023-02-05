x_list = [int(i) for i in input().split()]
y_list = [float(i) for i in input().split()]
print(x_list,y_list)
xp = int(input())
yp = 0 
for i in range(len(x_list)):
    pr = 1
    for j in range(len(x_list)):
        if j != i:
            pr *= (xp-x_list[j])/(x_list[i]-x_list[j])
    yp += y_list[i]*pr

print("P({}) = {}".format(xp,yp))
