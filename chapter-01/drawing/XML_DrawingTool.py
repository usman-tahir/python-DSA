
class GoToCommand:
    def __init__(self, x, y, width = 1.0, color = "black"):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y)

    def __str__(self):
        return "<Command x=%s y=%s width=%s color=%s>GoTo</Command>" % \
            % (str(self.x), str(self.y), str(self.width), self.color)
