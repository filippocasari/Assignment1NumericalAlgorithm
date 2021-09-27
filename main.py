######### ASSIGNMENT ONE ##########
###################################
######### NEWTON's METHOD #########
###################################
# FILIPPO CASARI's IMPLEMENTATION #
###################################
import math
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
    with np.errstate(divide='ignore'):
        return (distances[0] / (speeds[0] + x_temp)) + (distances[1] / (speeds[1] + x_temp)) \
               + (distances[2] / (speeds[2] + x_temp)) + (
                       distances[3] / (speeds[3] + x_temp)) - total_time


if __name__ == '__main__':

    is_default_mode = (raw_input("Do you want to use default input values? (write yes or no) "))
    yes = "yes"
    if is_default_mode == str(yes):
        print("Using default arrays...")
        distances = [5, 2, 3, 3]
        speeds = [3, 2, 6, 1]
        print("Speed Array: " + str(distances))
        print"Distance Array: " + str(speeds)

    else:
        try:
            n = int(input("Insert size of your arrays: "))
        except:
            print("Not a number, sorry, retry")
            sys.stderr.write("EXIT")
            exit(1)

        distances = []
        speeds = []
        i = 0
        while i < n:
            temp_distance = int(input("Insert distance[" + str(i) + "]: "))
            if temp_distance < 0:
                print("Try again, distance can not be negative")
                continue
            distances.append(temp_distance)
            temp_speed = int(input("Insert speed[" + str(i) + "]: "))
            speeds.append(temp_speed)
            i += 1
        try:
            num_of_iter = int(input("Insert number of iterations: "))
            total_time = int(input("Insert total time (integer): "))
        except:
            print("Not a number, sorry, retry")
            sys.stderr.write("EXIT")
            exit(2)
    c = -0.0  # arbitrary starting c
    # set up plot
    fig = plt.figure(figsize=(60, 40), dpi=80)  # create a figure
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.xlim([-9, 2])
    # arrays of distances
    #
    # arrays of speeds
    #
    # x points on x axe
    x = np.linspace(-6, 2, 400)
    # stopping if function is smaller or greater than some error
    array_of_computed_y = []
    array_of_c_values = []
    y = calculate_y_function(x)  # calculate function for plot
    for k in range(num_of_iter):  # loop to find the root of f(x)
        c = calculate_c_parameter(distances, speeds, c)  # compute c updated
        y_temp = calculate_y_function(c)  # calculate y if necessary. We want to check if f(x)
        array_of_c_values.append(c)
        array_of_computed_y.append(y_temp)
        if with_error:
            error = 1 * 10 ^ (-2)  # calculate this error if user wants to work with errors

            # is enough small to stop our algorithm
            if -error < y_temp < error:  # check condition
                print("STOPPING LOOP...ROOT FOUND")
                break  # stop the loop if we have already found the root
        print("Values of c : ", c)
        print("Value of Y(c) : ", y_temp)
        if (y_temp == 0.0):
            print("ROOT FOUND, we do not need other iterations...")
            print("Number of iterations to reach root: ", k)
            break
    # plotting f(x)
    plt.plot(x, y, 'r', linewidth=4)

    plt.plot(array_of_c_values, array_of_computed_y, linewidth=6, markersize=10)
    plt.show()

#  end of file
