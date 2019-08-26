import sys
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str([self.x, self.y])

def constructing_points(x, y):
    points = [Point(x[i],y[i]) for i in range(len(x))]
    return sorted(points, key = lambda a:a.x)

def calculate_distance(pone, ptwo):
    return ((pone.x - ptwo.x)**2 + (pone.y - ptwo.y)**2)**0.5

def naive_minimum_distance(points):
    if len(points) == 1:
        return 0
    elif len(points) == 2:
        return calculate_distance(points[0], points[1])
    result = sys.maxsize
    for i in range(len(points)):
        for k in range(i+1, len(points)):
            result = min(result, calculate_distance(points[i], points[k]))
    return result



def minimum_distance(points):
    if len(points) < 4:
        return naive_minimum_distance(points)

    mid = len(points)//2
    d1 = minimum_distance(points[:mid])
    d2 = minimum_distance(points[mid:])    
    d = min(d1, d2)

    check_points = list()
    mid_line_x = (points[len(points) -1].x + points[0].x) / 2
    for i in range(len(points[:mid])):
        if abs(points[i].x - mid_line_x) <= d:
           check_points.append(points[i])

    for j in range(len(points[mid:])):
        if abs(points[j+mid].x - mid_line_x) <= d:
            check_points.append(points[j+mid])
    check_points = sorted(check_points, key = lambda a: a.y)

    for k in range(len(check_points)):
        for j in range(k+1, min(len(check_points), k+8)):
            if abs(check_points[k].y - check_points[j].y) <=d:
                d = min(d, calculate_distance(check_points[k], check_points[j]))
    return d

if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = constructing_points(x,y)
    print("{0:.9f}".format(minimum_distance(points)))
