S = input().split(" ")

A = int(S[0])
B = int(S[1])
X = int(S[2])

def calculate(A, B, N):
    return A * N + B * len(str(N))


def find(start, end, x):
    mid = (start + end) // 2
    midVal = calculate(A, B, mid)

    if end - start == 1:
        s1 = x - calculate(A,B,start)
        s2 = calculate(A,B,end) - x
        if s2 > 0:
            return start
        else:
            if s2 > s1:
                return start
            else:
                return end

    if midVal > x:
        return find(start, mid, x)
    elif midVal < x:
        return find(mid, end, x)
    else:
        return mid


result = find(0, 1000000000, X)
print(result)
