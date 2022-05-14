"""I draw a smiling face!"""
__author__ = "730406932"
from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """the entrypoint of the program and drawing loops. the eyes() function is called twice on lines 10-11. tongue_up() and tongue_down(), formerly being the same function till i broke them up, are called on 15-16"""
    turtle: Turtle = Turtle()
    background(-666, 666, turtle)
    face(0, -300, turtle)
    eyes(125, 75, turtle)
    eyes(-125, 75, turtle)
    nose(-40, 50, turtle)
    mouth(-250, 25, turtle)
    smile(-225, 25, turtle)
    tongue_up(-125, -192.5, turtle)
    tongue_down(125, -192.5, turtle)
    # hair(-150, 300, turtle)
    done()


def background(x: float, y: float, turtle: Turtle) -> None:
    i: int = 225
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(0)
    turtle.goto(x, y)
    turtle.pendown()
    while i >= 10:
        r: int = 0
        turtle.begin_fill()
        while r < 2:
            turtle.color(10, i, 222)
            turtle.forward(2000)
            turtle.right(90)
            turtle.forward(25)
            turtle.right(90)
            r += 1
        turtle.end_fill()
        turtle.right(90)
        turtle.forward(25)
        turtle.seth(0.0)
        i -= 5


def face(x: float, y: float, turtle: Turtle) -> None:
    """the face is a very simple circle. pencolor and fillcolor used here"""
    turtle.begin_fill()
    turtle.pencolor("peachpuff")
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(25)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(300)
    turtle.fillcolor("peachpuff")
    turtle.end_fill()


def eyes(x: float, y: float, turtle: Turtle) -> None:
    """one eyeball, called twice"""
    turtle.begin_fill()
    turtle.pencolor("black")
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(25)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(25)
    turtle.fillcolor("black")
    turtle.end_fill()


def nose(x: float, y: float, turtle: Turtle) -> None:
    """while loop on lines 59-62 to draw a triangle for a nose"""
    i: int = 0
    turtle.begin_fill()
    turtle.pencolor("tomato")
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(25)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("tomato")
    while i < 3:
        turtle.forward(80)
        turtle.left(120)
        i += 1
    turtle.end_fill()


def mouth(x: float, y: float, turtle: Turtle) -> None:
    """big semicircle for a big smile"""
    turtle.hideturtle()
    turtle.pencolor("darkred")
    turtle.penup()
    turtle.speed(25)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(-90)
    turtle.circle(250, 180)
    turtle.fillcolor("darkred")
    turtle.end_fill()


def smile(x: float, y: float, turtle: Turtle) -> None:
    """teef, represented by a rectangle with two rounded corners"""
    turtle.hideturtle()
    turtle.pencolor("white")
    turtle.penup()
    turtle.speed(25)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(-90)
    turtle.forward(450)
    turtle.right(90)
    turtle.forward(45)
    turtle.circle(-5, 90)
    turtle.forward(395)
    turtle.forward(45)
    turtle.circle(-5, 90)
    turtle.fillcolor("white")
    turtle.end_fill()

    
def tongue_up(x: float, y: float, turtle: Turtle) -> None:
    """two semicircles, not hemicircles, for the tongue."""
    # i: int = 0
    # while i < 2:
    #     turtle.hideturtle()
    #     turtle.pencolor("lightcoral")
    #     turtle.penup()
    #     turtle.speed(5)
    #     turtle.goto(x * -1 ** i, y)
    #     turtle.pendown()
    #     turtle.begin_fill()
    #     turtle.right(120 * -1 ** i)
    #     turtle.circle(250, 60)
    #     turtle.fillcolor("lightcoral")
    #     turtle.end_fill()
    #     turtle.penup()
    #     i += 1
    turtle.hideturtle()
    turtle.pencolor("lightcoral")
    turtle.penup()
    turtle.speed(25)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(120)
    turtle.circle(250, 60)
    turtle.fillcolor("lightcoral")
    turtle.end_fill()


def tongue_down(x: float, y: float, turtle: Turtle) -> None:
    """this function used to be combined with  tongue_up() till i realized i had to break up a function, so now there are two functions for the tongue"""
    turtle.hideturtle()
    turtle.pencolor("lightcoral")
    turtle.penup()
    turtle.speed(25)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(-120)
    turtle.circle(250, 60)
    turtle.fillcolor("lightcoral")
    turtle.end_fill()
    turtle.penup()


# def hair(x: float, y: float, turtle: Turtle) -> None:
    """gave up because idek how to draw hair like what does hair even look like"""
#     turtle.begin_fill()
#     turtle.pencolor("black")
#     turtle.hideturtle()
#     turtle.penup()
#     turtle.speed(5)
#     turtle.goto(x, y)
#     turtle.pendown()
#     turtle.circle(100, 180)
#     turtle.fillcolor("black")
#     turtle.end_fill()


"""these below are my lines of code from the tutorial"""
# turtle_object_variable.method_name()
# turtle.forward(50)
# turtle.left(30)
# turtle.right(40)
# turtle.forward(300)
# turtle.left(90)
# turtle.forward(300)
# turtle.left(90)
# turtle.forward(300)
# turtle.left(90)
# turtle.forward(300)
# turtle.left(90)
# i: int = 0
# while (i < 4):
#     turtle.forward(300)
#     turtle.left(90)
#     i = i + 1
# i: int = 0
# while (i < 3):
#     turtle.forward(300)
#     turtle.left(120)
#     i = i + 1
# turtle.color("blue")
# turtle.color(99, 204, 250)
# turtle.penup()
# turtle.goto(45, 60)
# turtle.pendown()
# turtle.speed(10)
# turtle.hideturtle()
# turtle.begin_fill()
# turtle.begin_fill()
# turtle.fillcolor(32, 67, 93)
# # code for shape to be filled 
# turtle.pencolor("pink")
# turtle.color("green", "yellow")
# turtle.fillcolor("black")
# turtle.penup()
# turtle.goto(45, 60)
# turtle.pendown()
# # turtle.speed(10)
# side_length: float = 300.0
# i: int = 0
# while (i < 3):
#     side_length = side_length * 0.97
#     turtle.forward(side_length)
#     turtle.left(120)
#     i = i + 1
# while (i < 3):
#     turtle.forward(300)
#     turtle.left(123)
#     i = i + 1
# turtle.end_fill()
# turtle.end_fill()


if __name__ == "__main__":
    main()