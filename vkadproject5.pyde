x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
x8=0
x9=0
x10=0
x11=0
x12=0
x13=0



def setup():
    size(800,600)
    for i in range (100,700,110):
        rect(i,50,100,100)
    for i in range (100,700,90):
        rect(i,200,80,80)
  

    
def draw():
    
    global x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13
    textSize(20)
    fill(0)
    text("Podskazka: eto yazyk",20,20)
    text("Podskazka: eto kryg",20,190)
    textSize(70)
    fill(255)
    if x2==1 and x3==1 and x4==1 and x5==1 and x6==1 and x7==1 and x8==1 and x9==1 and x10==1 and x11==1 and x12==1 and x13==1:
        textSize(65)
        fill(mouseX,mouseY,150)
        text("YPOBEHb okonchen!", 100,400)
        fill(255)
        textSize(70)
    if keyPressed:
        if key == "P" or key == "p":
            if x2==0:
                fill(0,100,0)
                rect(100,50,100,100)
                fill(0)
                text("P",120,120)
                x2+=1
                if x3==0:
                    fill(0,100,0)
                    rect(460,200,80,80)
                    fill(0)
                    text("p",470,255)
                    x3+=1
 

        elif key == "Y" or key == "y":
            if x4==0:
                fill(0,100,0)
                rect(210,50,100,100)
                fill(0)
                text("y",220,125)
                x4+=1

        elif key == "t" or key == "T":
            if x5==0:
                fill(0,100,0)
                rect(320,50,100,100)
                fill(0)
                text("t",330,125)
                x5+=1
        elif key == "H" or key == "h":
            if x6==0:
                fill(0,100,0)
                rect(430,50,100,100)
                fill(0)
                text("h",440,125)
                x6+=1
            
        elif key == "O" or key == "o":
            if x7==0:
                fill(0,100,0)
                rect(540,50,100,100)
                fill(0)
                text("o",560,125)
                x7+=1

        elif key == "n" or key == "N":
            if x8==0:
                fill(0,100,0)
                rect(650,50,100,100)
                fill(0)
                text("n",670,125)
                x8+=1
   
   
   


        elif key == "e" or key == "E":
            if x9==0:
                fill(0,100,0)
                rect(100,200,80,80)
                fill(0)
                text("E",120,265)
                x9+=1
                if x10==0:
                    fill(0,100,0)
                    rect(640,200,80,80)
                    fill(0)
                    text("e",660,265)
                    x10+=1

        elif key == "l" or key == "L":
            if x11==0:
                fill(0,100,0)
                rect(190,200,80,80)
                fill(0)
                text("l",220,265)
                fill(0,100,0)
                rect(280,200,80,80)
                fill(0)
                text("l",300,265)
                x11+=1

        elif key == "i" or key == "I":
            if x12==0:
                
                fill(0,100,0)
                rect(370,200,80,80)
                fill(0)
                text("i",400,265)
                x12+=1


        elif key == "s" or key == "S":
            if x13==0:
                fill(0,100,0)
                rect(550,200,80,80)
                fill(0)
                text("s",560,265)
                x13+=1
    
    
