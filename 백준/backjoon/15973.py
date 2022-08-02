rect1 = list(map(int,input().split()))
rect2 = list(map(int,input().split()))


def intersect_area(rect1, rect2):
    x1, y1 = rect1[0], rect1[1]
    x2, y2 = rect1[2], rect1[3]
    x3, y3 = rect2[0], rect2[1]
    x4, y4 = rect2[2], rect2[3]

    point1 = [[x1,y1],[x2,y2],[x2,y1],[x1,y2]]
    point2 = [[x3,y3],[x4,y4],[x4,y3],[x3,y4]]

    # 벗어나 있는 경우
    if x2 < x3 or x1 > x4 or y2 < y3 or y1 > y4:
        return 'NULL'

    left_up_x = max(x1, x3)
    left_up_y = max(y1, y3)
    right_down_x = min(x2, x4)
    right_down_y = min(y2, y4)

    width = right_down_x - left_up_x
    height = right_down_y - left_up_y

    if width * height > 0:
        return 'FACE'
    else:
        if point1[0] == point2[1] or point1[1] == point2[0] or point1[2] == point2[3] or point1[3] == point2[2]:
            return 'POINT'
        else:
            return 'LINE'
print(intersect_area(rect1,rect2))