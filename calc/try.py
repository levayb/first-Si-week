'''
Who remembers back to their time in the schoolyard,
when girls would take a flower and tear its petals,
saying each of the following phrases each time a petal was torn:

I love you
a little
a lot
passionately
madly
not at all
When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls
would say for a flower of a given number of petals, where nb_petals > 0.
'''
import os


def invert(lst):
    # my solution
    # result = []
    # for i in lst:
    #     if i > 0:
    #         i -= i*2
    #         if i == 1:
    #             i -= 2
    #             result.append(i)
    #         result.append(i)
    #     else:
    #         i += (-i)*2
    #         result.append(i)
    #         if i == -1:
    #             i += 2
    #             result.append(i)
    # return result

    # Gábor solution
    #     result = []
    # for i in lst:
    #     if i > 0:
    #         result.append(-i)
    #     else:
    #         result.append(abs(i))
    # return result

    # net soluton 1
    # result = []
    # for i in lst:
    #     result.append(i * (-1))
    # return result

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


    # result = [integer]
    # constans = integer
    # while integer <= limit:
    #     integer += constans
    #     result.append(integer)
    # del result[-1]
    # return result

    # lst = []
    # for i in range(integer, (limit + 1), integer):
    #     if i <= limit:
    #         lst.append(i)
    # return lst

def main():
    os.system('clear')
    print(find_multiples(5, 25))


if __name__ == "__main__":
    main()
