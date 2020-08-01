from collections import deque
SA = input()
SB = input()
SC = input()

def calculate(SA,SB,SC):
    a1 = list(SA)
    a2 = list(SB)
    a3 = list(SC)

    q1 = deque()
    for a in a1:
        q1.append(a)

    q2 = deque()

    for a in a2:
        q2.append(a)

    q3 = deque()

    for a in a3:
        q3.append(a)

    arr = [q1,q2,q3]
    stt = ["A","B","C"]

    currentIndex = 0

    while currentIndex >= 0:
        if len(arr[currentIndex]) == 0:
            break

        currentValue = arr[currentIndex].popleft()

        if currentValue == "a":
            currentIndex = 0
            continue

        if currentValue == "b":
            currentIndex = 1
            continue

        if currentValue == "c":
            currentIndex = 2
            continue

    print(stt[currentIndex])


calculate(SA,SB,SC)
