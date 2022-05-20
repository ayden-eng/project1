import random
def setup():
    global Cactus_1
    size(800,400)
    Cactus_1 = loadImage("Cactus_1.png")
    
frame,time,X,key1,Running=1,0,0,0,True
placements = [1000,1500,1800,2000,2500,2800,3000]
h = 200
Run_animation = loadImage("Trex_Run1.png")
fall = False
timer = False
Speed = 10
pkey = -1
def draw():
    background(0,0)
    global frame,time,Cactus_1,X,placements,Running,h,Run_animation,fall,timer,Speed,key1,pkey
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
    X -= Speed
    image(Cactus_1,X,200)
    if X <= -50:
        key1 = random.randint(0,6)
        X = placements[key1]
        key1 = pkey
        key1 = random.randint(0,6)
        if key1 = pkey:
            
        key


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


        
    if keyPressed == True:
        if key == 'w':
            timer = True
#_____________________________________________________________
    print(key1)
