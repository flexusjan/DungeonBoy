import pygame


class Spritehandler:
    """A handler for pygame sprites.
    
    Update and draw pygame sprites like a pygame Group. It stores sprites in segments
    for faster collision detection. (Quadtree would be better, but meh...)
    Spritehandler will draw sprites ordered by layer.

    Why use Spritehandler instead of Pygame Groups?
    - faster collision detection
    - can handle many sprites
    - you can change sprite's layer without refill the group
    - can be optimized for non-moving sprites

    Args:
        segment_size: Set the size of the segements, required for faster collision detection.
            Default is (512, 512).
    """

    # helper class, stores list of sprites and a rect.
    class Segment:
        def __init__(self, rect):
            self.rect = rect
            self.sprites = []

    def __init__(self, segment_size=(512, 512)):
        self._sprites = []
        self._static_sprites = []
        self._segments = {}
        self._static_segments = {}
        self._segment_size = segment_size

    def _make_segments(self, segments, sprites):
        # make a big rect, contains all sprites.
        union_rect = pygame.Rect(0, 0, 0, 0)
        union_rect.unionall_ip([s.rect for s in sprites])
        width, height = self._segment_size

        # prepare range args
        start_x = union_rect.x // width
        start_y = union_rect.y // height
        stop_x = start_x + union_rect.width // width + 2
        stop_y = start_y + union_rect.height // height + 2

        # make segments
        segments.clear()
        for y in range(start_y * height, stop_y * height, height):
            for x in range(start_x * width, stop_x * width, width):
                segments[(x, y)] = Spritehandler.Segment(pygame.Rect(x, y, width, height))

        # add sprites to segments
        for sprite in sprites:
            x = sprite.rect.x - sprite.rect.x % width
            y = sprite.rect.y - sprite.rect.y % height
            segments[x, y].sprites.append(sprite)

    def add(self, static, *sprites):
        """Adds any number of pygame sprite like objects to the Spritehandler.

        Args:
            static: if True: Sprites shouldn't move. And their update() method will not be called.
                if False: for moving and animated sprites (may be slower).
            sprites: pygame sprite like objects.
        """
        if static:
            for sprite in sprites:
                self._static_sprites.append(sprite)
            self._static_sprites.sort(key=lambda x: x._layer)
            self._make_segments(self._static_segments, self._static_sprites)
        else:
            for sprite in sprites:
                self._sprites.append(sprite)
            self._sprites.sort(key=lambda x: x._layer)
            self._make_segments(self._segments, self._sprites)

    def get(self, rect):
        """Returns all sprites in the given rect.

        Args:
            rect: pygame.Rect

        Returns: List of sprites.
        """
        # prepare range args
        step_x = self._segment_size[0]
        step_y = self._segment_size[1]
        start_x = rect.x - rect.x % step_x - step_x
        start_y = rect.y - rect.y % step_y - step_y
        stop_x = start_x + (rect.width // step_x + 3) * step_x
        stop_y = start_y + (rect.height // step_y + 3) * step_y

        # address segments via index and get the render sprites
        sprites = []
        for y in range(start_y, stop_y, step_y):
            for x in range(start_x, stop_x, step_x):
                if (x, y) in self._segments:
                    sprites.extend(self._segments[x, y].sprites)
                if (x, y) in self._static_segments:
                    sprites.extend(self._static_segments[x, y].sprites)

        return sprites

    def update(self):
        """Calls the update method for every non-static sprite"""
        for sprite in self._sprites:
            sprite.update()

        # remake segments, because some sprites have been moved.
        if self._segments:
            self._make_segments(self._segments, self._sprites)

    def draw(self, surface, offset=(0, 0)):
        """Draw all sprites to a pygame surface.

        Draw all sprites to the surface. Use the offset to make a viewport

        Args:
            surface: A pygame.Surface as render target.
            offset: (int, int) Sets the offset for the viewport.
        """
        # sort sprites (layer-based), apply offset, render image, remove offset
        offset_x = int(offset[0])
        offset_y = int(offset[1])
        rect = pygame.Rect(offset, surface.get_size())
        for sprite in sorted(self.get(rect), key=lambda s: s._layer):
            if rect.colliderect(sprite.rect):
                sprite.rect.x -= offset_x
                sprite.rect.y -= offset_y
                surface.blit(sprite.image, sprite.rect.topleft)
                sprite.rect.x += offset_x
                sprite.rect.y += offset_y

    def remove(self, *sprites):
        """Delete sprites from Spritehandler.

        Args:
            sprites: pygame sprite like objects.

        Returns:
            True if successful, False if a sprite can't be removed.
        """
        result = True
        for sprite in sprites:
            if sprite in self._sprites:
                self._sprites.remove(sprite)
                for segment in self._segments.itervalues():
                    if sprite in segment.sprites:
                        segment.sprites.remove(sprite)
                    else:
                        result = False
            elif sprite in self._static_sprites:
                self._static_sprites.remove(sprite)
                for segment in self._static_segments.itervalues():
                    if sprite in segment.sprites:
                        segment.sprites.remove(sprite)
                    else:
                        result = False
            else:
                result = False
        self._make_segments(self._segments, self._sprites)
        self._make_segments(self._static_segments, self._static_sprites)
        return result

    def empty(self):
        """Delete all sprites from Spritehandler"""
        self._sprites[:] = []
        self._segments.clear()
        self._static_sprites[:] = []
        self._static_segments.clear()
