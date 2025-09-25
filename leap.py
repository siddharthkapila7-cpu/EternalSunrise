def main():
    num = int(input("Enter year: "))
    print(check(num))


def check(year):
    if year % 4 == 0 and year % 100 != 0:
        return "Leap year"
    elif year % 100 == 0 and year % 400 != 0:
        return "Not leap year"
    elif year % 400 == 0:
        return "Leap year"
    
main()