import pygame


class Box():


    def __init__(self, pos=(0,0), size=150):
        self.x, self.y = pos
        self.size = size
        self.color = pygame.Color(220, 150, 0)
        self.rect = pygame.Rect(pos[0], pos[1], size, size)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius= 21)


def main():
    pygame.init()
    pygame.display.set_caption("BTS")
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

        #Render & Display
        bg_color = pygame.Color(80,100,200)
        screen.fill(bg_color)

        box.draw(screen)

        pygame.display.flip()
    pygame.quit()



if __name__ == "__main__":
    main()