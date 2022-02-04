from turtle import *

def drawSquare(sideLength):
    pendown()
    forward(sideLength)
    right(90)
    forward(sideLength)
    right(90)
    forward(sideLength)
    right(90)
    forward(sideLength)
    penup()

def main():
  number1 = input("Please enter a number between 10 and 50: ")
  number2 = input("Enter a second number that is the multiple of the first: ")
  drawSquare(number1)
  goto(200,200)
  drawSquare(number2)

  done()

main()
