import pygame 

YELLOW = (255, 255, 0)
RED = (255, 0, 0)

x = pygame.init()
window = pygame.display.set_mode((4000,4000))
pygame.display.set_caption("Game")

def msg(size,mess,x_pos,y_pos):
    font = pygame.sysfont(None,size)
    render = font.render(mess,True,RED)
    window.blits(render , (x_pos,y_pos))
    pygame.display.update()

def game_loop():
    x = 1040
    y = 2100
    z = 100
    k = 100
    game_over = False
    x_change=0
    y_change=0
    while game_over==False:
        window.fill(YELLOW)
        pygame.draw.rect(window, RED, [x,y,z,k])
        msg(200,"Start",1750,1750)
        x = x - x_change
        y = y - y_change
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True    
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change =+ 10
                if event.key==pygame.K_RIGHT:
                    x_change =- 10
                if event.key==pygame.K_DOWN:
                    y_change =+ 10
                if event.key==pygame.K_UP:
                    y_change =- 10
            if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT or pygame.K_RIGHT or pygame.K_DOWN or pygame.K_UP:
                        x_change=0 
                        y_change=0


pygame.quit()
quit()
