import random
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
    c = previus_c - (temp_sum - total_time) / (-1.0 * temp_sum_2)
    return c


if __name__ == '__main__':
    c = 0
    fig=plt.figure()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    distances = [5, 2, 3, 3]
    speeds = [3, 2, 6, 1]
    x= np.linspace(-5,5,100)



    y = (distances[0]/(speeds[0]+x))+(distances[1]/(speeds[1]+x))+distances[2]/(speeds[2]+x)+distances[3]/(speeds[3]+x)-total_time

    for k in range(400):
        c = calculate_C_parameter(distances, speeds, c)
        print("Values of c : ", c)
    plt.plot(x,y,'r')
    plt.show()