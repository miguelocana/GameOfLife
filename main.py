import pygame
import numpy as np
import time

pygame.init()
width, height = 1000, 800
screen = pygame.display.set_mode((width,height))
bg = 25,25,25
screen.fill(bg)
nxC, nyC = 50,50
dimCW = width/nxC
dimCH = height/nyC
gameState = np.zeros((nxC,nyC))

# Automaton
gameState[21,21] = 1
gameState[21,22] = 1
gameState[21,23] = 1
gameState[22,21] = 1
gameState[23,21] = 1
gameState[22,23] = 1
gameState[23,23] = 1
gameState[24,22] = 1
gameState[25,22] = 1
gameState[25,21] = 1
gameState[25,23] = 1
gameState[25,19] = 1
gameState[26,22] = 1
gameState[26,20] = 1
gameState[26,24] = 1
gameState[27,22] = 1
gameState[27,25] = 1
gameState[28,21] = 1
gameState[29,21] = 1
gameState[28,23] = 1
gameState[29,23] = 1

# Execution control of the game
pauseExect = False

# Execution loop
while True:
    
    newgameState = np.copy(gameState)
    
    screen.fill(bg)
    
    # Time between events
    time.sleep(0.01)
    
    # Keyboard and mouse events
    ev = pygame.event.get()
    for event in ev:
        # Detect any key
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect     
        # Detect mouse
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newgameState[celX,celY] = 1
        
        # To quit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # Grid
    for y in range(0,nxC):
        for x in range(0, nyC):
            
            if not pauseExect:
                n_neigh = gameState[(x-1) % nxC,(y-1) % nyC] + \
                gameState[(x) % nxC,(y-1) % nyC] + \
                gameState[(x+1) % nxC,(y-1) % nyC] + \
                gameState[(x-1) % nxC,(y) % nyC] + \
                gameState[(x+1) % nxC,(y) % nyC] + \
                gameState[(x-1) % nxC,(y+1) % nyC] + \
                gameState[(x) % nxC,(y+1) % nyC] + \
                gameState[(x+1) % nxC,(y+1) % nyC] 
                
                # RULES:
                if gameState[x,y] == 0 and n_neigh == 3:
                    newgameState[x,y] = 1
                
                elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newgameState[x,y] = 0
        
            poly = [((x)*dimCW, y*dimCH),
                    ((x+1)*dimCW, y*dimCH),
                    ((x+1)*dimCW, (y+1)*dimCH),
                    ((x)*dimCW, (y+1)*dimCH)]
            if newgameState[x,y]==0:
                pygame.draw.polygon(screen,(128,128,128),poly,1)
            else:
                pygame.draw.polygon(screen,(255,255,255),poly,0)

    # Upload the state of the game
    gameState = np.copy(newgameState)
    # Upload the fps
    pygame.display.flip()
    pass