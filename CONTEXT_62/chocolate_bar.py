S = input().split(" ")
H = int(S[0])
W = int(S[1])


def calculate(h, w):
    result = []
    for i in range(1, h):
        s1 = w * i
        s2 = (h - i) * (w // 2)
        s3 = (h - i) * w - s2

        minValue = min(min(s1, s2), s3)
        maxValue = max(max(s1, s2), s3)

        result.append(maxValue - minValue)

        if i <= h - 1:
            s1 = w * i
            s2 = ((h - i) // 2) * w
            s3 = (h - i) * w - s2
            minValue = min(min(s1,s2),s3)
            maxValue = max(max(s1,s2),s3)
            result.append(maxValue - minValue)

    for i in range(1, w):
        if i <= w - 1:
            s1 = i * h
            s2 = ((w - i) // 2) * h
            s3 = (w - i) * h - s2

            minValue = min(min(s1, s2), s3)
            maxValue = max(max(s1, s2), s3)
            result.append(maxValue - minValue)

        s1 = i * h
        s2 = (w - i) * (h //2)
        s3 = (w - i) * h - s2
        minValue = min(min(s1, s2), s3)
        maxValue = max(max(s1, s2), s3)
        result.append(maxValue - minValue)

    print(min(result))

calculate(H, W)
