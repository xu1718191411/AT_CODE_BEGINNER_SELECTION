# N = 10
# ARR = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
#
#
# N = 3
# ARR = [2, 2, 2]
#
# N = 3
# ARR = [2, 1, 2]
#
# N = 1
# ARR = [1]

N = int(input())
ARR = list(map(int,input().split()))

def calculate(n,arr):
    currentSearchIndexs = []
    currentSearch = 1
    for i in range(n):
        if arr[i] == currentSearch:
            if len(currentSearchIndexs) < currentSearch:
                currentSearchIndexs.append(i)
            else:
                currentSearchIndexs[currentSearch-1] = i

            currentSearch = currentSearch  + 1



    if len(currentSearchIndexs) == 0:
        print(-1)
        return

    print(n - len(currentSearchIndexs))

calculate(N,ARR)