from gamestateLvl01 import *


class GamestateInit(Gamestate):
    def __init__(self):
        Gamestate.__init__(self)

    def init(self, gsh):
        pygame.init()

        gsh.screen_flags = 0
        gsh.screen = pygame.display.set_mode((1280, 720), gsh.screen_flags)  # TODO: load resolution from config file
        gsh.view = pygame.Surface((1280, 720))
        gsh.screen_w, gsh.screen_h = gsh.screen.get_size()
        gsh.offset_x, gsh.offset_y = 0, 0
        gsh.clock = pygame.time.Clock()
        gsh.push_state(GamestateLvl01())

    def update(self, gsh):
        pass

    def close(self, gsh):
        print "FPS:", gsh.clock.get_fps()
        pygame.quit()
