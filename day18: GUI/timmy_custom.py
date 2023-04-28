import random
import turtle as t

t.colormode(255)

class NewTurtle(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.pencolor('black')
        self.pensize(17)
        self.shape('turtle')
        self.speed(9)

    def set_line_color(self):
        color_option = ["red", "green", "blue", "yellow", "orange", "purple",
                        "brown", "black", "gray", "cyan", "magenta",
                        "gold", "salmon", "seagreen", "violet", "navy",
                        "olive", "pink", "turquoise"]
        random_color = random.choice(color_option)
        self.pencolor(random_color)


    def set_line_color_rgb(self):
        rgb = []
        for _ in range(3):
            rgb.append(random.randint(0, 255))
        color = tuple(rgb)
        print(color)

    def random_walk(self):
        angles = [0, 90, 180, 270]
        self.setheading(random.choice(angles))
        self.fd(random.randint(10, 15) * 2)
