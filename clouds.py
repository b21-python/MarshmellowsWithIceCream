import pygame

move_arr = [30, 54, 80, 200, 160, 178, 120, 130, 140, 156, 166, 176, 36, 46, 56, 400, 360, 379, 500, 530, 560, 496, 485, 474, 600, 589, 579, 430, 441, 452, 434, 442, 452]

def updatepos(index, moveX):
    if move_arr[index] >= 640:
        move_arr[index] = 0
    else:
        move_arr[index]+=moveX


def clouds(screen, moveX = 0):
    
        #The Sun
    pygame.draw.circle(screen, (254,189,89,255), (320,40), 100)
      #left side of clouds
    updatepos(0, moveX)
    pygame.draw.circle(screen, "white", (move_arr[0],63), 33)
    updatepos(1, moveX)
    pygame.draw.circle(screen, "white", (move_arr[1],44), 30)
    updatepos(2, moveX)
    pygame.draw.circle(screen, "white", (move_arr[2],63), 32)
    
    updatepos(3, moveX)
    pygame.draw.circle(screen, "white", (move_arr[3],80), 23)
    updatepos(4, moveX)
    pygame.draw.circle(screen, "white", (move_arr[4],84), 23)
    updatepos(5, moveX)
    pygame.draw.circle(screen, "white", (move_arr[5],70), 20)
    
    updatepos(6, moveX)
    pygame.draw.circle(screen, "white", (move_arr[6],130), 13)
    updatepos(7, moveX)
    pygame.draw.circle(screen, "white", (move_arr[7],123), 10)
    updatepos(8, moveX)
    pygame.draw.circle(screen, "white", (move_arr[8],132), 12)
    
    updatepos(9, moveX)
    pygame.draw.circle(screen, "white", (move_arr[9],30), 13)
    updatepos(10, moveX)
    pygame.draw.circle(screen, "white", (move_arr[10],20), 10)
    updatepos(11, moveX)
    pygame.draw.circle(screen, "white", (move_arr[11],30), 12)
    
    updatepos(12, moveX)
    pygame.draw.circle(screen, "white", (move_arr[12],116), 12)
    updatepos(13, moveX)
    pygame.draw.circle(screen, "white", (move_arr[13],109), 10)
    updatepos(14, moveX)
    pygame.draw.circle(screen, "white", (move_arr[14],117), 11)
    
    #right side of clouds
    updatepos(15, moveX)
    pygame.draw.circle(screen, "white", (move_arr[15],112), 23)
    updatepos(16, moveX)
    pygame.draw.circle(screen, "white", (move_arr[16],115), 23)
    updatepos(17, moveX)
    pygame.draw.circle(screen, "white", (move_arr[17],98), 20)
    
    updatepos(18, moveX)
    pygame.draw.circle(screen, "white", (move_arr[18],63), 36)
    updatepos(19, moveX)
    pygame.draw.circle(screen, "white", (move_arr[19],34), 32)
    updatepos(20, moveX)
    pygame.draw.circle(screen, "white", (move_arr[20],63), 38)
      
    updatepos(21, moveX)
    pygame.draw.circle(screen, "white", (move_arr[21],132), 13)
    updatepos(22, moveX)
    pygame.draw.circle(screen, "white", (move_arr[22],121), 10)
    updatepos(23, moveX)
    pygame.draw.circle(screen, "white", (move_arr[23],130), 14)
    
    updatepos(24, moveX) 
    pygame.draw.circle(screen, "white", (move_arr[24],132), 13)
    updatepos(25, moveX)
    pygame.draw.circle(screen, "white", (move_arr[25],121), 10)
    updatepos(26, moveX)
    pygame.draw.circle(screen, "white", (move_arr[26],130), 14)
    
    updatepos(27, moveX)
    pygame.draw.circle(screen, "white", (move_arr[27],30), 13)
    updatepos(28, moveX)
    pygame.draw.circle(screen, "white", (move_arr[28],20), 10)
    updatepos(29, moveX)
    pygame.draw.circle(screen, "white", (move_arr[29],30), 12)
    
    updatepos(30, moveX)
    pygame.draw.circle(screen, "white", (move_arr[30],80), 11)
    updatepos(31, moveX)
    pygame.draw.circle(screen, "white", (move_arr[31],70), 9)
    updatepos(32, moveX)
    pygame.draw.circle(screen, "white", (move_arr[32],80), 10)