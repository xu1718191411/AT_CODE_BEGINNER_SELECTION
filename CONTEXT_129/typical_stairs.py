def calculate(n, arr2):
    steps = [0]*(n)
    steps[0] = 1

    if arr2.get(0) == True:
        steps[0] = 0
    else:
        steps[0] = 1

    if n == 1:
        return steps

    if arr2.get(1) == True:
        steps[1] = 0
    else:
        steps[1] = 1 + steps[0]

    if n == 2:
        return steps

    for index in range(2,n):
        if arr2.get(index) == True:
            steps[index] = 0
        else:
            steps[index] = steps[index-1] + steps[index-2]

    return steps

S = input().split(" ")
N = int(S[0])
M = int(S[1])


arr2 = {}
for i in range(M):
    index = int(input())
    arr2.setdefault(index-1, True)

result = calculate(N, arr2)

print(result[N-1] % 1000000007)


