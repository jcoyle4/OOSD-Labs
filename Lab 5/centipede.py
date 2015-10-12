from turtle import *
"""
Explaination in the Pukka Pad
"""

def centipede(length, step, life):
    #penup()              #stops the centipede leaving a trace
    theta = 5            #Initial rotation
    dtheta = 5          #How much to change the rotation by

    for i in range(life):
        forward(step)    #Move the centipede forward by indicated distance
        left(theta)      #Rotate the centipede
        theta += dtheta  #Update the rotation
        stamp()          #gives the centipede a tail
        """
        if i > length:
            clearstamps(1)  #delete the end of the centipede tail if it gets too long, higher the argument, shorter the tail
        """
        if theta > 50 or theta < -50:
            dtheta = -dtheta  #if theta goes outside a certain range, go from left to right
        if ycor() > 300 or ycor() < -300:  #The next four lines are boundry conditions
            left(45)
        if xcor() > 300 or xcor() < -300:
            right(45)

def main():
    setworldcoordinates(-400, -400, 400, 400) #how big the centipedes "world" is
    centipede(5, 10, 200)    #set up its lenght, how bit it steps, and how long it survives
    exitonclick() #Exits the window when clicked upon and the life is exceeded

main()