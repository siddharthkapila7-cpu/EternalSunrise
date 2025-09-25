import time


def main():
    num = int(input("Enter a number: "))
    #max = int(input("Enter max factor: "))
    write_table(num, 10)#max)


def write_table(a, b):
    for i in range(1, b + 1):
        print(f"{a} x {i} = {a * i}")
        time.sleep(0.5)
    print("End")

main() 