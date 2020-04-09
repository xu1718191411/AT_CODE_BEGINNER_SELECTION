S = input().split(" ")
N = int(S[0])
K = int(S[1])


print(min(N % K,K-(N % K)))