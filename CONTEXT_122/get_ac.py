def calculate(n,q,S):
    indexes = [0 for i in range(n)]

    arr = list(S)

    for i in range(len(arr)):
        if i == 0:
            indexes[i] = 0
            continue
        if arr[i] == 'C' and arr[i-1] == 'A':
                indexes[i] = indexes[i-1] + 1
        else:
            indexes[i] = indexes[i-1]
    return indexes

def conclution(res,Q):
    for qrr in Q:
        s2 = res[qrr[1]-1]
        s1 = res[qrr[0]-1]
        print(s2-s1)


input1 = input().split(" ")

n = int(input1[0])
q = int(input1[1])
S = input()

res = calculate(n,q,S)

qrr = []

for i in range(q):
    qrr.append([int(s) for s in input().split()])

conclution(res, qrr)

