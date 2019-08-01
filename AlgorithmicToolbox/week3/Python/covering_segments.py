# Uses python3
import sys
from collections import namedtuple


Segment = namedtuple('Segment', 'start end')
def custom_sort(t):
    return t[1]

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=custom_sort)
    while(len(segments) > 0):
        j = 0
        point = segments[0].end
        points.append(point)
        while(len(segments) > j):
            if(segments[j].start<= point and segments[j].end>=point):
                del segments[j]
            else:
                j+=1
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')