import itertools

n = int(input())


def calculate(n, length):
    count = 0
    for i in itertools.product([3, 5, 7], repeat=length):
        if isValid(i) == False:
            continue
        sum = 0
        for j in range(length):
            sum = sum + i[j] * 10 ** j
        if sum <= n:
            count = count + 1

    return count


def isValid(n):
    dict = {}
    for s in n:
        if dict.get(s) == None:
            dict.__setitem__(s, 1)
        else:
            dict.__setitem__(s, dict.get(s) + 1)

    s1 = dict.get(3) != None and dict.get(3) > 0
    s2 = dict.get(5) != None and dict.get(5) > 0
    s3 = dict.get(7) != None and dict.get(7) > 0

    return s1 and s2 and s3


length = len(str(n))

result = 0
for i in range(3, length + 1):
    result = result + calculate(n, i)

print(result)