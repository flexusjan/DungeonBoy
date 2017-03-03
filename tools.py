from sprites import *
import pygame
import tmx


# object data from map files is stored here
class Entry:
    def __init__(self, name=None, x=0, y=0, layer=0, has_collision=False):
        self.name = name
        self.x = x
        self.y = y
        self.layer = layer
        self.has_collision = has_collision

    def __str__(self):
        return str([self.name, self.x, self.y, self.layer, self.has_collision])


# load map file
# format: name, x, y, layer, collision-flag
def load_map(filename):
    map_data = []
    with open(filename, "r") as map_file:
        for line in map_file:
            split_result = line.split(",")
            if len(split_result) == 5:
                entry = Entry()
                entry.name = split_result[0]
                entry.x = int(split_result[1])
                entry.y = int(split_result[2])
                entry.layer = int(split_result[3])
                entry.has_collision = (int(split_result[4]) == 1)
                map_data.append(entry)
    return map_data


# load tmx file and generate sprites TODO: read all .tmx properties
def load_tmx_map(filename, tilesize=32):
    # load tmx file
    tilemap = tmx.TileMap.load(filename)

    # load gids from tilesets
    gids = {}
    for tileset in tilemap.tilesets:
        # load gids
        image = pygame.image.load(tileset.image.source)
        gid = tileset.firstgid
        for y in range(image.get_height() / tileset.tileheight):
            for x in range(image.get_width() / tileset.tilewidth):
                rect = pygame.Rect(x * tileset.tilewidth, y * tileset.tileheight, tileset.tilewidth, tileset.tileheight)
                if tilesize == tileset.tilewidth and tilesize == tileset.tileheight:
                    gids[gid] = image.subsurface(rect)
                else:
                    gids[gid] = pygame.transform.smoothscale(image.subsurface(rect), (tilesize, tilesize))
                gid += 1

    # create list of sprites based on layer & gids data
    sprites = []
    layer_id = 0
    for layer in [l for l in tilemap.layers if isinstance(l, tmx.Layer)]:
        for y in range(tilemap.height):
            for x in range(tilemap.width):
                gid = layer.tiles[y * tilemap.width + x].gid
                if gid > 0:
                    sprite = Staticsprite(gids[gid], x * tilesize + tilesize/2, y * tilesize + tilesize/2, layer_id, False)
                    if layer_id == 0:  # lowest layer don't need alpha
                        sprite.image = sprite.image.convert()
                    else:
                        sprite.image = sprite.image.convert_alpha()
                    sprites.append(sprite)
        layer_id += 10

    return sprites


def load_animation(image, frame_pos, frame_size, frame_count, frame_durations, index=0, is_looping=True):
    frames = []
    for x, duration in zip(range(frame_pos[0], frame_count * frame_size[0], frame_size[0]), frame_durations):
        frame = Frame(image.subsurface((x, frame_pos[1], frame_size[0], frame_size[1])).convert_alpha(), duration)
        frames.append(frame)
    return Animation(frames, index, is_looping)
