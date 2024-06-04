import pygame

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self,win):
        keys = pygame.key.get_pressed()
        #x1=self.x

        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel

        if keys[pygame.K_RIGHT] and self.x < 500 - self.width:
            self.x += self.vel

        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.vel

        if keys[pygame.K_DOWN] and self.y < 500 - self.height:
            self.y += self.vel
        
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height)) 
        # it refreshes the window  
        pygame.display.update() 
  

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
        #pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height)) 
