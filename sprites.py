import pygame


class Staticsprite(pygame.sprite.Sprite):
    """Just a simple, not changing, not moving pygme compatible sprite

    Attributes:
        image: pygame.Surface (derived attribute from pygame.sprite.Sprite)
        rect: pygame.Rect (derived attribute from pygame.sprite.Sprite)
        _layer: int (is protected for pygame compatibility)
        has_collision: bool (not yet implemented)

    Args:
        image: pygame.Surface
        x: int
        y: int
        layer: int
        has_collision: bool
    """

    def __init__(self, image, x, y, layer, has_collision):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self._layer = layer
        self.has_collision = has_collision  # not yet implemented TODO: collision handling


# TODO: make Animatedsprite class
class Animatedsprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
