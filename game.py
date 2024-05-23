import pygame
import os
from grid import Grid

# Set window position
os.environ['SDL_VIDEO_WINDOW_POS'] = "900,100"

# Initialize pygame
pygame.init()

# Set up display
surface = pygame.display.set_mode((1200, 1300))
pygame.display.set_caption('Sudoku')

# Initialize font
game_font = pygame.font.SysFont('Comic Sans Ms', 50)
game_font2 = pygame.font.SysFont('Comic Sans Ms', 30)


# Create grid instance
grid = Grid(pygame,game_font)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type ==pygame.MOUSEBUTTONDOWN and not grid.win:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                grid.get_mouse_click(pos[0],pos[1])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.win:
                grid.restart()
            
                
    
    # Clear window surface to black and draw grid
    surface.fill((0, 0, 0))
    
    #draw grid here
    grid.draw_all(pygame, surface)
    
    if grid.win:
        won_surface =game_font.render("You Won!!", False,(0,255,0))
        surface.blit(won_surface,(900,600))
        press_space_surf =game_font2.render("press space to restart",False,(0,255,200))
        surface.blit(press_space_surf,(920,720))
    
    # Update display
    pygame.display.flip()

pygame.quit()
