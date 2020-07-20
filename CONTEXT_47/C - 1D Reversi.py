S = input()

def calculate(s):
    categories = 0
    for i in range(len(s)):
        if i == 0:
            continue

        if s[i] != s[i-1]:
            categories += 1
            continue

    print(categories)



calculate(S)