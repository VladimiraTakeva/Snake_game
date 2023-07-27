from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.turtles.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):
        for turtle in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[turtle - 1].xcor()
            y = self.turtles[turtle - 1].ycor()
            self.turtles[turtle].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for turtle in self.turtles:
            turtle.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.turtles[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.turtles[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.turtles[0].setheading(RIGHT)




