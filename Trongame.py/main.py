# This file was created by: Miguel Castrillon
# Base code provided by Storm Coder Dojo Coding for Children
# Additions to the code made by me with the assistance of Ai
''''
Don’t start the game until a key is pressed
Make the bikes go faster or slower
Add a border to the edge of the screen
Instead of the game finishing when you hit the edge of the screen, make the bikes re-appear at the opposite edge of the screen.
from turtle import *
from utilities import *
'''


from turtle import *
import math

class vector():
    __slots__ = ('x', 'y', 'hash')
  
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hash = None

    def copy(self):
        type_self = type(self)
        return type_self(self.x, self.y)

    def move(self, other):
        self.x += other.x
        self.y += other.y

    def rotate(self, angle):
        radians = angle * math.pi / 180.0
        cosine = math.cos(radians)
        sine = math.sin(radians)
        x = self.x
        y = self.y
        self.x = x * cosine - y * sine
        self.y = y * cosine + x * sine

    def __eq__(self, other):
        if isinstance(other, vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __hash__(self):
        if self.hash is None:
            pair = (self.x, self.y)
            self.hash = hash(pair)
        return self.hash

p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()

def swap_sides(head):
    if head.x > 190:
        head.x = -200
    elif head.x < -200:
        head.x = 190
    elif head.y > 190:
        head.y = -200
    elif head.y < -200:
        head.y = 190

def draw_bounding_box():
    up()
    goto(-200, -200)
    down()
    color('black')
    for count in range(4):
        forward(400)
        left(90)

def draw():
    global game_started, bike_speed

    if not game_started:
        return

    p1xy.move(p1aim)
    swap_sides(p1xy)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    swap_sides(p2xy)
    p2head = p2xy.copy()

    if p1head in p2body or p1head in p1body:
        print('Player blue wins!')
        return

    if p2head in p1body or p2head in p2body:
        print('Player red wins!')
        return

    p1body.add(p1head)
    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    ontimer(draw, bike_speed)

def start_game():
    global game_started
    game_started = True
    draw()

def increase_speed():
    global bike_speed
    bike_speed -= 5
    print(f'Bike speed increased. Current speed: {bike_speed}')

def decrease_speed():
    global bike_speed
    bike_speed += 5
    print(f'Bike speed decreased. Current speed: {bike_speed}')

def square(x, y, size, name):
    up()
    goto(x, y)
    down()
    color(name)
    begin_fill()

    for count in range(4):
        forward(size)
        left(90)

    end_fill()

game_started = False
bike_speed = 50

setup(420, 420, 370, 0)
hideturtle()
tracer(0, 0)
listen()
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 'd')
onkey(lambda: p2aim.rotate(90), 'j')
onkey(lambda: p2aim.rotate(-90), 'l')
onkey(start_game, 's')
onkey(increase_speed, 'w')
onkey(decrease_speed, 'x')
draw_bounding_box()
done()
mainloop()