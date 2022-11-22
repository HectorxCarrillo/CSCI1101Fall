import pygame

pygame.init()

# game settings
monitor_display = (800, 600)

game_display = pygame.display

pygame.display_set_caption("tank domination")

system_clock = pygame.time.Clock()

game.characteristics = (
    "sky" {
    "color"; 135,206,235
    }
)

game_running_flag=True

# game logic 
while game_running_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            game_running_flag = True

    if not game_running_flag:
        pygame.quit()
        break

    # Running the game 
    game_display.fill(game.characteristics)
    pygame.display.update()

    system_clock.tick(30)





