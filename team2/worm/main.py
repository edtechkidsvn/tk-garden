import random
from bot_base import GardenBotBase

class GardenBot(GardenBotBase):
    def __init__(self, *args):
        GardenBotBase.__init__(self, *args)
        self.role = self.roles["WORM"]

    def do_turn(self):
        print(self.x, self.y)
        return self.directions["DOWN"]


