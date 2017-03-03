import pygame
import math


def func_dungeonboy(self, gsh):
    # don't divide by zero
    if gsh.time_delta == 0:
        fim = 0.0
    else:
        fim = gsh.time_delta / 1000.0

    speed = 100.0
    is_moving = False
    is_attacking = False
    x, y = 0, 0

    # handle input
    if gsh.pressed_keys[pygame.K_LEFT] and not gsh.pressed_keys[pygame.K_RIGHT]:
        self.direction = 'Left'
        is_moving = True
        x = -1
    if gsh.pressed_keys[pygame.K_RIGHT]and not gsh.pressed_keys[pygame.K_LEFT]:
        self.direction = 'Right'
        is_moving = True
        x = 1
    if gsh.pressed_keys[pygame.K_UP] and not gsh.pressed_keys[pygame.K_DOWN]:
        self.direction = 'Up'
        is_moving = True
        y = -1
    if gsh.pressed_keys[pygame.K_DOWN] and not gsh.pressed_keys[pygame.K_UP]:
        self.direction = 'Down'
        is_moving = True
        y = 1
    if gsh.pressed_keys[pygame.K_SPACE]:
        is_attacking = True

    # make diagonal movement so fast as other movement
    if x != 0 and y != 0:
        speed /= math.sqrt(2)

    # move sprite
    self.x += speed * fim * x
    self.y += speed * fim * y

    # set animation
    if is_attacking:
        self.change_animation('Attack' + self.direction, True)
    elif is_moving:
        self.change_animation('Walk' + self.direction, True)
    else:
        self.change_animation('Idle' + self.direction, False)
