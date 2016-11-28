# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 200)
PURPLE = (157, 38, 173)


# Make a player
player =  [200, 150, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

# make walls
wall1 =  [300, 275, 200, 25]
wall2 =  [400, 450, 200, 50]
wall3 =  [100, 20, 25, 500]
wall4 =  [360, 180, 150, 30]
wall5 =  [500, 20, 30, 220]
wall6 =  [300, 180, 20, 270]
wall7 =  [500, 275, 30, 200]
wall8 =  [100, 400, 150, 20]
wall9 =  [150, 350, 150, 20]
wall10 =  [100, 300, 150, 20]
wall11 =  [150, 250, 150, 20]
wall12 =  [100, 180, 150, 30]
wall13 =  [100, 20, 500, 30]
wall14 =  [600, 20, 20, 480]
wall15 =  [100, 510, 520, 20]
wall16 =  [170, 450, 300, 20]
wall17 =  [100, 500, 520, 20]
wall18 =  [350, 350, 150, 20]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall16, wall17, wall18]

# Make coins
coin1 = [460, 310, 25, 25]
coin2 = [550, 420, 25, 25]
coin3 = [150, 150, 25, 25]
coin4 = [330, 220, 25, 25]
coin5 = [367, 473, 25, 25]

coins = [coin1, coin2, coin3, coin4, coin5]

#Make portal
portal1 = [545, 30, 40, 25]
portal2 = [490, 390, 25, 40]

portals = [portal1, portal2]

#Make moving objects

# Game loop
win = False
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


    ''' here is where you should resolve player collisions with screen edges '''





    ''' get the coins '''
    coins = [c for c in coins if not intersects.rect_rect(player, c)]

    if len(coins) == 0:
        win = True


    '''portal stuff'''
    
    '''horizontal collision'''
    for p in portals:
        if intersects.rect_rect(player, p):
            if player_vx > 0:
                player = [550, 55, 25, 25]
            elif player_vx < 0:
                player = [550, 55, 25, 25]
    #465, 400, 25, 25
    #550, 55, 25, 25

    '''vertical collision'''
    for p in portals:
        if intersects.rect_rect(player, p):                    
            if player_vy > 0:
                player = [465, 400, 25, 25]
            if player_vy < 0:
                player = [465, 400, 25, 25]
           
    

                
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player)
    
    for w in walls:
        pygame.draw.rect(screen, GREEN, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    for p in portals:
        pygame.draw.rect(screen, PURPLE, p)
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, WHITE)
        screen.blit(text, [400, 200])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
