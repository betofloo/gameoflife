import pygame
import random

pygame.init()
pygame.display.set_caption("game of life!")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

map = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
       
map = [[random.random()>.7 for i in range(80)]for i in range(80)]

       
while True:
    clock.tick(60)
    event = pygame.event.get()
    
    
    for event in pygame.event.get():
        break
    
    for i in range (80):
        for j in range(80):
            counter = 0
            #up down
            if i<79 and map[i+1] [j] == 1: 
                counter+=1
            if i>0 and map[i-1] [j] == 1:
                counter+=1
            # right left
            if j<79 and map[i][j+1] == 1: 
                counter+=1
            if j>0 and map[i][j-1] == 1: 
                counter+=1
            #top corners
            if i<79 and j<79 and map[i+1][j+1]==1: 
                counter+=1
            if i>=0 and j<79 and map[i-1][j+1]==1: 
                counter+=1
            #bottom corners
                
            if i<79 and j>=0 and map[i+1][j-1]==1: 
                counter+=1
            if i>=0 and j>=0 and map[i-1][j-1]==1: 
                counter+=1
                
    pygame.time.wait(200)
    
    
    
    screen.fill((0,0,0))
    
    for i in range (80):
        for j in range(80):
            if map[i][j]==0:
                pygame.draw.rect(screen, (255,255,255), (j*10, i*10, 10, 10 ))
                pygame.draw.rect(screen, (0,0,0), (j*10, i*10, 10, 10 ), 1)
            if map[i][j]==1:
                pygame.draw.rect(screen, (0,200,200), (j*10, i*10, 10, 10, ))
                    
                    
                
    
    pygame.display.flip()
    
    
    
pygame.quit()
