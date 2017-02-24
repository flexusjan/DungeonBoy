import pygame


class Staticsprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, layer, has_collision):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.layer = layer
        self._layer = layer
        self.has_collision = has_collision

    def update(self):
        pass
