#Pong tutorial by @TokyoEdTech
#Expanded to triple pong by myself(Harry)

import  turtle

wn = turtle.Screen()
wn.title("Triple Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Main game loop
while True:
    wn.update()
