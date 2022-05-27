import random
add_library('minim')
def setup():
    minim = Minim(this)
    global Cactus_1,Cacti_1,Cacti_2,Cacti_3,trex_Extinct # Sprite image assets
    global jump_mp3 # Sound effects / music / mp3 audio assets
    size(800,400)
    Cactus_1 = loadImage("Cactus_1.png")
    Cacti_1 = loadImage("Cacti_1.png")
    Cacti_2 = loadImage("Cacti_2.png")
    Cacti_3 = loadImage("Cacti_3.png")
    trex_Extinct = loadImage("Trex_Extinct.png")
    jump_mp3 = minim.loadFile("TrexJumped.mp3")
    #_____________________________________________________________________________________
    global status
    status = 0 #0 = menu, 1 = in-game, 2 = Instructions, 3 = Death screen
    global play_hover_status
    play_hover_status = 0
    global mb_w1 #Main menu play button width
    mb_w1 = 6.4
    global mb_h1 #Main menu play button height
    mb_h1 = 9
    global mb_w2 #Main menu Help button width
    mb_w2 = 6.4
    global mb_h2 #Main menu Help button height
    mb_h2 = 9
    global ib_w #Instructions page back button width
    ib_w = 6.4
    global ib_h #Instructions page back button height
    ib_h = 9
    global mb1_x #Play button X position
    mb1_x = 640-622  
    global mb1_y #Play button Y position
    mb1_y = 175
    global mb2_x #Help button X position
    mb2_x = 640-622
    global mb2_y #Help button Y position
    mb2_y = 225
    global restartHoverStatus # Restart Button hover status
    restartHoverStatus = 0 # 0 = No Hover, 1 = Hover
frame,time,Running=1,0,True
placements,placements2,placements3 = [1000,2000,2500],[4500,4900,5000],[5500,5900,6000]
h = 200
Run_animation = loadImage("Trex_Run1.png")
fall = False
timer = False
Speed = 8
pkey = -1
key1,key2,key3,key4 = 0,0,0,0
X,XX,XXX,XXXX = 1000,2000,3000,4000
score = [0,0,0,0,0,0,0]
score_number = 0
score_value0 , score_value1, score_value2, score_value3, score_value4,score_value5,score_value6=0,0,0,0,0,0,0
textdisplay = 0
time2 = 0
t = 255
Speed_Cap = False
gravity = 0
def draw():
    background(0,0)
    global status,restartHoverStatus,frame,time,Cactus_1,placements,placements2,placements3,Running,h,Run_animation,fall,timer,time2,Speed,pkey,Cacti_1,Cacti_2,Cacti_3,key1,key2,key3,key4,X,XX,XXX,XXXX,score,score_number,score_value0 , score_value1, score_value2, score_value3, score_value4,score_value5,score_value6,textdisplay,trex_Extinct,t,gravity,Speed_Cap
    ###############################################
    global img_logo, img_playbutton, img_helpbutton, img_howtoplaytitle, logob_w, logob_h, Cacti_3, img_floor #Image Assets UI
    global mb_w1, mb_w2, mb_h1, mb_h2, mb1_x, mb1_y, ib_w, ib_h #Coordinate variables
    global jump_mp3 #Audio assets
    if (status == 0): #Main Menu
        X,XX,XXX,XXXX = 1000,2000,3000,4000
        score = [0,0,0,0,0,0,0]
        t = 255
        score_number = 0
        Speed = 8
        noTint()
        img_stars = loadImage("Trex_Stars.png")
        image(img_stars, 0, 0)
        img_moon = loadImage("Trex_moon.png")
        image(img_moon, 650, 20, width / 8, height / 4)
        img_logo = loadImage("Trex.png")
        image(img_logo, 15, -20, width / 4, height / 2)
        img_playbutton = loadImage("Trex_Play (1).png")
        image(img_playbutton, mb1_x, mb1_y, width / mb_w1, height / mb_h1)
        img_helpbutton = loadImage("Trex_Play (2).png")
        image(img_helpbutton, mb2_x, mb2_y, width / mb_w2, height / mb_h2)
        fill(117, 117, 117)
        rect(0,285,800,200)
        tint(17, 102, 0)
        image(Cacti_3, 500, 200)
        noTint()
        img_floor = loadImage("TrexgameFloor.png")
        image(img_floor, 0, 285)
        img_menutrex = loadImage("Trex_Home_Jump.png")
        image(img_menutrex, 200, 200)
        tint(255,180)
        
        
             
    elif status == 1: #In-game
        KEY = key
        if Running == True:
            time += 1
            if time >=10:
                frame += 1
                time = 0
            noTint()
            w ="Trex_Run"+str(frame)+".png"
            Run_animation = loadImage(w)
            image(Run_animation,10,200)
            if frame > 2:
                frame = 1     
    #________________________________________________________________
        X -= Speed
        XX -= Speed
        XXX -= Speed
        # XXXX -= Speed
        noTint()
        image(Cactus_1,X,200)
        image(Cacti_1,XX,200)
        image(Cacti_2,XXX,200)
        img_floor2 = loadImage("TrexgameFloor.png")
        image(img_floor2, 0, 285)
        # image(Cacti_3,XXXX,200)
        if X <= -100:
            key1 = random.randint(0,2)
            X = placements[key1]
        if XX <= -100:
            key2 = random.randint(0,2)
            XX = placements2[key2]
        if XXX <= -100:
            key3 = random.randint(0,2)
            XXX =placements3[key3]
        if XX - X <= 500 and XX - X >= 0 or XX - X >= -500 and XX-X <=0:
            XX = XX + 100
        if XXX - X <= 500 and XXX - X >= 0 or XXX - X >= -500 and XXX-X <=0:
            XXX = XXX +100 
        if XXX - XX <= 500 and XXX - XX >= 0 or XXX - XX >= -500 and XXX-XX <=0:
            XXX = XXX + 100

    #_______________________________________________________________
        if timer == True:
            Running = False
            if fall == False:
                if h <= 200 and h >= 10:
                    for i in range (1,60):
                        gravity -= 0.0001
                        h -= gravity
                image(Run_animation,10,h)
            if h <= 10:        
                fall = True
                gravity = 0.03
            if fall == True:
                if h <= 200:
                    for i in range (1,50):
                        gravity += 0.0002
                        h += gravity
                if h >=200:
                    KEY = "s"
                    Running = True
                    timer = False
                    h = 200
                    fall = False
                image(Run_animation,10,h)

    
            
        if keyPressed == True:
            if key == 'w':
                gravity = 0.190
                timer = True
                jump_mp3.play()
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
        f = loadFont("OCRAExtended-40.vlw")
        textFont(f)
        textSize(30)
        textdisplay = str(score[0])+str(score[1])+str(score[2]) +str(score[3]) + str(score[4])+str(score[5]) + str(score[6])
        text(textdisplay,350,30)
    #_________________________________________________________________________________________
        time2 +=1
        while Speed_Cap == False:
            if time2 > 50:
                Speed += 0.1
                time2 = 0
       
    
    #_________________________________________________________________________________
        if X < 80 or XX < 80 or XXX < 80 or XXXX < 80:
            if h > 172:
                status = 3
    elif (status == 2): #Instructions
        noTint()
        img_backbutton = loadImage("Trex_Back.png")
        image(img_backbutton, 15, 24, width / ib_w, height / ib_h)
        img_howtoplaytitle = loadImage("Trex_HTPtitle.png")
        image(img_howtoplaytitle, 250, 20, width / 2.5, height / 7.5)
        img_howtoplaytext = loadImage("Trex_InstructionsText.png")
        image(img_howtoplaytext, 0, 20)
        
    elif (status == 3): #game-over
        t -= 2
        tint(255,t)
        image(trex_Extinct,10,h)
        tint(255,255)
        image(Cactus_1,X,200)
        image(Cacti_1,XX,200)
        image(Cacti_2,XXX,200)
        image(img_floor,0,285)
        if (t <= 0):
            noTint()
            img_gameovertitle = loadImage("Trex_gameover.png")
            image(img_gameovertitle, 240, 100, width / 2.5, height / 9)
            fill(255,255,255)
            f = loadFont("OCRAExtended-40.vlw")
            textFont(f)
            textSize(20)
            textdisplay = str(score[0])+str(score[1])+str(score[2]) +str(score[3]) + str(score[4])+str(score[5]) + str(score[6])
            text('Final score: ' + textdisplay,280,180)
            if (restartHoverStatus == 0):
                img_restart = loadImage("Restart.png")
                image(img_restart,367,200, width / 12, height / 6)
            else:
                img_restartH = loadImage("Restarthover.png")
                image(img_restartH,367,200, width / 12, height / 6)
            
        
