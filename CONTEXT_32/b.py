def calculate(s, k):
    if k > len(s):
        print(0)
        return

    res = set()

    for i in range(0, len(s) - k + 1):
        res.add(s[i:i + k])

    print(len(res))


s = input()
k = int(input())

calculate(s, k)

