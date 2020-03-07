from player import *
from static_objects import *
from score_board import *
from config import *
from swords import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

# init player
player1 = Player(PLAYER_1_CONFIG)
player2 = Player(PLAYER_2_CONFIG)
player2.rect.x = 200

furnace = Furnace()
Hammer = Hammer()
score = ScoreBoard()
endPoint = EndPoint(score)
collect = CollectionPoint(Iron)
grinder = Grinder()

# Init sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(collect)
all_sprites.add(score)
all_sprites.add(endPoint)
score.add_item()
score.add_item()
score.add_item()
score.add_item()

# init game clock
clock = pygame.time.Clock()

# start music
pygame.mixer.music.load("Music/ingame.mp3")
pygame.mixer.music.play(-1)

# game clock
while not done:
    # Set screen background
    screen.fill(BACKGROUND_COLOUR)

    # Draw all sprites
    for entity in all_sprites:
        if isinstance(entity, Player):
            screen.blit(entity.surf, entity.rect)
            # Draw inventory if not none
            if entity.inventory is not None:
                screen.blit(entity.inventory.surf, entity.inventory.rect)
        else:
            screen.blit(entity.surf, entity.rect)

        if isinstance(entity, StaticObject) and entity.print_inventory:
            entity.print(screen)

    # Loop through every event in the queue
    for event in pygame.event.get():
        # Quiting
        if event.type == pygame.QUIT:
            done = True

    # Update players
    pressed = pygame.key.get_pressed()
    player1.update(pressed, all_sprites)
    player2.update(pressed, all_sprites)
    furnace.update()

    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()
quit()