def mousePressed():
    global status
    println(str(mouseX) + ',' + str(mouseY))
    if (status == 0):
        if ((mouseX > 642-622 and mouseX < 763-622) and (mouseY > 175 and mouseY < 222)):
            status = 1
        elif ((mouseX > 641-622 and mouseX < 763-622) and (mouseY > 225 and mouseY < 266)):
            status = 2
    elif (status == 2):
        if ((mouseX > 10 and mouseX < 130) and (mouseY > 351-330 and mouseY < 392-330)):
            status = 0
    elif (status == 3):
        if ((mouseX > 368 and mouseX < 429) and (mouseY > 201 and mouseY < 265)):
            status = 0

def mouseMoved():
    global status, restartHoverStatus
    global mb_w1, mb_w2, mb_h1, mb_h2, ib_w, ib_h
    if (status == 0):
        if ((mouseX > 642-622 and mouseX < 763-622) and (mouseY > 175 and mouseY < 222)):
            mb_w1 = 6
            mb_h1 = 8.65
        elif ((mouseX > 641-622 and mouseX < 763-622) and (mouseY > 225 and mouseY < 266)):
            mb_w2 = 6
            mb_h2 = 8.65
        else: 
            mb_w1 = 6.4
            mb_h1 = 9
            mb_w2 = 6.4
            mb_h2 = 9
    if (status == 2):
        if ((mouseX > 10+5 and mouseX < 130+5) and (mouseY > 351-330 and mouseY < 392-330)):
            ib_w = 6
            ib_h = 8.65
        else:
            ib_w = 6.4
            ib_h = 9
    if (status == 3):
        if ((mouseX > 368 and mouseX < 429) and (mouseY > 201 and mouseY < 265)):
            restartHoverStatus = 1
        else:
            restartHoverStatus = 0
#_________________________________________________
#_________________________________________________Speed cap
    if Speed >= 12.6:
        Speed_cap = True
        print("ok")
