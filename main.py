import sys  # just to print on stderr
import matplotlib.pyplot as plt  # to plot math functions
import numpy as np  # to work with arrays

n = 4  # number of segments
total_time = 10  # total time of her journey
with_error = False
num_of_iter = 400  # can be set by user. Number of iterations to reach the value of c


#  we want to compute C value
def calculate_c_parameter(distances, speeds, previus_c):
    temp_sum = 0  # temp means temporary sum. We must sum up (j-th distance)/(j-th speed + c i-th)
    temp_sum_2 = 0  # second temp sum. We must calculate (j-th distance)/((j-th speed + c i-th)^2)

    for j in range(n):  # just a for loop to sum up to compute f(x)/f'(x)

        temp_sum += distances[j] / (speeds[j] + previus_c)
        temp_sum_2 += distances[j] / ((speeds[j] + previus_c) ** 2)
        if (speeds[j] + previus_c) == 0:  # check if we got a division by zero, math warning.
            print("DIVISION BY ZERO, WARNING", sys.stderr)
    c_updated = previus_c - ((temp_sum - total_time) / (-1.0 * temp_sum_2))  # return our value c.
    # Thus, return c c(i-th+1) = c(i-th)-f(x)/f'(x)

    return c_updated


# calculate f(x). Polynomial function of third grade.
def calculate_y_function(x_temp):
    return (distances[0] / (speeds[0] + x_temp)) + (distances[1] / (speeds[1] + x_temp)) \
           + (distances[2] / (speeds[2] + x_temp)) + (
                   distances[3] / (speeds[3] + x_temp)) - total_time


if __name__ == '__main__':
    c = 0.0  # arbitrary starting c
    # set up plot
    fig = plt.figure()  # create a figure
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    # arrays of distances
    distances = [5, 2, 3, 3]
    # arrays of speeds
    speeds = [3, 2, 6, 1]
    # x points on x axe
    x = np.linspace(-1, 3, 100)
    # stopping if function is smaller or greater than some error

    y = calculate_y_function(x)  # calculate function for plot

    for k in range(num_of_iter):  # loop to find the root of f(x)
        c = calculate_c_parameter(distances, speeds, c)  # compute c updated
        if with_error:
            error = 1 * 10 ^ (-2)  # calculate this error if user wants to work with errors
            y_temp = calculate_y_function(c)  # calculate y if necessary. We want to check if f(x)
            # is enough small to stop our algorithm
            if -error < y_temp < error:  # check condition
                print("STOPPING LOOP...ROOT FOUND")
                print("Value of c: ", c, "Value of Y(c) : ", y_temp)
                break  # stop the loop if we have already found the root
        print("Values of c : ", c)

    # plotting f(x)
    plt.plot(x, y, 'r')
    plt.show()
