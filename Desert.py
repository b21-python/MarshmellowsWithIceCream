import pygame
from math import pi
from player_animation import cat
from enemy_animation import kitten
pygame.init() # initialize pygame

# Create a game window that is 640 by 480 pixels
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True

# create a variable to store player position so we can modify it based on keyboard input
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

enemy_pos = pygame.Vector2(0, 300)
player_size = 34
def cropAlpha(surface):
    final_size = surface.get_bounding_rect()
    cropped = pygame.Surface((final_size.width, final_size.height), pygame.SRCALPHA, 32)
    cropped.blit(surface, (0,0), final_size)
    cropped = cropped.convert_alpha()
    return cropped

def prepareTraffic(sprite):
    rotated_sprite = pygame.transform.rotate(sprite, 180)
    return cropAlpha(rotated_sprite)

def is_point_in_ellipse(point_x, point_y, ellipse_center_x, ellipse_center_y, ellipse_radius_x, ellipse_radius_y):
    dx = (point_x - ellipse_center_x) / ellipse_radius_x
    dy = (point_y - ellipse_center_y) / ellipse_radius_y
    if (dx*dx + dy*dy <= 1):
        return True
    else:
        return False
    
player = cat()
enemy = kitten()
player_frame = 0
enemy_frame = 0
#player = cropAlpha(pygame.image.load('Sprites/cat.png'))
#print(player)
#player = pygame.transform.scale(player, (120,100))
font = pygame.font. SysFont('Ariel',42)
game_over = False
while running:
    # poll for events and react to user closing the window to end the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #if game_over == True:
        #fontSurface = font.render("You win!", True, [0, 225, 0])
    #else:
        #fontSurface = font.render("You lose!", True, [225, 0, 0])
    #screen.blit(fontSurface, [300, 200])
    #pygame.display.flip()

    # Set screen color
    screen.fill("cyan")
    
    #The Sun
    pygame.draw.circle(screen, (254,189,89,255), (320,40), 100)
      #left side of clouds
    pygame.draw.circle(screen, "white", (30,63), 33)
    pygame.draw.circle(screen, "white", (54,44), 30)
    pygame.draw.circle(screen, "white", (80,63), 32)
    
    pygame.draw.circle(screen, "white", (200,80), 23)
    pygame.draw.circle(screen, "white", (160,84), 23)
    pygame.draw.circle(screen, "white", (178,70), 20)
    
    pygame.draw.circle(screen, "white", (120,130), 13)
    pygame.draw.circle(screen, "white", (130,123), 10)
    pygame.draw.circle(screen, "white", (140,132), 12)
    
    pygame.draw.circle(screen, "white", (156,30), 13)
    pygame.draw.circle(screen, "white", (166,20), 10)
    pygame.draw.circle(screen, "white", (176,30), 12)
    
    pygame.draw.circle(screen, "white", (36,116), 12)
    pygame.draw.circle(screen, "white", (46,109), 10)
    pygame.draw.circle(screen, "white", (56,117), 11)
    
    #right side of clouds
    pygame.draw.circle(screen, "white", (400,112), 23)
    pygame.draw.circle(screen, "white", (360,115), 23)
    pygame.draw.circle(screen, "white", (379,98), 20)
    
    pygame.draw.circle(screen, "white", (500,63), 36)
    pygame.draw.circle(screen, "white", (530,34), 32)
    pygame.draw.circle(screen, "white", (560,63), 38)
      
    pygame.draw.circle(screen, "white", (496,132), 13)
    pygame.draw.circle(screen, "white", (485,121), 10)
    pygame.draw.circle(screen, "white", (474,130), 14)
    
    pygame.draw.circle(screen, "white", (600,132), 13)
    pygame.draw.circle(screen, "white", (589,121), 10)
    pygame.draw.circle(screen, "white", (579,130), 14)
    
    pygame.draw.circle(screen, "white", (430,30), 13)
    pygame.draw.circle(screen, "white", (441,20), 10)
    pygame.draw.circle(screen, "white", (452,30), 12)
    
    pygame.draw.circle(screen, "white", (434,80), 11)
    pygame.draw.circle(screen, "white", (442,70), 9)
    pygame.draw.circle(screen, "white", (452,80), 10)
    

    # Draw a rectangle
    pygame.draw.rect(screen, (234,182,118), (0, 150, 640,480))
    
    #pygame.Rect( (60, 100), (80,80))
    
    player_box = screen.blit(player[player_frame], player_pos)
    
    enemy_box = screen.blit(enemy[0],enemy_pos)
   
    # Draw an ellipse
    lake = pygame.Surface((480,180), pygame.SRCALPHA)
    lake_width = 450
    lake_height = 100
    pygame.draw.ellipse(lake, (0,200,255, 170), (0, 20, lake_width, lake_height))
    
    lake_offset_pos_x = 110
    lake_offset_pos_y = 230
    lake_box = screen.blit(lake, (lake_offset_pos_x, lake_offset_pos_y))
    
    #enemy_box = pygame.draw.rect(screen, (227,241,241,255), (enemy, (50,50)))
    
    if player_box.colliderect(enemy_box):
        running = False
        game_over = True        
   
#     if enemy_box.colliderect(lake_box):
        #running = False
        
    # update player position based on keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 10
        player_frame = (player_frame + 1) % 3 + 3
        
    if keys[pygame.K_s]:
        player_pos.y += 10
        player_frame = (player_frame + 1) % 3 + 6

    if keys[pygame.K_a]:
        player_pos.x -= 10
        player_frame = (player_frame + 1) % 3 + 9

    if keys[pygame.K_d]:
        player_pos.x += 10
        player_frame = (player_frame + 1) % 3 
        
    if player_pos.x > enemy_pos.x:
        enemy_pos.x += 1
    if player_pos.x < enemy_pos.x:
        enemy_pos.x -= 1
    if player_pos.y > enemy_pos.y:
        enemy_pos.y += 1
    if player_pos.y < enemy_pos.y:
        enemy_pos.y -= 1
        
    if player_pos.x <= -player_size:
        player_pos.x = screen.get_width() - 1
    if player_pos.x >= screen.get_width():
        player_pos.x = -player_size + 1
    if player_pos.y <= -player_size:
        player_pos.y = screen.get_height() - 1
    if player_pos.y >= screen.get_height():
        player_pos.y = -player_size + 1
    # Render what you've drawn to the screen
    pygame.display.flip()

    clock.tick(60) # limit to 60 FPS
    
#font = pygame.font. SysFont('Ariel',42)
#game_over = False
#running = True
#while running:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #running = False
if game_over == True:
    fontSurface = font.render("You lose!", True, [0, 225, 0])
    screen.blit(fontSurface, [300, 200])
    pygame.display.flip()
else:
    pygame.quit()  
# Exit game when we leave the game loop
#pygame.quit()         