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
        self.falling = False
        self.fall_speed = 0

    def update(self, dt, base, game_over):
        new_box = False
        #movement
        if self.moving:
            self.rect.x += self.speed * self.direction * dt/1000

        #bounce off left
            if self.rect.x <=0:
                self.rect.x = 0
                self.direction = 1
        #bounce off right
            elif self.rect.right >= 1200:
                self.rect.right = 1200
                self.direction = -1
        
        #falling
        if self.falling:
            self.fall_speed += 1
            self.rect.y += self.fall_speed

            #stop on base
            if self.rect.bottom >= base.top:
                self.rect.bottom = base.top
                self.falling = False

                if self.rect.right > base.left and self.rect.left < base.right:
                    print("Good landing!")
                    new_box = True
                else:
                    game_over = True
        return game_over, new_box
    
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
    base = pygame.Rect(400, 680, 400, 120)
    game_over = False

    running = True
    while running:
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                box.moving = False
                box.falling = True

        #game logic
        game_over, new_box = box.update(dt, base, game_over)
        if new_box and not game_over:
            box = Box((525, 70))

        #Render & Display
        screen.fill((80,100,150))
        pygame.draw.rect(screen, (30, 90, 40), (0, 700, 1200, 100)) #grass like
        pygame.draw.rect(screen, (60, 60, 70), base)
        pygame.draw.rect(screen, (120, 110, 140), base, 5)

        box.draw(screen)

        if game_over:
            font = pygame.font.SysFont(None, 120)
            text = font.render("GAME OVER", True, (200, 50, 50))
            screen.blit(text, (350, 300))

        pygame.display.flip()
        dt = clock.tick(36)
    pygame.quit()



if __name__ == "__main__":
    main()