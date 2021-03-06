from gamestateLvl01 import *
from sprites import *
from tools import load_animation
from spritefuncs import *


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
        gsh.sprites = {}
        gsh.events = []
        gsh.pressed_keys = None
        gsh.time = pygame.time.get_ticks()
        load_dungeonboy(gsh)
        gsh.push_state(GamestateLvl01())

    def update(self, gsh):
        pass

    def close(self, gsh):
        print "FPS:", gsh.clock.get_fps()
        pygame.quit()


def load_dungeonboy(gsh):
    image = pygame.image.load(os.path.join("media", "sprites", "animated", "dungeonboy_2.png"))
    animations = {'SpellcastUp': load_animation(image, (0, 0), (64, 64), 7, [150] * 7),
                  'SpellcastLeft': load_animation(image, (0, 64), (64, 64), 7, [150] * 7),
                  'SpellcastDown': load_animation(image, (0, 128), (64, 64), 7, [150] * 7),
                  'SpellcastRight': load_animation(image, (0, 192), (64, 64), 7, [150] * 7),
                  'IdleUp': load_animation(image, (0, 512), (64, 64), 1, [0]),
                  'IdleLeft': load_animation(image, (0, 576), (64, 64), 1, [0]),
                  'IdleDown': load_animation(image, (0, 640), (64, 64), 1, [0]),
                  'IdleRight': load_animation(image, (0, 704), (64, 64), 1, [0]),
                  'WalkUp': load_animation(image, (64, 512), (64, 64), 8, [80] * 8),
                  'WalkLeft': load_animation(image, (64, 576), (64, 64), 8, [80] * 8),
                  'WalkDown': load_animation(image, (64, 640), (64, 64), 8, [80] * 8),
                  'WalkRight': load_animation(image, (64, 704), (64, 64), 8, [80] * 8),
                  'Hurt': load_animation(image, (0, 1280), (64, 64), 6, [100] * 6, 0, False),
                  'AttackUp': load_animation(image, (0, 1344), (192, 192), 6, [75] * 6),
                  'AttackLeft': load_animation(image, (0, 1536), (192, 192), 6, [75] * 6),
                  'AttackDown': load_animation(image, (0, 1728), (192, 192), 6, [75] * 6),
                  'AttackRight': load_animation(image, (0, 1920), (192, 192), 6, [75] * 6)}

    gsh.sprites['DungeonBoy'] = Animatedsprite(animations, 'IdleDown', func_dungeonboy, 1500, 1500, 50, True)
    gsh.sprites['DungeonBoy'].direction = 'Down'
    gsh.sprites['DungeonBoy'].speed = 200.0


