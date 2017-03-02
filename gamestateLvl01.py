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

    def update(self, gsh):
        for event in pygame.event.get():
            # Escape Key
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                gsh.close_all()
                return
            # Exit Button
            elif event.type == pygame.QUIT:
                gsh.close_all()
                return

        # gsh.offset_x += 1
        # gsh.offset_y += 1
        gsh.screen.fill((0, 0, 0))
        self.spritehandler.update()
        self.spritehandler.draw(gsh.screen, (gsh.offset_x, gsh.offset_y))
        pygame.display.flip()
        gsh.clock.tick(0)

    def close(self, gsh):
        pass
