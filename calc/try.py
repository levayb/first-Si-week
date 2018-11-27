# 2018.11.27
# Codwar session

import os


def invert(lst):
    # my solution
    result = []
    for i in lst:
        if i > 0:
            i -= i*2
            if i == 1:
                i -= 2
                result.append(i)
            result.append(i)
        else:
            i += (-i)*2
            result.append(i)
            if i == -1:
                i += 2
                result.append(i)
    return result

    # Gábor solution
    result = []
    for i in lst:
        if i > 0:
            result.append(-i)
        else:
            result.append(abs(i))
    return result

    # net soluton 1
    result = []
    for i in lst:
        result.append(i * (-1))
    return result

    # net solution 2
    return [x * (-1) for x in lst]


'''
Your task is to find the first element of an array that is not consecutive.
E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all
consecutive but 6 is not, so that's the first non consecutive number.
If the whole array is consecutive then return null
The array will always have at least 2 elements and all the elements will be numbers. 
The numbers will also all be unique and in ascending order.
The numbers could be positive or negative and the first non-consecutive could be either too!
'''


def first_non_consecutive(arr):
    num = len(arr)-1
    for i in range(num):
        if arr[i] + 1 != arr[i + 1]:
            return arr[i + 1]
        else:
            if arr[i] == arr[-2]:
                return "null"


'''
Ask a small girl - "How old are you?". She always says strange things... Lets help her!

For correct answer program should return int from 0 to 9.

Assume test input string always valid and may look like "1 year old" or "5 years old", etc..
The first char is number only.
'''


def get_age(age):
    return int(age[0])


'''
In this simple exercise, you will build a program that takes a value, integer,
and returns a list of its multiples up to another value, limit. If limit is a multiple of integer, 
it should be included as well. There will only ever be positive integers passed into the function, 
not consisting of 0. The limit will always be higher than the base.
For example, if the parameters passed are (2, 6), the function 
should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.'''


def find_multiples(integer, limit):
    result = [integer]
    constans = integer
    while integer != limit:
        integer += constans
        result.append(integer)
    return result


    result = [integer]
    constans = integer
    while integer <= limit:
        integer += constans
        result.append(integer)
    del result[-1]
    return result

    lst = []
    for i in range(integer, (limit + 1), integer):
        if i <= limit:
            lst.append(i)
    return lst


def add(n):
    def kecske(a):
        return "Bassza meg " + str(n * a) + "-ször az annyját aki ilyet kitalál 7 kyu-nál "
    return kecske


def elimination(arr):
    new_list = []
    for i in arr:
        if i not in new_list:
            new_list.append(i)
        else:
            return i


def to_query_string(data):
    # to_query_string({ "bar": [ 2, 3 ], "foo": 1 }) // => "bar=2&bar=3&foo=1"
    final_string = ""
    for key, value in data.items():
        if type(value) == list:
            for i in range(len(value)):
                final_string += key + "=" + (str(value[i])) + "&"
        else:
            final_string += key + "=" + (str(value)) + "&"
    return final_string.strip("&")


def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0], signature[1]]
    elif n > 2:
        a = signature[0]
        b = signature[1]
        c = signature[2]
        fib = a + b + c
        listFib = [a , b, c]
        for i in range(0, (n - 3)):
            listFib.append(fib)
            a = b
            b = c
            c = fib
            fib = a + b + c
        return listFib

'''
8 coins are given where all the coins have equal weight, except one. 
The odd one weights less than the others, not being of pure gold. 
In the worst case, how many iterations are actually needed to 
find the odd one out on a two plates scale.
I am asking you then to tell me what is the minimum 
amount of weighings it will take to measure n coins in 
every possible occurrence (including worst case scenario, ie: without relying on luck at all).
n is guaranteed to be a positive integer.
Tip: being able to think recursively might help here :p
Note: albeit this is more clearly a logical than a coding problem, 
do not underestimate (or under-rank) the kata for requiring not necessarily wizard-class coding skills: 
a good coder is a master of pattern recognition and subsequent optimization ;)'''


def how_many_measurements(n):
    if n > 1:
        return 1 + how_many_measurements(n / 3)
    else:
        return 0


'''
I I I I  # each Pin has a Number:    7 8 9 10
I I I                                4 5 6
I I                                  2 3
I                                    1'''

"I I I  \n I I I \n    I  \n       "


def bowling_pins(arr):
    pin_list = [        # index of string
        [7, 8, 9, 10],  # 0 2 4 6
        [4, 5, 6],      # 9 11 13
        [2, 3],         # 19 21
        [1]             # 28
        ]
    pin_table = ["I", " ", "I", " ", "I", " ", "I",
                                "\n", " ", "I", " ", "I", " ", "I", " ", "\n",
                                " ", " ", "I", " ", "I", " ", " ", "\n", " ",
                                " ", " ", "I",  " ", " ", " "]
    for f in range(len(arr)):
        for i in arr:
            if i == 1:
                pin_table[27] = " "
            elif i == 2:
                pin_table[18] = " "
            elif i == 3:
                pin_table[20] = " "
            elif i == 4:
                pin_table[9] = " "
            elif i == 5:
                pin_table[11] = " "
            elif i == 6:
                pin_table[13] = " "
            elif i == 7:
                pin_table[0] = " "
            elif i == 8:
                pin_table[2] = " "
            elif i == 9:
                pin_table[4] = " "
            else:
                pin_table[6] = " "
    var = ""
    for i in pin_table:
        var += i
    return var


def how_many_bees(hive):
    for i in 

    # Gábor solution
    # lst = []
    # horizontal_list = []
    # vertical_list = []
    # var = ""
    # if len(hive) > 0:
    #     for i in hive:          # vízszintes sorok darabolása
    #         lst.append(i)
    #     for j in lst:           # szétszedve 3 karakteresre,
    #         var = j[0:3]
    #         horizontal_list.append(var)
    #         var = j[4:7]
    #         horizontal_list.append(var)
    # #[  'bee', 'bee', 
    # #   '.e.', 'e..', 
    # #   '.b.', 'eeb'

    # #print(bee_counter_list)
    # var = horizontal_list[0][0] + horizontal_list[2][0] + horizontal_list[4][0]
    # vertical_list.append((var))
    # var = horizontal_list[0][1] + horizontal_list[2][1] + horizontal_list[4][1]
    # vertical_list.append((var))
    # var = horizontal_list[0][2] + horizontal_list[2][2] + horizontal_list[4][2]
    # vertical_list.append((var))
    # var = horizontal_list[1][0] + horizontal_list[3][0] + horizontal_list[5][0]
    # vertical_list.append((var))
    # var = horizontal_list[1][1] + horizontal_list[3][1] + horizontal_list[5][1]
    # vertical_list.append((var))
    # var = horizontal_list[1][2] + horizontal_list[3][2] + horizontal_list[5][2]
    # vertical_list.append((var))
    # final = vertical_list + horizontal_list
    # print(horizontal_list)
    # print(vertical_list)
    # print(final)
    # #print(bee_counter_list)
    # bee_counter = 0
    # for i in final:
    #     if i == "bee":
    #         bee_counter += 1
    #     elif i == "eeb":
    #         bee_counter += 1
    # return bee_counter


def show(hive):
    print('\n'.join(hive))
    return list(map(list, hive))


def main():
    hive = ["bee.bee",
            ".e..e..",
            ".b..eeb"]
    show(hive)
    print(how_many_bees(hive))


if __name__ == "__main__":
    main()
