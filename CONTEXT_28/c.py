ARR = list(map(int, input().split()))
result = set()
import sys
sys.setrecursionlimit(10000000)
def calculate(arr):
    dfs(arr[0], 0, 1, arr, 3)
    dfs(0, 0, 0, arr, 3)

    print(sorted(result, key=lambda x: -x)[2])


def dfs(currentSum, currentIndex, currentK, arr, maxK):
    if currentK == maxK:
        result.add(currentSum)
        return

    if currentIndex == (len(arr) - 1):
        return

    dfs(currentSum + arr[currentIndex + 1], currentIndex + 1, currentK + 1, arr, maxK)
    dfs(currentSum, currentIndex + 1, currentK, arr, maxK)


calculate(ARR)
