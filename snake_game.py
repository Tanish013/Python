import turtle as t
import random as rd
import time as ti

t.bgcolor('yellow')
catterpillar = t.Turtle()
catterpillar.shape('square')
catterpillar.speed(0)
catterpillar.penup()
catterpillar.hideturtle()

leaf = t.Turtle()
# apple_shape=((0,0),(12,2),(12,4),(0,6),(4,12),(2,12))
# t.register_shape('apple',apple_shape)
# leaf.shape('apple')
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.speed()
leaf.hideturtle()


game_strt = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start',align='center',font=('Aerial',25,'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)




def outside_window():
    l_wall = -t.window_width() / 2
    r_wall = t.window_width() /2
    t_wall = t.window_height() /2
    b_wall = -t.window_height() /2
    (x,y) = catterpillar.pos()
    out_snake = x < l_wall or x > r_wall or y > t_wall or y< b_wall
    return out_snake

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def game_over():
    catterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER !',align='center',font=['Aerial',30,'normal'])


def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 50
    y = (t.window_height()/2) - 50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score),align='right',font=('Aerial',30,'bold'))


def start_game():
    global game_strt
    if game_strt:
        return
    game_strt = True
    score = 0
    text_turtle.clear()

    catterpillar_speed = 2
    catterpillar_length = 3
    catterpillar.shapesize(1,catterpillar_length,1)
    catterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        catterpillar.forward(catterpillar_speed)
        if catterpillar.distance(leaf) < 20:
            place_leaf()
            catterpillar_length = catterpillar_length + 1
            catterpillar.shapesize(1,catterpillar_length,1)
            catterpillar_speed = catterpillar_speed + 0.5
            score = score + 1
            display_score(score)
        if outside_window():
            game_over()
            break


def move_up():
    if catterpillar.heading() == 0 or catterpillar.heading()==180:
        catterpillar.setheading(90)

def move_down():
    if catterpillar.heading() == 0 or catterpillar.heading()==180:
        catterpillar.setheading(270)

def move_left():
    if catterpillar.heading() == 90 or catterpillar.heading()==270:
        catterpillar.setheading(180)

def move_right():
    if catterpillar.heading() == 90 or catterpillar.heading()==270:
        catterpillar.setheading(0)






t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_down,'Down')
t.onkey(move_right,'Right')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()
