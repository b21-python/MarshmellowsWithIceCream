import pygame
from math import pi
pygame.init() # initialize pygame

# Create a game window that is 640 by 480 pixels
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True

# create a variable to store player position so we can modify it based on keyboard input
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

def cropAlpha(surface):
    final_size = surface.get_bounding_rect()
    cropped = pygame.Surface((final_size.width, final_size.height), pygame.SRCALPHA, 32)
    cropped.blit(surface, (0,0), final_size)
    cropped = cropped.convert_alpha()
    return cropped

def prepareTraffic(sprite):
    rotated_sprite = pygame.transform.rotate(sprite, 180)
    return cropAlpha(rotated_sprite)

# Load Car
cat_sheet = pygame.image.load('Sprites/cat_white-32x32.png')
#image from opengameart.org, search cats and click 'CATS REWORKS'
cat1 = pygame.Surface((32,32), pygame.SRCALPHA, 32)
cat1.blit(cat_sheet, (0,0), (0, 0, 32, 32))

cat2 = pygame.Surface((32,32), pygame.SRCALPHA, 32)
cat2.blit(cat_sheet, (0,0), (32, 0, 32, 32))

cat3 = pygame.Surface((32,32), pygame.SRCALPHA, 32)
cat3.blit(cat_sheet, (0,0), (64, 0, 32, 32))

cat4 = pygame.Surface((32,32), pygame.SRCALPHA, 32)
cat4.blit(cat_sheet, (0,0), (0, 32, 32, 32))

cat5 = pygame.Surface((32,32), pygame.SRCALPHA, 32)
cat5.blit(cat_sheet, (0,0), (32, 32, 32, 32))

cat6 = pygame.Surface((32,32), pygame.SRCALPHA, 32)
cat6.blit(cat_sheet, (0,0), (64, 32, 32, 32))

player = [cat1, cat2, cat3, cat4, cat5, cat6]
player_frame = 0

#player = cropAlpha(pygame.image.load('Sprites/cat.png'))
#print(player)
#player = pygame.transform.scale(player, (120,100))

while running:
    # poll for events and react to user closing the window to end the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Set screen color
    screen.fill("cyan")
    
    pygame.draw.circle(screen, (254,189,89,255), (320,40), 100)
    
    pygame.draw.circle(screen, "white", (20,63), 33)
    pygame.draw.circle(screen, "white", (50,44), 30)
    pygame.draw.circle(screen, "white", (80,63), 32)
    
    pygame.draw.circle(screen, "white", (200,80), 23)
    pygame.draw.circle(screen, "white", (160,84), 23)
    pygame.draw.circle(screen, "white", (178,70), 20)
        
    pygame.draw.circle(screen, "white", (500,63), 36)
    pygame.draw.circle(screen, "white", (530,34), 32)
    pygame.draw.circle(screen, "white", (560,63), 38)
    
    pygame.draw.circle(screen, "white", (400,112), 23)
    pygame.draw.circle(screen, "white", (360,115), 23)
    pygame.draw.circle(screen, "white", (379,98), 20)

    # Draw a rectangle
    pygame.draw.rect(screen, (234,182,118), (0, 150, 640,480))
    
    player_box = screen.blit(player[player_frame], player_pos)
    
    # Draw an ellipse
    pygame.draw.ellipse(screen, (0,200,255), (100, 250, 450, 100))
    
    pygame.draw.ellipse(screen, (227,241,241,255),(200, 350, 150, 100))    
    #banana

    # update player position based on keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 10
    if keys[pygame.K_s]:
        player_pos.y += 10
    if keys[pygame.K_a]:
        player_pos.x -= 10
    if keys[pygame.K_d]:
        player_pos.x += 10
        player_frame = (player_frame + 1) % 6
        
    

    # Render what you've drawn to the screen
    pygame.display.flip()

    clock.tick(60) # limit to 60 FPS

# Exit game when we leave the game loop
pygame.quit()         