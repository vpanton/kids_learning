from turtle import *
import time

bg_image = "bgfield.gif"
hero_image = "luntic.gif"
textbg_image = "textbg.gif"
text_image = "empty.gif"

def nv_screen(bg_image, hero_image, text_s, sleeptime=5):
    # add the shape first then set the turtle shape
    screen = Screen()
    screen.setup(600,400)
    screen.bgpic(bg_image)
    screen.addshape(hero_image)
    screen.addshape(textbg_image)
    screen.addshape(text_image)
    hero = Turtle(shape=hero_image)
    hero.penup()
    textbg = Turtle(shape=textbg_image)
    textbg.penup()
    textbg.goto(x=0,y=-150)
    text = Turtle(shape=text_image)
    text.penup()
    text.goto(x=0,y=-135)
    text.write(text_s, True, align="center", font=("Arial", 20, "normal"))
    time.sleep(sleeptime)


nv_screen(bg_image, hero_image, "Привет", 1)
nv_screen(bg_image, hero_image, "Привет2", 1)
nv_screen(bg_image, hero_image, "Привет3", 1)
nv_screen(bg_image, hero_image, "Привет4", 1)

#Screen.mainloop() # start everything running
