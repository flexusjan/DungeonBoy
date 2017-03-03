from gamestate import Gamestate
from spritehandler import Spritehandler
import pygame
import tools
import os


class GamestateLvl01(Gamestate):
    def __init__(self):
        Gamestate.__init__(self)
        self.spritehandler = Spritehandler()

    def init(self, gsh):
        sprites = tools.load_tmx_map(os.path.join("media", "sprites", "static", "lvl01.tmx"), 32
                                     )
        self.spritehandler.add(True, *sprites)
        gsh.offset_x, gsh.offset_y = 1000, 1000

        # load animated sprites
        self.spritehandler.add(False, gsh.sprites['DungeonBoy'])

    def update(self, gsh):
        # handle global events, store remainder in gsh.events
        gsh.events[:] = []
        for event in pygame.event.get():
            # Escape Key
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                gsh.close_all()
                return
            # Exit Button
            elif event.type == pygame.QUIT:
                gsh.close_all()
                return
            else:
                gsh.events.append(event)
        gsh.pressed_keys = pygame.key.get_pressed()

        # calculate time delta
        gsh.time_delta = pygame.time.get_ticks() - gsh.time
        gsh.time = pygame.time.get_ticks()

        gsh.offset_x = gsh.sprites['DungeonBoy'].x - gsh.screen_w/2
        gsh.offset_y = gsh.sprites['DungeonBoy'].y - gsh.screen_h/2

        gsh.screen.fill((0, 0, 0))
        self.spritehandler.update(gsh)
        self.spritehandler.draw(gsh.screen, (gsh.offset_x, gsh.offset_y))
        pygame.display.flip()
        gsh.clock.tick(0)

    def close(self, gsh):
        pass
