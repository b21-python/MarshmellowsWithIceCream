import pygame
from math import pi
pygame.init() # initialize pygame

# Create a game window that is 640 by 480 pixels
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True

# create a variable to store player position so we can modify it based on keyboard input
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    # poll for events and react to user closing the window to end the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Set screen color
    screen.fill("cyan")
    
    pygame.draw.circle(screen, (254,189,89,255), (320,40), 100)

    # Draw a rectangle
    pygame.draw.rect(screen, (234,182,118), (0, 150, 640,480))
   
    # Draw an ellipse
    pygame.draw.ellipse(screen, (0,200,255), (100, 250, 450, 100))
    
    pygame.draw.ellipse(screen, (227,241,241,255),(100, 250, 450, 100))
    
       # Draw the player
    pygame.draw.circle(screen, "purple", player_pos, 40)
    
    

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

    # Render what you've drawn to the screen
    pygame.display.flip()

    clock.tick(60) # limit to 60 FPS

# Exit game when we leave the game loop
pygame.quit()