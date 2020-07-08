N = 6
ARR = [
    "AC",
    "TLE",
    "AC",
    "AC",
    "WA",
    "TLE"
]
N = int(input())
ARR = []

for i in range(N):
    ARR.append(input())

acNum = 0
tleNum = 0
waNum = 0
reNum = 0
for i in range(N):
    if ARR[i] == "AC":
        acNum +=1

    if ARR[i] == "TLE":
        tleNum += 1

    if ARR[i] == "WA":
        waNum += 1

    if ARR[i] == "RE":
        reNum += 1



print("AC x {}".format(acNum))
print("WA x {}".format(waNum))
print("TLE x {}".format(tleNum))
print("RE x {}".format(reNum))