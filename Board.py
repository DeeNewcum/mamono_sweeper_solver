import pprint

class Board:

    
    def __init__(self, width, height, is_blind):
        self.width = width
        self.height = height
        self.is_blind = is_blind        # win criteria -- is this is "blind" style winning criteria?
        self.grid = [[0] * width] * height

