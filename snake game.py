
#SNAKE GAME
import turtle
import random
import time
delay=0.1
sc=0
hs=0
bodies=[]
#creating screen point snake
s=turtle.Screen()
s.title("SNAKE GAME")
s.bgcolor("light blue")
s.setup(width=300,height=400)
#creating head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.fillcolor("pink")
head.penup()
head.goto(0,0)
head.direction="stop"
#creating food for snake
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("pink")
food.fillcolor("orange")
food.penup()
food.ht()     #it is use for hide of going
food.goto(200,200)
food.st()     #it show turtle
#creating score board
sb=turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-200,100)
sb.write("score:0  |   Hieght score:0") 
#creating function for moving in all direction
def moveUp():
    if head.direction!="down":
        head.direction="up"
def moveDown():
    if head.direction!="up":
        head.direction="down"
def moveLeft():
    if head.direction!="right":
        head.direction="left"
def moveRight():
    if head.direction!="left":
        head.direction="right"
def moveStop():
        head.direction="stop"
#moving the snake 
def move():
    if head.direction=="up":#snake moving at upside
        y=head.ycor()#y+ codinate
        head.sety(y+20)#moving snake 20 in +y direction
    if head.direction=="left":#snake moving at upside
        x=head.xcor()#-x codinate
        head.setx(x-20)#moving snake 20 in -x direction
    if head.direction=="down":#snake moving at upside
        y=head.ycor()#y- codinate
        head.sety(y-20)#moving snake 20 in -y direction
    if head.direction=="right":#snake moving at upside
        x=head.xcor()#x+ codinate
        head.setx(x+20)#moving snake 20 in x+ direction
#event handing action
s.listen()
s.onkey(moveUp,"Up")#moveup is take from def moveup
s.onkey(moveDown,"Down")#movedown is take from def movedown
s.onkey(moveLeft,"Left")#moveleft is take from def moveleft
s.onkey(moveRight,"Right")#moveright is take from def moveright
s.onkey(moveStop,"space")#movestop is take from def movestop
#mainloop
while True:
    s.update()#to update the screen
    #check collision with border
    if head.xcor()>290:#head take from above side xcordinate mean less then 290 in left side
        head.setx(-290)#come in right side from staring
    if head.xcor()<-290:#head take from above side xcordinate mean less then 290 in right side
        head.setx(290)#come in left side from staring
    if head.ycor()>290:#head take from above side xcordinate mean less then 290 in up side
        head.sety(-290)#come in up side from staring
    if head.ycor()<-290:#head take from above side xcordinate mean less then 290 in bottom side
        head.sety(290)#come in right side from starting
        #check collision with food
    if head.distance(food)<20:#if snake come near food till 19
        x=random.randint(-290,290)#it change automatic place between screen both side of x
        y=random.randint(-290,290)#it change automatic place between screen both side of y
        food.goto(x,y)# go to x,y any side between -290,290=x -290,290=y
        #increase the body of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)#append the new body in list or snake
        #increase the score
        sc=sc+100
        delay=delay-0.001#increse the speed
        #update the hieght score
        if sc>hs:
            hs=sc #update hieght score
        sb.clear()#clear old record of score
        sb.write("Score:{} | Highest Score:{}".format(sc,hs))
    #move snake bodies
    for i in range(len(bodies)-1,0,-1):#find len of snake loop
        x=bodies[i-1].xcor()
        y=bodies[i-1].ycor()
        bodies[i].goto(x,y) #move snake with take all body
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)#move with snake body
    move()
#check collision with snake body,,,touch snake body to itself
    for body in bodies:
        if body.distance(head)<20:#if snake near to body thier body
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            #hide bodies
            for body in bodies:
                 body.ht()# it use to hide body
            bodies.clear()
            sc=0
            delay=0.1#again delay same
            sb.clear()#starting board score clear
            sb.write("Score:{} | highest Score:{}".format(sc,hs))
    time.sleep(delay)
s.mainloop()
                
                 
                 
                 
        

        
    
