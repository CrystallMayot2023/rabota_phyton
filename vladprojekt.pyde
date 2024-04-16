
def setup():
    size(800,600)
    for i in range (100,700,110):
        rect(i,50,100,100)
def draw():
    textSize(70)
    if keyPressed:
        if key == "P" or key == "p":
            fill(0,100,0)
            rect(100,50,100,100)
            fill(0)
            text("P",120,120)
        else:
            fill(100,0,0)
            rect(100,50,100,100)
    if keyPressed:
        if key == "h" or key == "H":
            fill(0,100,0)
            rect(210,50,100,100)
            fill(0)
            text("h",230,125)
        else:
            fill(100,0,0)
            rect(210,50,100,100)
    if keyPressed:
        if key == "Y" or key == "y":
            fill(0,100,0)
            rect(320,50,100,100)
            fill(0)
            text("y",340,125)
        else:
            fill(100,0,0)
            rect(320,50,100,100)
    if keyPressed:
        if key == "t" or key == "T":
            fill(0,100,0)
            rect(430,50,100,100)
            fill(0)
            text("t",450,125)
        else:
            fill(100,0,0)
            rect(430,50,100,100)
    if keyPressed:
        if key == "O" or key == "o":
            fill(0,100,0)
            rect(540,50,100,100)
            fill(0)
            text("o",560,125)
        else:
            fill(100,0,0)
            rect(540,50,100,100)
    if keyPressed:
        if key == "n" or key == "N":
            fill(0,100,0)
            rect(650,50,100,100)
            fill(0)
            text("n",670,125)
        else:
            fill(100,0,0)
            rect(650,50,100,100)
