import heapq
N = 4
ARR = [2, 2, 1, 3]

N = 7
ARR = [1, 1, 1, 1, 1, 1, 1]

N = int(input())

ARR = list(map(int,input().split()))
def calculate(n, arr):
    result = []

    arr = sorted(arr,reverse=True)

    heapq.heappush(result,-1 * arr[0])

    ans = 0
    for i in range(1,n):
        ans -= heapq.heappop(result)

        heapq.heappush(result,-1 * arr[i])
        heapq.heappush(result, -1 * arr[i])

    print(ans)

calculate(N, ARR)