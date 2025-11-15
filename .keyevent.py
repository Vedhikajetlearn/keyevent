import pgzrun, random, pyautogui
print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()
TITLE="Catch it!"
bee=Actor("bee.png")
bee.pos=(random.randint(0,800),random.randint(0,500))
flower=Actor("flower.png")
flower.pos=(random.randint(0,800),random.randint(0,500))
score=0
message="Catch the flower"

def draw():
    screen.fill("blue")
    screen.blit("garden.png",(0,0))
    bee.draw()
    flower.draw()
def update():
    if keyboard.left:
        bee.x-=20
def on_key_down(key):
    print(key)
    if key==keys.RIGHT:
        bee.x+=20
pgzrun.go()