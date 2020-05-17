K = int(input())
S = input()

def calculate(k,s):
    ss = list(S)

    if len(ss) > k:
        print("".join(ss[0:k]) + "...")
    else:
        print(s)

calculate(K,S)