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
        self.screen_width = 1200
        self.moving = True
        self.falling = False
        self.fall_speed = 0

    def update(self, dt, support, game_over):
        new_box = False
        #movement
        if self.moving:
            self.rect.x += self.speed * self.direction * dt/1000

        #bounce off left
            if self.rect.x <=0:
                self.rect.x = 0
                self.direction = 1
        #bounce off right
            elif self.rect.right >= self.screen_width:
                self.rect.right = self.screen_width
                self.direction = -1
        
        #falling
        if self.falling:
            self.fall_speed += 1
            self.rect.y += self.fall_speed

            #stop on base
            if self.rect.bottom >= support.top:
                self.rect.bottom = support.top
                self.falling = False

                if self.rect.right > support.left and self.rect.left < support.right:
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
    boxes = [Box((525, 70))] 
    base = pygame.Rect(400, 680, 400, 120)
    support = base
    game_started = False
    show_start_screen = True
    game_over = False

    running = True
    while running:
        box = boxes[-1]
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if show_start_screen:
                    game_started = True
                    show_start_screen = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    boxes = [Box((525, 70))]
                    box = boxes[-1]
                    support = base
                    game_over = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                box.moving = False
                box.falling = True

        #game logic
        if game_started and not game_over:
            game_over, new_box = box.update(dt, support, game_over)

            if new_box:
                support = boxes[-1].rect
                boxes.append(Box((525, 70)))

        #Render & Display
        screen.fill((80,100,150))
        pygame.draw.rect(screen, (30, 90, 40), (0, 700, 1200, 100)) #grass like
        pygame.draw.rect(screen, (60, 60, 70), base)
        pygame.draw.rect(screen, (120, 110, 140), base, 5)

        for b in boxes:
            b.draw(screen)

        if game_over:
            font = pygame.font.SysFont(None, 120)
            text = font.render("GAME OVER", True, (200, 50, 50))
            screen.blit(text, (350, 300))

            font_2 = pygame.font.SysFont(None, 40)
            restart_text = font_2.render("Press R to restart", True, (255, 255, 255))
            screen.blit(restart_text, (350, 380))

        if show_start_screen:
            screen.fill((20,20,40))
            font1 = pygame.font.SysFont(None, 80)
            start_text = font1.render("Click to Start", True, (255, 255, 255))
            screen.blit(start_text, (300, 350))

        pygame.display.flip()
        dt = clock.tick(36)
    pygame.quit()



if __name__ == "__main__":
    main()