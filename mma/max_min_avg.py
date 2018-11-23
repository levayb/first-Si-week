# max-min-avg app
# 2018.11.23

import os 

# The story
# Algorithms are one of the most important things for programmers - 
# they are the foundations on which we build our programs. 
# No matter which language you (will) use, the algorithms are always involved.

# So, no more talking, let's practice some of them - 
# calculating minimum, maximum and average from numbers in a list.

# PLEASE DO NOT USE BUILT-IN PYTHON FUNCTIONS TO CALCULATE MIN, MAX, AND AVG! 
# Those forbidden functions are: min(), max(), sum(), sort(), sorted() etc.

# The exercise
# 1. Let's assume we've got a list: numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
# 2. Please create three flowcharts for calculating the maximum, 
# minimum and average number for above list (you can use draw.io ).
# 3. After this, please create a python script that will implement above flowcharts.
# 4. (optional) Now, the list looks a bit different: 
# numbers = [-5, 23, 0, "dupa", -9, 12, 99, [2, 44], None, 105, -43] ** 
# Update your python script to maintain its previous functionality - **
# please ignore non-numbers and search for numbers inside nested list!


def maximum(number_list):
    max_number = 0
    for i in number_list:
        if i > max_number:
            max_number = i
    return max_number


def minimum(number_list):
    min_number = 0
    for y in number_list:
        if y < min_number:
            min_number = y
    return min_number


def average(number_list):
    avg_number = 0
    for j in number_list:
        avg_number = avg_number + j
    avg_number = avg_number / len(number_list)
    return avg_number


def main():
    os.system('clear')
    numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
    print('The maximum number in list is: ', maximum(numbers))
    print('\nThe minumum number in list is: ', minimum(numbers))
    print('\nThe average number of the list is: ', average(numbers))


if __name__ == "__main__":
    main()
