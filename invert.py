def main():
    word = input("Enter a word: ")
    reverse(word)


def reverse(string):
    reverse = []
    i = length(string) - 1
    while i >= 0:
        reverse.append(string[i])
        i -= 1
    for i in range(0, length(reverse)):
        print(reverse[i], end="")
        

def length(string):
    count = 0
    for _ in string:
        count += 1
    return count

main()