import pygame
import numpy as np
import time

pygame.init()

# Ancho y alto de la pantall
width, height = 1000, 800

# Se crea la pantalla
screen = pygame.display.set_mode((width,height))

# Color del fondo oscuro
bg = 25,25,25

# Se pinta el fondo con el color elegido
screen.fill(bg)

# Cuantas celdas
nxC, nyC = 50,50

# Alto y ancho de cada celda
dimCW = width/nxC
dimCH = height/nyC

# Estado de las celdas (Vivas = 1, Muertas = 0)
gameState = np.zeros((nxC,nyC))

#%% Autómata
gameState[22,20] = 1
gameState[24,20] = 1
gameState[21,21] = 1
gameState[21,22] = 1
gameState[21,23] = 1
gameState[21,24] = 1
gameState[22,24] = 1
gameState[23,24] = 1
gameState[24,23] = 1

# Control de la ejecución del juego
pauseExect = False

#%%
# Bucle de ejecución
while True:
    
    newgameState = np.copy(gameState)
    
    screen.fill(bg)
    
    # Tiempo entre eventos
    time.sleep(0.01)
    
    # Registramos eventos de teclado y ratón
    ev = pygame.event.get()
    
    for event in ev:
        
        # Detecta la tecla
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
            
        # Detecta el mouse
        mouseClick = pygame.mouse.get_pressed()
        
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newgameState[celX,celY] = 1
        
        # Para salir
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # Para crear el polígono de cada celda
    for y in range(0,nxC):
        for x in range(0, nyC):
            
            if not pauseExect:
            
                # Número de vecinos cercanos
                n_neigh = gameState[(x-1) % nxC,(y-1) % nyC] + \
                gameState[(x) % nxC,(y-1) % nyC] + \
                gameState[(x+1) % nxC,(y-1) % nyC] + \
                gameState[(x-1) % nxC,(y) % nyC] + \
                gameState[(x+1) % nxC,(y) % nyC] + \
                gameState[(x-1) % nxC,(y+1) % nyC] + \
                gameState[(x) % nxC,(y+1) % nyC] + \
                gameState[(x+1) % nxC,(y+1) % nyC] 
                
                # Regla 1º: una célula muerta con exactamente 3 vecinas vivas, "revive"
                if gameState[x,y] == 0 and n_neigh == 3:
                    newgameState[x,y] = 1
                
                # Regla 2º: una célula viva con menos de 2 o más de 3 vecinas vivas, "muerte"
                elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newgameState[x,y] = 0
        
            # Puntos aue definen el polígono que estamos dibujando
            poly = [((x)*dimCW, y*dimCH),
                    ((x+1)*dimCW, y*dimCH),
                    ((x+1)*dimCW, (y+1)*dimCH),
                    ((x)*dimCW, (y+1)*dimCH)]
                    
            # Se dibuja la celda para x e y
            if newgameState[x,y]==0:
                pygame.draw.polygon(screen,(128,128,128),poly,1)
            else:
                pygame.draw.polygon(screen,(255,255,255),poly,0)

    # Actualizamos el estado del juego
    gameState = np.copy(newgameState)
                
    # Actualiza los fotogramas de nuesta app en cada iteración del while
    pygame.display.flip()
                    

    

    
    pass