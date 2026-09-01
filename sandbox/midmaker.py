import pygame
from midiutil import MIDIFile
pygame.init()
pygame.mixer.init()
midi = MIDIFile(1,deinterleave=True)

w,h = 2100, 1080    
screen = pygame.display.set_mode((w,h),pygame.FULLSCREEN)

BLUE = (0,0,240)
BGRAY = (26, 43, 76)
LBLUE = (57,134,255)
GRAY = (146, 118,156) 
CYAN = (0,254,240) 
GREEN = (0,254,15)
 
rects = []
size = min(w,h)//5
btn = [False for _ in range(16)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(rects):
                if rect.collidepoint(event.pos):
                    btn[i] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            btn = [False for _ in range(16)]
     
    screen.fill(BGRAY)
    if len(rects) < 16:
        for c in range(4):
            for r in range(4):
                rects += [pygame.Rect(10+c*size*1.2,10+r*size*1.2,size,size)]
    
    for i, rect in enumerate(rects):
        if btn[i]:
            pygame.draw.rect(screen,CYAN,rect)
        else:
            pygame.draw.rect(screen,LBLUE,rect)
    
    pygame.display.update()  
pygame.quit()                     