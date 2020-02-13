import heapq

S = input().split(" ")
N = int(S[0])
M = int(S[1])
S = input()

arr = [-int(s) for s in S.split(" ")]

heapq.heapify(arr)

for i in range(M):
    maxValue = -heapq.heappop(arr)
    heapq.heappush(arr,-(maxValue//2))

print(-sum(arr))