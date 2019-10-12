xpos=0
ypos=0
xVers=+1
yVers=+1
xRac=0
def setup():
    global xpos, ypos
    xpos=10
    ypos=100
    size (900,700)
    background (5, 5, 5)
    fill (0, 255, 0)
    rect (0, 0, 255, 700)
    fill (250, 255, 255)
    rect (220, 0, 255, 700)
    fill (255, 000, 000)
    rect (470, 0, 255, 700)
    
def draw():
    global xpos, ypos, xVers, yVers, xRac
    background (5, 5, 5)

    ellipse(xpos, ypos, 50, 50)
    xpos=xpos+5*xVers
    ypos=ypos+5*yVers

    if xpos>width or xpos<0:
        xVers=xVers*(-1)
        fill(random(0,255),random(0,255),random(0,255))
    
    if ypos>height or ypos<0:
        yVers*=-1
        fill(random(0,255),random(0,255),random(0,255))
        
    rect(xRac,height-25,100,25)
    
def keyPressed():
    
    global xRac

    if (keyCode == RIGHT and xRac<width-100):
        xRac+=20
        
    elif (keyCode == LEFT and xRac>0):
        xRac-=20
        
     
        
        
    

    
        

        
    
        
    
    
    
