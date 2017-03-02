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


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, func, x, y, layer, has_collision):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.func = func
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self._layer = layer
        self.has_collision = has_collision

    def update(self, time_delta=0):
        self.func(time_delta)


# TODO: make Animatedsprite class
class Animatedsprite(pygame.sprite.Sprite):
    def __init__(self, animations, animation_name, func, x, y, layer, has_collision):
        pygame.sprite.Sprite.__init__(self)
        self.animations = animations
        self.animation_name = animation_name
        self.func = func
        self.image = animations[animation_name].get_frame(0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self._layer = layer
        self.has_collision = has_collision

    def update(self, time_delta=0):
        self.func(time_delta)
        center = self.rect.center
        self.image = self.animations[self.animation_name].get_frame(time_delta)
        self.rect = self.image.get_rect()
        self.rect.center = center

    def change_animation(self, animation_name):
        self.reset_animation()
        self.animation_name = animation_name

    def reset_animation(self):
        self.animations[self.animation_name].reset()


class Animation:
    def __init__(self, frames, index=0, is_looping=True):
        self.frames = frames
        self.index = index
        self.time = 0
        self.is_looping = is_looping
        self.pause = False

    def get_frame(self, time_delta):
        if not self.pause and (self.is_looping or self.index < len(self.frames) - 1):
            self.time += time_delta
            if self.time > self.frames[self.index].duration:
                self.time -= self.frames[self.index].duration
                self.index += 1
                self.index %= len(self.frames)
        return self.frames[self.index].image

    def reset(self):
        self.index = 0
        self.time = 0


class Frame:
    def __init__(self, image, duration):
        self.image = image
        self.duration = duration
