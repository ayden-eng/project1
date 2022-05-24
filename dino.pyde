import random
def setup():
    global Cactus_1,Cacti_1,Cacti_2,Cacti_3
    size(800,400)
    Cactus_1 = loadImage("Cactus_1.png")
    Cacti_1 = loadImage("Cacti_1.png")
    Cacti_2 = loadImage("Cacti_2.png")
    Cacti_3 = loadImage("Cacti_3.png")
frame,time,Running=1,0,True
placements = [1000,1500,2100,2000,2800,3100,3400]
h = 200
Run_animation = loadImage("Trex_Run1.png")
fall = False
timer = False
Speed = 1
pkey = -1
key1,key2,key3,key4 = 0,0,0,0
X,XX,XXX,XXXX = 0,0,0,0
score = [0,0,0,0,0,0,0]
score_number = 0
score_value0 , score_value1, score_value2, score_value3, score_value4,score_value5,score_value6=0,0,0,0,0,0,0
textdisplay = 0
time2 = 0
def draw():
    background(0,0)
    global frame,time,Cactus_1,placements,Running,h,Run_animation,fall,timer,time2,Speed,pkey,Cacti_1,Cacti_2,Cacti_3,key1,key2,key3,key4,X,XX,XXX,XXXX,score,score_number,score_value0 , score_value1, score_value2, score_value3, score_value4,score_value5,score_value6,textdisplay
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
    XX -= Speed
    XXX -= Speed
    XXXX -= Speed
    image(Cactus_1,X,200)
    image(Cacti_1,XX,200)
    image(Cacti_2,XXX,200)
    image(Cacti_3,XXXX,200)
    if X <= -50:
        key1 = random.randint(0,6)
        X = placements[key1]
    if XX <= -50:
        key2 =random.randint(0,6)
        if key2 == key1:
            key2 =random.randint(0,6)
        XX = placements[key2]
    if XXX <= -50:
        key3 =random.randint(0,6)
        if key3 == key1 or key3 == key2:
            key3 =random.randint(0,6)
        XXX = placements[key3]
    if XXXX <= -50:
        key4 =random.randint(0,6)
        if key4 == key1 or key4 == key2 or key4 == key1:
            key4 =random.randint(0,6)
        XXX = placements[key4]
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
                    h += .09
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
    score_number += 0.1
    if score_number >= 1:
        score_number = 0
        score_value0 += 1
        score[6] += score_value0 - (score_value0 -1)
    if score_value0 > 9:
        score_value0 = 0
        score[6] = 0
        score_value1 += 1
        score[5] += score_value1 - (score_value1 -1)
    if score_value1 > 9:
        score_value1 = 0
        score[5] = 0
        score_value2 += 1
        score[4] += score_value2 - (score_value2 -1)
    if score_value2 > 9:
        score_value2 = 0
        score[4] = 0
        score_value3 += 1
        score[3] += score_value3 - (score_value3 -1)
    if score_value3 > 9:
        score_value3 = 0
        score[3] = 0
        score_value4 += 1
        score[2] += score_value4 - (score_value4 -1)
    if score_value4 > 9:
        score_value4 = 0
        score[2] = 0
        score_value5 += 1
        score[1] += score_value5 - (score_value5 -1)
    if score_value5 > 9:
        score_value5 = 0
        score[1] = 0
        score_value6 += 1
        score[0] += score_value6 - (score_value6 -1)
#-----------------------------------------------------------------------------------------
    fill(255,255,255)
    textSize(20)
    textdisplay = str(score[0])+str(score[1])+str(score[2]) +str(score[3]) + str(score[4])+str(score[5]) + str(score[6])
    text(textdisplay,700,20)
#_________________________________________________________________________________________
    time2 +=1
    if time2 >50:
        Speed += 0.1
        time2 = 0
  
#_________________________________________________________________________________\
      if X or XX or XXX or XXXX < 0:
        if h <= 400:
            print("die")
