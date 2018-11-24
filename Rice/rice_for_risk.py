# Risk of dice
# 2018.11.03.

import random

'''
Write a python script, that generates 5 numbers between 
1 and 6 and prints them in a meaningful way
for the game. Sort the results for the attacker and for the defender,
so make roll pairs, like in this image:

In a dice pair, there are the following rules:

When the attacker's die value is larger: Attacker wins (1 defender unit dies)
When the 2 dice value is tie: Defender wins (1 attacker unit dies)
When the defender's die value is larger: Defender wins (1 attacker unit dies)

Calculate the Outcome of the rolls: 
https://code-embed-lti.herokuapp.com/placement/5jStvYEhHT6vKN2BuMfu
Add 2 questions and inputs, where the users can set how many attackers and
defenders play in the current roll.
Limit the attackers to only type 1, 2 or 3, and the defender to type only 1 or 2.
https://code-embed-lti.herokuapp.com/placement/hkRlVVsS5YcqqRlrATVP
'''


def attacker_user_input():  # ha elsőre rossz számot  vagy betűt kap akkor a jó szám után None lesz a return!!!!
    while True:
        attack_input = input("How many units attack: ")
        if attack_input.isdigit():
            if int(attack_input) == 1:
                return attack_input
            elif int(attack_input) == 2:
                return attack_input
            elif int(attack_input) == 3:
                return attack_input
            else:
                attacker_user_input()
                break
        else:
            attacker_user_input()
            break


def defender_user_input():  # ha elsőre rossz számot kap akkor a jó szám után None lesz a return!!!!
    while True:
        defend_input = input("How many units defend: ")
        if defend_input.isdigit():
            if int(defend_input) == 1:
                return defend_input
            elif int(defend_input) == 2:
                return defend_input
            else:
                defender_user_input()
                break
        else:
            defender_user_input()
            break


def random_num():
    num1 = random.randrange(1, 7)
    num2 = random.randrange(1, 7)
    num3 = random.randrange(1, 7)
    num4 = random.randrange(1, 7)
    num5 = random.randrange(1, 7)
    return num1, num2, num3, num4, num5


def attacker_nums(n1, n2, n3, attack_input):  # ez jó
    if attack_input == "1":
        nums_a = [n1]
    elif attack_input == "2":
        nums_a = [n1, n2]
        nums_a.sort()
        nums_a.reverse()
    else:
        nums_a = [n1, n2, n3]
        nums_a.sort()
        nums_a.reverse()
    return nums_a


def defender_nums(n4, n5, defend_input):  # ez jó
    if defend_input == "1":
        nums_d = [n4]
    else:
        nums_d = [n4, n5]
        nums_d.sort()
        nums_d.reverse()
    return nums_d


def fight(attack_input, defend_input, nums_a, nums_d):
    attacker_unit = 0
    defender_unit = 0
    if attack_input or defend_input == 1:
        if nums_a >= nums_d:
            defender_unit += 1
            print_outcome(attacker_unit, defender_unit)
        else:
            attacker_unit += 1
            print_outcome(attacker_unit, defender_unit)
    elif attack_input == 2 or attack_input == 3 and defend_input == 2:
        if nums_a[0] >= nums_d[0]:
            defender_unit += 1
            print_outcome(attacker_unit, defender_unit)
        else:
            attacker_unit += 1
            print_outcome(attacker_unit, defender_unit)
            if nums_a[1] >= nums_d[1]:
                defender_unit += 1
                print_outcome(attacker_unit, defender_unit)
            else:
                attacker_unit += 1
                print_outcome(attacker_unit, defender_unit)


def print_outcome(attacker_unit, defender_unit):
    print("\nOutcome:")
    print("  Attacker: Lost", attacker_unit, "unit")
    print("  Defender: Lost",  defender_unit, "unit\n")


def print_dice(nums_a, nums_d):
    print("\nDice:")
    if len(nums_a) == 3:
        print("  Attacker:", nums_a[0], "-", nums_a[1], "-", nums_a[2])
    elif len(nums_a) == 2:
        print("  Attacker:", nums_a[0], "-", nums_a[1])
    else:
        print("  Attacker:", nums_a[0])

    if len(nums_d) == 2:
        print("  Defender:", nums_d[0], "-", nums_d[1])
    else:
        print("  Defender:", nums_d[0])


def main():
    attacker_units = attacker_user_input()

    defender_units = defender_user_input()

    num1, num2, num3, num4, num5 = random_num()

    attack_numbers_list = attacker_nums(num1, num2, num3, attacker_units)

    defender_numbers_list = defender_nums(num4, num5, defender_units)

    attack_dice = attacker_nums(num1, num2, num3, attacker_units)

    defend_dice = defender_nums(num4, num5, defender_units)

    print_dice(attack_dice, defend_dice)

    fight(attacker_units, defender_units, attack_numbers_list, defender_numbers_list)


if __name__ == '__main__':
        main()
