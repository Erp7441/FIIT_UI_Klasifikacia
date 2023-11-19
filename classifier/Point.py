class Point:
    def __init__(self, x: float, y: float, color: str = None, parent_index: int = None):
        self.x = x
        self.y = y
        self.color = color
        self.parent_index = parent_index
