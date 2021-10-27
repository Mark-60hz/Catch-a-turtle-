# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spotColor = "red"
spotShape = "square"
spotSize = 5
score = 0
font_setup = ("Arial", 20, "normal")

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spotShape)
spot.turtlesize(spotSize)
spot.fillcolor(spotColor)

score_writer = trtl.Turtle()
score_writer.pu()
score_writer.goto(-180,170)

spot.penup()
#-----game functions--------
def spot_clicked(x,y):
  change_position()
  update_score()

def change_position(size):
  new_xpos = rand.randint(-180,180)
  new_ypos = rand.randint(-140,140)
  colors = ["blue" , "red", "green", "pink"]
  colorcycle = rand.randint(0,3)
  spot.hideturtle()
  spot.fillcolor(colors[colorcycle])
  spot.turtlesize(size)

def change_position():
  new_xpos = rand.randint(-180,180)
  new_ypos = rand.randint(-140,140)
  spot.hideturtle()
  spot.goto(new_xpos,new_ypos)
  spot.showturtle()

def update_score():
  global score 
  score += 1
  print(score)
  score_writer.clear()
  score_writer.write(score, font=font_setup)

#-----events----------------
spot.onclick(spot_clicked)
#-----events----------------
spot.onclick(spot_clicked)
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----countdown writer-----
counter =  trtl.Turtle()
#-----game functions-----
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
#---------events---------
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 

  
  
wn = trtl.Screen()
wn.mainloop()