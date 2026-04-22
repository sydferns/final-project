import pygame


def main():
    pygame.init()
    pygame.display.set_caption("BTS")
    resolution = (1200, 800)
    screen = pygame.display.set_mode(resolution)
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
        pygame.display.flip()
    pygame.quit()



if __name__ == "__main__":
    main()