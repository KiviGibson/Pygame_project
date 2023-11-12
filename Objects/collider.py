import math


class Collider:

    def __init__(self, width, height, sizex, sizey):
        self.center = (width + sizex/2, height + sizey/2)
        self.y = sizey/2
        self.x = sizex/2
        self.up = self.center[1] - self.y
        self.down = self.center[1] + self.y
        self.left = self.center[0] - self.x
        self.right = self.center[0] + self.x
        self.collision = []
        self.onground = False
        self.hit_celling = False

    def colide(self, other):
        collision = []
        self.onground = False
        self.hit_celling = False
        for o in other:
            col = o.collider
            if abs(self.center[0] - col.center[0]) < self.x + col.x:
                if abs(self.center[1] - col.center[1]) < self.y + col.y:
                    up = abs(self.up - col.down)
                    down = abs(self.down - col.up)
                    left = abs(self.left - col.center[0])
                    right = abs(self.right - col.center[0])
                    stay_above = self.center[0]+10 - col.left > 0 > self.center[0]-10 - col.right
                    if stay_above:
                        if up < down:
                            collision.append({"dir": "up", "obj": col})
                            self.hit_celling = True
                        else:
                            collision.append({"dir": "down", "obj": col})
                            self.onground = True
                    else:
                        if right < left:
                            collision.append({"dir": "right", "obj": col})
                            print("right")
                        else:
                            collision.append({"dir": "left", "obj": col})
                            print(right, left)
ddddddddddddd                            print("left")

        self.collision = collision

    def update(self, x, y):
        self.center = (x + self.x, y + self.y)
