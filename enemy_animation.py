import pygame

def kitten():
    cat_sheet = pygame.image.load('Sprites/cat_orange-32x48.png')
    cat1 = pygame.Surface((32,48), pygame.SRCALPHA, 32)
    cat1.blit(cat_sheet, (0,0), (0, 0, 32, 32))

    cat2 = pygame.Surface((32,48), pygame.SRCALPHA, 32)
    cat2.blit(cat_sheet, (0,0), (32, 0, 32, 32))

    cat3 = pygame.Surface((32,48), pygame.SRCALPHA, 32)
    cat3.blit(cat_sheet, (0,0), (64, 0, 32, 32))

    cat4 = pygame.Surface((32,48), pygame.SRCALPHA, 32)
    cat4.blit(cat_sheet, (0,0), (0, 32, 32, 32))

    cat5 = pygame.Surface((32,48), pygame.SRCALPHA, 32)
    cat5.blit(cat_sheet, (0,0), (32, 32, 32, 32))

    cat6 = pygame.Surface((32,48), pygame.SRCALPHA, 32)
    cat6.blit(cat_sheet, (0,0), (64, 32, 32, 32))

    cat7 = pygame.Surface((32,48), pygame.SRCALPHA, 32)
    cat7.blit(cat_sheet, (0,0), (0, 64, 32, 32))

    cat8 = pygame.Surface((32,48), pygame.SRCALPHA, 32)
    cat8.blit(cat_sheet, (0,0), (32, 64, 32, 32))

    cat9 = pygame.Surface((32,48), pygame.SRCALPHA, 32)
    cat9.blit(cat_sheet, (0,0), (64, 64, 32, 32))

    cat10 = pygame.Surface((32,48), pygame.SRCALPHA, 32)
    cat10.blit(cat_sheet, (0,0), (32, 96, 32, 32))

    cat11 = pygame.Surface((32,48), pygame.SRCALPHA, 32)
    cat11.blit(cat_sheet, (0,0), (64, 96, 32, 32))

    cat12 = pygame.Surface((32,48), pygame.SRCALPHA, 32)
    cat12.blit(cat_sheet, (0,0), (96, 96, 32, 32))

    enemy = [cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10, cat11, cat12]
    return enemy