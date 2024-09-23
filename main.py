import pygame

pygame.init()

clock = pygame.time.Clock()
black = 0, 0, 0
size = width, height = 320, 240
screen = pygame.display.set_mode(size)
speed = [2, 2]

ball = pygame.image.load("image/ball.png")
ballrect = ball.get_rect()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
         
    ballrect = ballrect.move(speed)   
         
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()