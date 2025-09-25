import time

def main():
    num = int(input("Enter a number: "))
    print(f"{root(num)} \nThe value may or may not be approximate")


def root(a):
    for i in range(0, a):
        if i ** 2 == a:
            return i
    return approx(a)


def approx(a):
    for i in range(0, a):
        if i ** 2 < a and (i + 1) ** 2 > a:
            if (a - (i ** 2)) > (((i + 1) ** 2) - a):
                return i + 1
            else:
                return i

main()
