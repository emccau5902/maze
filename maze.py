# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()

#To Do: read me

# Window
WIDTH = 1000
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
TITLE = "Mediocre Multiplayer Coin-Get Program"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

#Font
MY_FONT = pygame.font.Font(None, 30)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 150, 40)
BLUE = (0, 0, 200)
PURPLE = (157, 38, 173)
ORANGE = (244, 100, 66)


# Make a player

player =  [180, 110, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

'''p2 stuff'''
player2 =  [420, 110, 25, 25]
player2_vx = 0
player2_vy = 0
player2_speed = 5


#Powerups
speed1 = [200, 600, 25, 25]

speeds = [speed1]

# make walls
wall1 =  [300, 275, 200, 25]
wall2 =  [400, 450, 200, 50]
wall3 =  [100, 20, 25, 750]
wall4 =  [360, 180, 150, 30]
wall5 =  [500, 20, 30, 220]
wall6 =  [300, 180, 20, 270]
wall7 =  [500, 275, 30, 200]
wall8 =  [200, 300, 20, 50]
wall9 =  [150, 350, 150, 20]
wall10 =  [250, 180, 20, 130]
wall11 =  [150, 250, 100, 20]
wall12 =  [100, 180, 150, 30]
wall13 =  [100, 20, 850, 30]
wall14 =  [600, 20, 20, 480]
wall15 =  [200, 500, 420, 20]
wall16 =  [170, 450, 300, 20]
wall17 =  [100, 500, 60, 20]
wall18 =  [350, 350, 150, 20]
wall19 =  [100, 770, 850, 20]
wall20 =  [950, 20, 20, 770]


walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20]

# Make coins
coin1 = [460, 310, 25, 25]
coin2 = [550, 420, 25, 25]
coin3 = [150, 150, 25, 25]
coin4 = [330, 220, 25, 25]
coin5 = [367, 473, 25, 25]

coins = [coin1, coin2, coin3, coin4, coin5]

#Make portal
portal1a = [545, 30, 40, 25]
portal1b = [495, 390, 25, 40]

portals = [portal1a, portal1b]


#other stuff i guess
win1 = False
win2 = False
display_score = True
p1score = 0
p2score = 0
p_time = 0
ticks = 0


# Game loop
done = False


while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_w]
    down = pressed[pygame.K_s]
    left = pressed[pygame.K_a]
    right = pressed[pygame.K_d]

    if up:
        player_vy = -player_speed
    elif down:
        player_vy = player_speed
    else:
        player_vy = 0
        
    if left:
        player_vx = -player_speed
    elif right:
        player_vx = player_speed
    else:
        player_vx = 0

    '''P2 Controls'''
    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    if up:
        player2_vy = -player2_speed
    elif down:
        player2_vy = player2_speed
    else:
        player2_vy = 0
        
    if left:
        player2_vx = -player2_speed
    elif right:
        player2_vx = player2_speed
    else:
        player2_vx = 0

        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player[0] += player_vx

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player, w):        
            if player_vx > 0:
                player[0] = w[0] - player[2]
            elif player_vx < 0:
                player[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player[1] += player_vy
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player, w):                    
            if player_vy > 0:
                player[1] = w[1] - player[3]
            if player_vy < 0:
                player[1] = w[1] + w[3]


    player2[0] += player2_vx

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player2, w):        
            if player2_vx > 0:
                player2[0] = w[0] - player2[2]
            elif player2_vx < 0:
                player2[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player2[1] += player2_vy
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player2, w):                    
            if player2_vy > 0:
                player2[1] = w[1] - player2[3]
            if player2_vy < 0:
                player2[1] = w[1] + w[3]

    ''' here is where you should resolve player collisions with screen edges '''





    ''' get the collectables '''

    powerup = [s for s in speeds if intersects.rect_rect(player, s)]

    for po in powerup:
        p_time = 5
        speeds.remove(po)
        player_speed = 7
    powerup = [s for s in speeds if intersects.rect_rect(player2, s)]

    for po in powerup:
        p_time = 5
        speeds.remove(po)
        player2_speed = 7
    
    hit_list = [c for c in coins if intersects.rect_rect(player, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        p1score += 1
        
    
    hit_list2 = [c for c in coins if intersects.rect_rect(player2, c)]
    
    for h in hit_list2:
        coins.remove(h)
        p2score += 1


    if len(coins) == 0 and p1score > p2score:
        win1 = True
    if len(coins) == 0 and p2score > p1score:
        win2 = True

    '''portal stuff'''
    
    '''horizontal collision'''
    for p in portals:
        if intersects.rect_rect(player, p):
            if player_vx > 0:
                player = [550, 55, 25, 25]
            elif player_vx < 0:
                player = [550, 55, 25, 25]
            

    #550, 55, 25, 25
    #465, 400, 25, 25

    '''vertical collision'''
    for p in portals:
        if intersects.rect_rect(player, p):                    
            if player_vy > 0:
                player = [465, 400, 25, 25]
            if player_vy < 0:
                player = [465, 400, 25, 25]

                
    '''p2 portal stuff'''
    '''horizontal collision'''
    for p in portals:
        if intersects.rect_rect(player2, p):
            if player2_vx > 0:
                player2 = [550, 55, 25, 25]
            elif player2_vx < 0:
                player2 = [550, 55, 25, 25]
            

    #550, 55, 25, 25
    #465, 400, 25, 25

    '''vertical collision'''
    for p in portals:
        if intersects.rect_rect(player2, p):                    
            if player2_vy > 0:
                player2 = [465, 400, 25, 25]
            if player2_vy < 0:
                player2 = [465, 400, 25, 25]


    ''' timer stuff '''
    if done == False:
        ticks += 1

        if ticks % refresh_rate == 0:
            p_time -= 1

        if p_time == 0:
            player_speed = 5
            player2_speed = 5
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, BLUE, player2)
    
    for w in walls:
        pygame.draw.rect(screen, GREEN, w)

    for c in coins:
        pygame.draw.rect(screen, ORANGE, c)
        
    for p in portals:
        pygame.draw.rect(screen, PURPLE, p)

    for s in speeds:
        pygame.draw.ellipse(screen, YELLOW, s)

    ''' timer text '''
    timer_text = MY_FONT.render("Power Up Time: " + str(p_time), True, WHITE)
    if p_time >= 1:
        screen.blit(timer_text, [420, 475])

    
    if display_score:
        scorea = MY_FONT.render("P1 Score: " + str(p1score), 1, RED)
        scoreb = MY_FONT.render("P2 Score: " + str(p2score), 1, BLUE)
        screen.blit(scorea, [130, 55])
        screen.blit(scoreb, [380, 55])
        
    
    
    if win1:
        font = pygame.font.Font(None, 48)
        text = font.render("Player 1 Wins!", 1, WHITE)
        screen.blit(text, [200, 100])
    if win2:
        font = pygame.font.Font(None, 48)
        text = font.render("Player 2 Wins!", 1, WHITE)
        screen.blit(text, [200, 100])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
