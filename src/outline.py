import pygame


class Box():


    def __init__(self, pos=(0,0), size=150, speed=200):
        self.x, self.y = pos
        self.size = size
        self.color = pygame.Color(220, 150, 0)
        self.rect = pygame.Rect(pos[0], pos[1], size, size)
        self.age = 0
        self.speed = speed
        self.direction = 1
        self.moving = True

    def update(self, dt):
        if not self.moving:
            return
        self.age += dt
        self.rect.x += self.speed * self.direction * dt/1000

        #bounce off left
        if self.rect.x <=0:
            self.rect.x = 0
            self.direction = 1
        
        #bounce off right
        elif self.rect.right >= 1200:
            self.rect.right = 1200
            self.direction = -1
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius= 21)


def main():
    pygame.init()
    pygame.display.set_caption("BTS")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (1200, 800)
    screen = pygame.display.set_mode(resolution)
    box = Box((525, 70)) 

    running = True
    while running:
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        #TODO game logic
        box.update(dt)

        #Render & Display
        bg_color = pygame.Color(80,100,150)
        screen.fill(bg_color)
        pygame.draw.rect(screen, (30, 90, 40), (0, 700, 1200, 100)) #grass like
        pygame.draw.rect(screen, (100, 100, 100), (400, 700, 400, 150))

        box.draw(screen)

        if event.type == pygame.MOUSEBUTTONDOWN:
            box.moving = False

        pygame.display.flip()
        dt = clock.tick(36)
    pygame.quit()



if __name__ == "__main__":
    main()