import random
def setup():
    global Cactus_1
    size(800,400)
    Cactus_1 = loadImage("Cactus_1.png")
    
frame,time,X,key1,Running=1,0,0,0,True
placements = [1000,1500,1800]
h = 200
Run_animation = loadImage("Trex_Run1.png")
fall = False
timer = False


def draw():
    background(0,0)
    global frame,time,Cactus_1,X,placements,Running,h,Run_animation,fall,timer
    KEY = key
    if Running == True:
        time += 1
        if time >=10:
            frame += 1
            time = 0
        w ="Trex_Run"+str(frame)+".png"
        Run_animation = loadImage(w)
        image(Run_animation,10,200)
        if frame > 2:
            frame = 1
#______________________________________________________________
    fill(255,255,255)
    rect(0,285,800,10)
#________________________________________________________________
    X -= 1
    image(Cactus_1,X,200)
    if X <= -50:
        key1 = random.randint(0,2)
        X = placements[key1]

#_______________________________________________________________
    if timer == True:
        Running = False
        if fall == False:
            if h <= 200 and h >= 10:
                for i in range (1,50):
                    h -= .125
            image(Run_animation,10,h)
        if h <= 10:        
            fall = True
        if fall == True:
            if h <= 200:
                for i in range (1,50):
                    h += .125
            if h >=200:
                KEY = "s"
                Running = True
                timer = False
                h = 200
                fall = False
            image(Run_animation,10,h)


#_____________________________________________________________
    if Running == True:
        fall == False
#_____________________________________________________________
    if keyPressed == True:
        timer = True
#_____________________________________________________________
    print(timer)
