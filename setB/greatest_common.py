# Greatest common finder
# 2018.11.23

from fractions import gcd

'''
Write a program which takes two numbers from a command
line and prints the greatest common divisor of them.
'''
# A legnagyobb közös osztó előállítása:
# Az adott számok közös osztói csak olyan prímtényezőket tartalmaznak,
# amelyek mindegyik szám prímtényezős felbontásában szerepel.
# Ebből következik, hogy a közös osztók keresését
# a számok prímtényezős felbontása alapján keressük:
# a=630=2*3*3*5*7=2*(3**2)*5*7,
# b=252=2*2*3*3*7=(2**2)*(3**2)*7,
# c=2205=3*3*5*7*7=2*(3**2)*5*(7**2).
# Közös prímtényezők: a 3 (mindegyik számban kétszer), és a 7.
# Így a legnagyobb közös osztó: d=3*3*7=(3**2)*7=63.


def greatest_common(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    print(greatest_common(252, 630))


if __name__ == "__main__":
    main()
