S = input().split(" ")
A = int(S[0])
B = int(S[1])
C = int(S[2])
D = int(S[3])
E = int(S[4])
F = int(S[5])

def calculate(a, b, c, d, e, f):
    result = []


    for x in range(0,31):
        for y in range(0,31):
            if a * x * 100 + b * y * 100 <= F:
                result.append([x, y])

    memo = {}

    for res in result:
        waterValue = res[0] * 100 * a + res[1] * 100 * b
        for m in range(0, 101):
            for n in range(0, 101):

                sugerValue = m * c + n * d

                if waterValue + sugerValue == 0:
                    break

                if waterValue + sugerValue > f:
                    break

                if (waterValue / 100 * e) < sugerValue:
                    break

                nondu = (sugerValue * 100) / (sugerValue + waterValue)
                memo[res[0],res[1],m,n] = nondu



    maxNonDu = max(memo.values())

    for k,v in memo.items():
        if v == maxNonDu:
            print(k[0]*a*100+k[1]*b*100+k[2]*c+k[3]*d,k[2]*c+k[3]*d)
            break

    memo.values()

calculate(A, B, C, D, E, F)
