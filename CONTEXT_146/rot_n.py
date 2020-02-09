# 65 - 90
N = int(input())
S = input()
arr = []
for s in S:

    tmp1 = ord(s)


    if tmp1 <= (90-N):
        tmp2 = tmp1 + N
    else:
        tmp2 = 64 + tmp1 + N - 90

    arr.append(chr(tmp2))

result = "".join(arr)
print(result)