# 离散的PID调制
# 可以检查更改是吧
previous = 0
res_error = 0
acc_error =0
distance = [21, 22, 23, 24, 25]
kp = 1
ki = 1
kd = 1
for i in range(len(distance)):
    P_error = (distance[i]-20)*kp
    print("p out",P_error)
    acc_error = (distance[i]-20) + acc_error
    I_error = acc_error*ki
    print("I output",I_error)
    if i == 0:
        res_error = 0
    else:
        res_error = (distance[i]-20) - previous
    D_error = res_error*kd
    print("D output", D_error)
    previous = distance[i]-20


#写出一个爬虫程序  






