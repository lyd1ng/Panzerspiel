# import random
import pygame
import box
from random import randint
from global_settings import (SCREEN_DIMENSION, BOX_SIZE)


class arena(list):
    """
    An arena is just an extended list providing
    an update and a draw function
    An arena is build by an arena factory function
    """
    def __init(self):
        pass

    def update(self):
        """
        Update every box in this arena and remove them if their
        are death ( the health is less or equal to zero)
        This way a destructable arena is provided
        """
        for s in self:
            s.update()
            if s.death:
                self.remove(s)

    def draw(self, screen):
        """
        Just draw every box
        """
        for s in self:
            s.draw(screen)


def add_borders(arena, box_template, box_size):
    """
    This function just adds borders to the arena
    """
    # Add borders at the top and bottom of the arena
    for i in range(0, SCREEN_DIMENSION[0] // box_size[0] + 1):
        # Use deepcopy to as the boxes in box_types only works
        # as a template
        box_template = box_template
        box_rectangle = pygame.Rect(i * box_size[0],
                0, box_size[0], box_size[1])
        arena.append(box.box(box_rectangle, box_template))
        box_rectangle = pygame.Rect(i * box_size[0],
                SCREEN_DIMENSION[1] - box_size[1], box_size[0], box_size[1])
        arena.append(box.box(box_rectangle, box_template))
    # Add borders at the left and right of the arena
    for i in range(0, SCREEN_DIMENSION[1] // box_size[1] + 1):
        # Use deepcopy to as the boxes in box_types only works
        # as a template
        box_template = box_template
        box_rectangle = pygame.Rect(0,
                i * box_size[1], box_size[0], box_size[1])
        arena.append(box.box(box_rectangle, box_template))
        box_rectangle = pygame.Rect(SCREEN_DIMENSION[0] - box_size[0],
                i * box_size[1], box_size[0], box_size[1])
        arena.append(box.box(box_rectangle, box_template))
    return arena


def random_arena():
    """
    This function is for test purpose only and places 20 boxes
    of random type randomly of the arena
    """
    _arena = arena()
    box_templates = [box.box_template(pygame.image.load("res2/TBoxWood.png"), 500),
            box.box_template(pygame.image.load("res2/TBoxStone.png"), -1)]

    for i in range(20):
        posx = randint(BOX_SIZE[0], SCREEN_DIMENSION[0])
        posy = randint(BOX_SIZE[1], SCREEN_DIMENSION[1])
        box_template = box_templates[randint(0, len(box_templates) - 1)]
        b = box.box(pygame.Rect((posx, posy), BOX_SIZE), box_template)
        _arena.append(b)

    add_borders(_arena, box_templates[1], BOX_SIZE)

    return _arena
