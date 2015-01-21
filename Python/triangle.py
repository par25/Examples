# PRtriangle2.py
# by Mrs. Redding

from graphics import *

def main():
   win = GraphWin("Draw a Triangle",500,500)
   win.setCoords(0.0,0.0,10.0,10.0)
   message = Text(Point(5,0.5),"Click on three points")
   message.setSize(18)
   message.draw(win)
   
   # Get and draw three vertices of triangle
   p1 = win.getMouse()
   p1.draw(win)
   p2 = win.getMouse()
   p2.draw(win)
   p3 = win.getMouse()
   p3.draw(win)
   
   # Delete the text message
   message.undraw()
   
   # Use Polygon object to draw the triangle
   triangle = Polygon(p1,p2,p3)
   triangle.setFill(color_rgb(50,100,200))
   triangle.setWidth(15)
   triangle.setOutline("green")
   triangle.draw(win)
   
   message.setText("Click anywhere to quit.")
   win.getMouse()
   
main()
