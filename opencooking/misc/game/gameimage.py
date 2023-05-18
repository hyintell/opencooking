import pygame
import os
import numpy as np
from PIL import Image
from opencooking.misc.game.game import Game
# from misc.game.utils import *


class GameImage(Game):
    def __init__(self, filename, world, sim_agents, record=False):
        Game.__init__(self, world, sim_agents)
        self.game_record_dir = 'misc/game/record/{}/'.format(filename)
        self.record = record


    def on_init(self):
        super().on_init()

        if self.record:
            # Make game_record folder if doesn't already exist
            if not os.path.exists(self.game_record_dir):
                os.makedirs(self.game_record_dir)

            # Clear game_record folder
            for f in os.listdir(self.game_record_dir):
                os.remove(os.path.join(self.game_record_dir, f))

    def get_image_obs(self):
        self.on_render()
        string = pygame.image.tobytes(self.screen, 'RGB')
        img_rgb = Image.frombytes('RGB', self.screen.get_size(), string)
        img_rgb = np.array(img_rgb)
        return img_rgb

    def save_image_obs(self, t):
        self.on_render()
        pygame.image.save(self.screen, '{}/t={:03d}.png'.format(self.game_record_dir, t))
