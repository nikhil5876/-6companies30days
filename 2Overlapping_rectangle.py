def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1 = rec1[0]
        y1 = rec1[1]
        x2 = rec1[2]
        y2 = rec1[3]
        x1d = rec2[0]
        y1d = rec2[1]
        x2d = rec2[2]
        y2d = rec2[3]
        x_dist = min(x2,x2d) - max(x1,x1d)
        y_dist = min(y2,y2d) - max(y1,y1d)
        return x_dist > 0 and y_dist > 0
