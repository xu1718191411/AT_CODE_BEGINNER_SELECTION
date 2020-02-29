S = input()
K = int(input())
def calculate(S,K):
    normalStart = 1
    firstOneArr = []
    for s in S:
        if s != "1":
            normalStart = int(s)
            break
        else:
            firstOneArr.append(1)
    if K > len(firstOneArr):
        print(normalStart)
    else:
        print(1)
calculate(S,K)