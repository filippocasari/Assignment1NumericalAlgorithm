
import sys
import matplotlib.pyplot as plt
import numpy as np
n = 4
total_time = 10


def calculate_C_parameter(distances, speeds, previus_c):
    temp_sum = 0
    temp_sum_2 = 0
    for j in range(4):

        temp_sum += distances[j] / (speeds[j] + previus_c)
        temp_sum_2 += distances[j] / ((speeds[j] + previus_c) ** 2)
        if((speeds[j] + previus_c)==0 ):
            print("DIVISION BY ZERO, WARNING", sys.stderr)
            print("ROOT FOUND")
    c_updated = previus_c - ((temp_sum - total_time) / (-1.0 * temp_sum_2))

    return c_updated


if __name__ == '__main__':
    c = -0.4
    fig=plt.figure()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    distances = [5, 2, 3, 3]
    speeds = [3, 2, 6, 1]
    x= np.linspace(-2,3,100)


    error=1*10^(-2)
    y = (distances[0]/(speeds[0]+x))+(distances[1]/(speeds[1]+x))+(distances[2]/(speeds[2]+x))+(distances[3]/(speeds[3]+x))-total_time

    for k in range(1000):
        c = calculate_C_parameter(distances, speeds, c)
        y_temp = (distances[0]/(speeds[0]+c))+(distances[1]/(speeds[1]+c))+(distances[2]/(speeds[2]+c))+(distances[3]/(speeds[3]+c))-total_time
        if(y_temp>-error and y_temp<error):
            print("STOPPING LOOP...ROOT FOUND")
            print("Value of c: ", c, "Value of Y(c) : ", y_temp)
            break
        print("Values of c : ", c)
    plt.plot(x,y,'r')
    plt.show()