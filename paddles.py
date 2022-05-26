import turtle
import time

wn = turtle.Screen()
wn.title("First try!")
wn.bgcolor("black")
wn.setup(800, 600)
wn.tracer(0)


#Paddle A

class Paddle:
  def __init__(self, name):
      self.name = name
  def setPaddle(self):
      self.name = turtle.Turtle()
      self.name.speed(0)
      self.name.shape("square")
      self.name.shapesize(stretch_wid=5, stretch_len=1) 
      self.name.color("white")
      self.name.penup()
  def positionPaddle(self, x):
      self.name.goto(x, 0)
  def movePaddleUp(self):
      y = self.name.ycor()
      y += 20
      self.name.sety(y)
      if self.name.ycor() > 250:
          self.name.sety(250)
  def movePaddleDown(self):
      y = self.name.ycor()
      y -= 20
      self.name.sety(y)
      if self.name.ycor() < -250:
          self.name.sety(-250)
      
      
class Ball:
  def __init__(self, name):
      self.name = name
  def setBall(self):
      self.name = turtle.Turtle()
      self.name.shape("square")
      self.name.color("white")
      self.name.penup()
      self.name.goto(0, 0)
  
      

pA = Paddle("paddle_a")
pB = Paddle("paddle_b")

pA.setPaddle()
pA.positionPaddle(350)
pB.setPaddle()
pB.positionPaddle(-350)
ball = Ball("lopta")
ball.setBall()


wn.listen()
wn.onkeypress(pA.movePaddleUp, "w")
wn.onkeypress(pA.movePaddleDown, "s")
wn.onkeypress(pB.movePaddleUp, "Up")
wn.onkeypress(pB.movePaddleDown, "Down")

dx = 0.2
dy = 0.2
aScore = 0
bScore = 0

while True:
    wn.update()
    ball.name.setx(ball.name.xcor() + dx)
    ball.name.sety(ball.name.ycor() + dy)
    if ball.name.ycor() > 290:
        ball.name.sety(290)
        dy *= -1
    if ball.name.ycor() < -290:
        ball.name.sety(-290)
        dy *= -1    
    if ball.name.xcor() > 390:
        ball.name.goto(0, 0)
        dx *= -1 
        aScore += 1

    if ball.name.xcor() < -390:
        ball.name.goto(0, 0)
        dx *= -1
        bScore += 1
    if ball.name.xcor() > 330 and pA.name.ycor() < (ball.name.ycor() + 20) and pA.name.ycor() > (ball.name.ycor() - 20):
        ball.name.setx(330)
        dx *= -1   
    if ball.name.xcor() < -330 and pB.name.ycor() < (ball.name.ycor() + 20) and pB.name.ycor() > (ball.name.ycor() - 20):
        ball.name.setx(-330)
        dx *= -1   
    if aScore == 10 or bScore == 10:
        break
print("The game is over." "Left player: ", bScore, "Right player: ", aScore)
if aScore > bScore:
    print("Right player wins!")
else:
    print("Left player wins!")

    
    

