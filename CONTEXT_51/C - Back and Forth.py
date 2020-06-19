def calculate(cx1, cy1, cx2, cy2):

    Up = 'U'
    Right = 'R'
    Left = 'L'
    Down = 'D'

    h = abs(cy2 - cy1)
    w = abs(cx2 - cx1)

    if cx2 > cx1:
        if cy2 < cy1:
            Down = 'U'
            Up = 'D'
    else:
        if cy2 > cy1:
            Left = 'R'
            Right = 'L'
        else:
            Left = 'R'
            Right = 'L'
            Down = 'U'
            Up = 'D'

    return h * Up + w * Right + h * Down + (w + 1) * Left + (h + 1) * Up + (w + 1) * Right + Down + Right + (
            h + 1) * Down + (w + 1) * Left + Up


cx1, cy1, cx2, cy2 = -2, -2, 1, 1
cx1, cy1, cx2, cy2 = map(int,input().split())

print(calculate(cx1, cy1, cx2, cy2))