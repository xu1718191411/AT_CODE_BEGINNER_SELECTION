S = input()
T = input()
def calculate(s, t):
    criterion = ["a", "t", "c", "o", "d", "e", "r"]
    isOk = True
    for i in range(len(s)):
        if s[i] == t[i]:
            continue

        if (s[i] == "@") or (t[i] == "@"):
            if (s[i] in criterion) or (t[i] in criterion):
                continue

        isOk = False
        break

    if isOk:
        print("You can win")
    else:
        print("You will lose")


calculate(S, T)
