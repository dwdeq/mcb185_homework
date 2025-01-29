def dist(x1,y1,x2,y2):
    dy = y2 - y1
    dx = x2 - x1
    d = (dx**2 + dy**2)**0.5
    return d

def prob(n):
    if (n >= 0 and n <= 1): return True
    else:                   return False

def geomean(a, b, c, d):
    return a * b * c * d / 4

def max(a, b, c, d):
    if a >= b and a >= c and a >= d:
        return a
    if b >= c and b >= d:
        return b
    if c >= d:
        return c
    return d
    