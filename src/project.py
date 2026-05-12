import pygame


class Box():


    def __init__(self, pos=(0,0), speed=200):
        self.x, self.y = pos
        self.color = pygame.Color(220, 150, 90) #220, 150, 0
        self.width = 250
        self.height = 150
        self.rect = pygame.Rect(pos[0], pos[1], self.width, self.height)
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
    
    def draw(self, surface, camera):
        draw_rect = self.rect.copy()
        draw_rect.y += camera
        pygame.draw.rect(surface, self.color, draw_rect, border_radius= 21)
        pygame.draw.rect(surface, (240, 210, 170), draw_rect, 5, border_radius= 21)


# -- display and render function-----------------------------------------------------------

def display(screen, base, show_start_screen, game_over, camera):
    if show_start_screen:
        screen.fill((20,20,40))
        font1 = pygame.font.SysFont(None, 80)
        start_text = font1.render("Click to Start", True, (255, 255, 255))
        screen.blit(start_text, (300, 350))

    elif game_over:
        font = pygame.font.SysFont(None, 120)
        text = font.render("GAME OVER", True, (200, 50, 50))
        screen.blit(text, (350, 300))

        font_2 = pygame.font.SysFont(None, 40)
        restart_text = font_2.render("Press R to restart", True, (255, 255, 255))
        screen.blit(restart_text, (350, 380))

    else:
        screen.fill((80, 100, 150))
        ground_rect = pygame.Rect(0, 700 + camera, 1200, 100)
        pygame.draw.rect(screen, (30, 90, 40), ground_rect)
        base_draw = base.copy()
        base_draw.y += camera
        pygame.draw.rect(screen, (60, 60, 70), base_draw)
        pygame.draw.rect(screen, (120, 110, 140), base_draw, 5)


# -- main loop -----------------------------------------------------------------------------

def main():
    pygame.init()
    pygame.display.set_caption("BTS")
    clock = pygame.time.Clock()
    dt = 0

    resolution = (1200, 800)
    screen = pygame.display.set_mode(resolution)

    boxes = [Box((475, 70))] 
    base = pygame.Rect(400, 680, 400, 120)
    support = base

    game_started = False
    show_start_screen = True
    game_over = False
    score = 0
    camera = 0

    running = True
    while running:
        box = boxes[-1]
        if len(boxes) > 1:
            camera_target = 150- (support.y - 400)
            camera += (camera_target - camera) * 0.1

        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if show_start_screen:
                    game_started = True
                    show_start_screen = False
                    
                elif game_started and not game_over:
                    box.moving = False
                    box.falling = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    boxes = [Box((475, 70))]
                    box = boxes[-1]
                    support = base
                    score = 0
                    camera = 0
                    game_over = False #don't need start screen for restart

        #game logic
        if game_started and not game_over:
            game_over, new_box = box.update(dt, support, game_over)

            if new_box:
                score += 1
                support = box.rect
                new_y = support.y - 460
                boxes.append(Box((475, new_y)))

        #Render & Display
        display(screen, base, show_start_screen, game_over, camera)

        if game_started and not game_over:    
            for b in boxes:
                b.draw(screen, camera)

        #scoring
        score_font = pygame.font.SysFont(None, 50)
        score_text = score_font.render(f"Score: {score}", True, (255,255,255))
        screen.blit(score_text, (20,20))
            
        
        

        pygame.display.flip()
        dt = clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()