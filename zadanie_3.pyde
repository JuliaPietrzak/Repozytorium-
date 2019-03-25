def setup():
    size (400,400)
    textSize(70)
def draw():
    background (10,50,150)
    text("J", width/2-25, height/2)
    text("P", width/2+25, height/2)
    fill(100,0,15)
    if keyPressed:                                #zmiana koloru po wciśnieciu "j" 
        fill(100,0,15)
        if key=='j' or key=='J':
            fill(0,100,10)
            text("J", width/2-25, height/2)
            fill(100,0,15)
    if keyPressed:                                #zmiana koloru po wciśnięciu "p"
        fill(100,0,15)
        if key=='p'or key== 'P':   
            fill(0,100,10)
            text("P", width/2+25, height/2)
            fill(100,0,15)                         
                  
    if (mouseX >= 170 and mouseX <=190):         #najechanie myszą na J (ciemniejszy kolor), kliknięcie strzałki w prawo, zmiana koloru P
        fill(80, 0, 30)
        text("J", width/2-25, height/2)
        fill(100,0,15)
        if keyPressed:   
            if keyCode==39:
                fill(0,200,0)
                text("P", width/2+25, height/2)
                fill(0,200,0)   
            
    if (mouseX >= 220 and mouseX <=250):         ##najechanie myszą na P (ciemniejszy kolor), kliknięcie strzałki w lewo, zmiana koloru J
        fill(80, 0, 30)
        text("P", width/2+25, height/2)
        fill(100,0,15)
        if keyPressed:   
            if keyCode==37:
                fill(0,200,0)
                text("J", width/2-25, height/2)
                  
        
    s = createShape()                               #nieregularny kształt- podkreślenie
    s.beginShape()
    s.fill(204, 102, 0)
    s.vertex(10, height/3*2)
    s.vertex(15, height/2)
    s.vertex(width/2, height/3*2)
    s.vertex(width-100, height/3*2+20)
    s.vertex(width-150, height/3*2)
    s.endShape(CLOSE)
    shape(s, 25, 25)
