import pygame

size = 540, 1080
width, height = size
DBLUE = (30, 30, 150)
RED = (255, 0, 0)
wed = 64
start, end = (0, 0), (0, 0)
starts, ends = [], []
drawing = False

pygame.init()
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            if(end != (0,0)):
                start = end
            else:
                start = event.pos
            starts.append(start)
        elif event.type == pygame.MOUSEMOTION and drawing:
            end = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end = event.pos
            ends.append(end)
    
    screen.fill(DBLUE)
    
    pygame.draw.line(screen,(255,255,0),start,end,wed)
    
    for line in range(len(ends)):
        pygame.draw.line(screen,RED,starts[line],ends[line],wed)
        pygame.draw.circle(screen,RED,ends[line],wed//2)
        
    pygame.display.update()

pygame.quit()
