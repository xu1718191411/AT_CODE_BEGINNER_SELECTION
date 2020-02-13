S = input().split(" ")
N = int(S[0])
K = int(S[1])
S = list(input())

num = 0
for index in range(len(S)-1):
    if S[index] == 'L' and S[index+1] == 'L':
        num = num + 1
    if S[index] == 'R' and S[index+1] == 'R':
        num = num + 1

result = min(num + 2*K,N-1)

print(result)