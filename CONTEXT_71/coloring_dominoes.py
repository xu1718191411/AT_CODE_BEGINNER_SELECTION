N = int(input())
S1 = input()
S2 = input()

def prepare(s1,s2,n):
    result = []
    i = 0
    while i < n:
        if s1[i] == s2[i]:
            result.append(1)
            i += 1
        else:
            result.append(0)
            i += 2

    return result



def calculate(arr):
    ans = 1
    for index in range(len(arr)):
        if index == 0:
            if arr[index] == 0:
                ans = 6
            else:
                ans = 3
            continue
        #xo
        if (arr[index - 1] == 1) and (arr[index] == 0):
            ans *= 2

        #xx
        if (arr[index - 1] == 1) and (arr[index] == 1):
            ans *= 2

        #oo
        if (arr[index - 1] == 0) and (arr[index] == 0):
            ans *= 3

        #ox
        if (arr[index - 1] == 0) and (arr[index] == 1):
            ans *= 1

    print(ans % 1000000007)



arr = prepare(S1,S2,N)
calculate(arr)
