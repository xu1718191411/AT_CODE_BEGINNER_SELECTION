N, M = list(map(int, input().split()))
ARR = list(map(int, input().split()))

total = sum(ARR)

print(max(-1,N-total))