import turtle
from calendar import c
from operator import concat
import datetime
s = turtle.getscreen()
t = turtle.Turtle()
t.right(90)
t.forward(100)
t.left(90)
t.backward(100)
t.clear()
t.reset()

t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()
now = datetime.datetime.now().year
print (now)
now = int(now)

username = input("Please enter your username: ")

new_user = concat (username , "@aws.com")

age = input("Please enter your age: ")
birthyear = int(age) - int(now)
birthyear = abs(birthyear)
mightbe = int(birthyear) -1
if int(age) < 18:
    print("go away")
elif int(age) >= 18:
    print("aws username is: " + new_user)
    print("your age is: " + age )
    print("you were born in: ",  birthyear ," or ", mightbe) 
print("good bye")



