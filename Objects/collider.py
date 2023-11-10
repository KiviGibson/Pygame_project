class Collider:

    def __init__(self, width, height, sizex, sizey):
        self.center = (width + sizex/2, height + sizey/2)
        self.y = sizey/2
        self.x = sizex/2
        self.collision = []
        self.onground = False

    def colide(self, other):
        collision = []
        self.onground = False
        for o in other:
            col = o.collider
            if abs(self.center[0] - col.center[0]) < self.x + col.x:
                if abs(self.center[1] - col.center[1]) < self.y + col.y:
                    x = self.center[0] - col.center[0]
                    y = self.center[1] - col.center[1]
                    if abs(x) - abs(y) < 0:
                        if y > 0:
                            collision.append({"dir": "up", "obj": col})
                        if y < 0:
                            collision.append({"dir": "down", "obj": col})
                            self.onground = True
                    else:
                        if x > 0:
                            collision.append({"dir": "right", "obj": col})
                        if x < 0:
                            collision.append({"dir": "left", "obj": col})
        self.collision = collision

    def update(self, x, y):
        self.center = (x + self.x, y + self.y)
