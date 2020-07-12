import pygame
pygame.init()
#Creating the window for the game
screen_width = 1920
screen_height = 1080
win = pygame.display.set_mode((screen_width,screen_height))

#Naming the window
pygame.display.set_caption('Kipreoi POWER')
#General Graphics
WalkRight = [pygame.image.load('Graphics/Kipreos 1/walk/rightwalk (1).png'),
pygame.image.load('Graphics/Kipreos 1/walk/rightwalk (1).png'),pygame.image.load('Graphics/Kipreos 1/walk/rightwalk (2).png'),
pygame.image.load('Graphics/Kipreos 1/walk/rightwalk (3).png'),pygame.image.load('Graphics/Kipreos 1/walk/rightwalk (4).png'),
pygame.image.load('Graphics/Kipreos 1/walk/rightwalk (5).png'),pygame.image.load('Graphics/Kipreos 1/walk/rightwalk (6).png'),
pygame.image.load('Graphics/Kipreos 1/walk/rightwalk (7).png'),pygame.image.load('Graphics/Kipreos 1/walk/rightwalk (8).png')]
WalkLeft = [pygame.image.load('Graphics/Kipreos 1/walk/leftwalk (1).png'),pygame.image.load('Graphics/Kipreos 1/walk/leftwalk (2).png'),
pygame.image.load('Graphics/Kipreos 1/walk/leftwalk (3).png'),pygame.image.load('Graphics/Kipreos 1/walk/leftwalk (4).png'),
pygame.image.load('Graphics/Kipreos 1/walk/leftwalk (5).png'),pygame.image.load('Graphics/Kipreos 1/walk/leftwalk (6).png'),
pygame.image.load('Graphics/Kipreos 1/walk/leftwalk (7).png'),pygame.image.load('Graphics/Kipreos 1/walk/leftwalk (8).png')]
#Background
bg = pygame.image.load('Graphics/Background/bg1.png')
char = pygame.image.load('Graphics/Kipreos 1/idle/2_terrorist_2_Idle_003.png')

#Character Stats
x=50
y=350
width=40
height = 60
left = False
right = False
walkCount = 0

vel = 10 #Velocity
clock = pygame.time.Clock()
#Juping Variables
isJump = False
jumpCount = 10
def redrawGameWindow():
    global walkCount
    #adding the background
    win.blit(bg, (0,0))
    #if I move withour the next line it will just fill with our square
    #win.fill((0,0,0))
    #creating character
    if walkCount +1 >= 27:
        walkCount = 0
    if left:
        win.blit(WalkLeft[walkCount//3], (x,y))
        walkCount +=1
    elif right:
        win.blit(WalkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        win.blit(char, (x,y))
    #pygame.draw.rect(win,(255,0,0),(x,y,width,height)) #this is to create a rectangle charactetr
    #need to update display in order to work
    pygame.display.update()

    #pygame.quit()
#Main LOOP
run = True
while run:
    clock.tick(60)
    #Making sure the [x] button work. display closing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Moving the character
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and x < screen_width -vel:   #Making the key press and not getting off screen
        x+= vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    if not(isJump):
        ####DONT NEED TO MOVE UP AND DOWN FOR SIDE SCROLLER####
        #if keys[pygame.K_UP] or keys[pygame.K_w] and y > vel:
        #    y -= vel
        #if keys[pygame.K_DOWN] or keys[pygame.K_s] and y < screen_height -vel:
        #    y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2)*0.5 * neg#jump height
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()
