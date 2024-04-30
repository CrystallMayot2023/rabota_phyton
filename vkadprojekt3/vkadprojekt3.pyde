#кординаты в эллипсе поставь!!!!!



def setup():
    size(800,600)
    for i in range (100,700,110):
        rect(i,50,100,100)
    for i in range (100,700,90):
        rect(i,200,80,80)
def draw():
    
    textSize(20)
    fill(0)
    text("Podskazka: eto yazyk",20,20)
    textSize(70)
    fill(255)
    if keyPressed:
        if key == "P" or key == "p":
            fill(0,100,0)
            rect(100,50,100,100)
            fill(0)
            text("P",120,120)
 

        elif key == "Y" or key == "y":
            fill(0,100,0)
            rect(210,50,100,100)
            fill(0)
            text("y",220,125)
            

        elif key == "t" or key == "T":
            fill(0,100,0)
            rect(320,50,100,100)
            fill(0)
            text("t",330,125)
            
        elif key == "h" or key == "H":
            fill(0,100,0)
            rect(430,50,100,100)
            fill(0)
            text("h",440,125)
            
        elif key == "O" or key == "o":
            fill(0,100,0)
            rect(540,50,100,100)
            fill(0)
            text("o",560,125)
 

        elif key == "n" or key == "N":
            fill(0,100,0)
            rect(650,50,100,100)
            fill(0)
            text("n",670,125)
   
   
   
   


        elif key == "e" or key == "E":
            fill(0,100,0)
            rect(100,200,80,80)
            fill(0)
            text("E",120,265)


        elif key == "l" or key == "L":
            fill(0,100,0)
            rect(190,200,80,80)
            fill(0)
            text("l",220,265)
            fill(0,100,0)
            rect(280,200,80,80)
            fill(0)
            text("l",300,265)


        elif key == "i" or key == "I":
            fill(0,100,0)
            rect(430,200,80,80)
            fill(0)
            text("i",200,265)

        elif key == "p" or key == "P":
            fill(0,100,0)
            rect(540,50,100,100)
            fill(0)
            text("p",560,125)


        elif key == "s" or key == "S":
            fill(0,100,0)
            rect(650,200,100,100)
            fill(0)
            text("s",670,125)

        elif key == "e" or key == "E":
            fill(0,100,0)
            rect(650,200,100,100)
            fill(0)
            text("e",670,125)
