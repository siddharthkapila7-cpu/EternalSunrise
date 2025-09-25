def main():
    answer = input("Enter a word: ")
    print(f"Number of vowels: {vowelcount(answer)}")


def vowelcount(word):
    count = 0
    countlist = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    length1 = len(word)
    
    for i in range(0, length1):
        if word[i] in vowels:
            count += 1
            countlist.append(word[i])
    
    length2 = len(countlist)

    for j in range(0, length2):
        print(countlist[j], end=" ")

    print("\n")
    return count

main()