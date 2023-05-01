from turtle import Turtle

MOVE_DISTANCE = 20


class Snake():
    def __init__(self) -> None:
        self.segments = []
        self.create_snakes()
        self.head = self.segments[0]

    def ver_elementos(self):
        for segment in self.segments:
            print(segment.xcor(), segment.ycor())

    def create_snakes(self):
        x_position = 0
        for _ in range(3):
            position = (x_position, 0)
            self.add_segment(position)
            x_position -= 20

    def add_segment(self, position):
        snake_portion = Turtle()
        snake_portion.penup()
        snake_portion.shape('square')
        snake_portion.color('white')
        snake_portion.goto(position)
        self.segments.append(snake_portion)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
