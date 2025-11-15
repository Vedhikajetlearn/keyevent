import pgzrun, random
WIDTH,HEIGHT=800,500
TITLE="Catch it!"
minion=Actor("minion.webp")
minion.pos=(random.randint(0,800),random.randint(0,500))
evilminion=Actor("evil minion.webp")
evilminion.pos=(random.randint(0,800),random.randint(0,500))
score=0
message="Catch the minion"
def draw():
    screen.clear()
    minion.draw()
    evilminion.draw()
    screen.draw.text(message,(10,10))
    screen.draw.text("score:"+str(score),(10,30))
    
def on_mouse_down(pos):
    global score,message
    print(pos)
    if minion.collidepoint(pos):
        score+=10
        message="Yes, you caught it!"
    elif evilminion.collidepoint(pos):
        score-=10
        message="You caught the the wrong one!"
    else:
        message="Oops, you missed both.:("
    minion.pos=(random.randint(0,800),random.randint(0,500))
    evilminion.pos=(random.randint(0,800),random.randint(0,500))
pgzrun.go()