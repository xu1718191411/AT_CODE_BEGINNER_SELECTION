import math
A, B, H, M = map(int,input().split())

def calculate(a, b, h, m):
    hradians = ((h % 12) / 12)*360 + (((m/60) % 12) / 12)*360
    mradians = (m / 60) * 360

    hx = a * math.sin(math.radians(hradians))
    hy = a * math.cos(math.radians(hradians))

    mx = b * math.sin(math.radians(mradians))
    my = b * math.cos(math.radians(mradians))

    print(distance(hx,hy,mx,my))

def distance(x1,y1,x2,y2):
    return math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
calculate(A, B, H, M)