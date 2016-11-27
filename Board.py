import pprint

class Board:

    
    def __init__(self, width, height, num_mines, is_blind):
        self.width = width
        self.height = height
        self.is_blind = is_blind        # win criteria -- is this is "blind" style winning criteria?
        self.num_covered = width * height
        self.mine_grid = [[0] * width] * height
        self.clue_grid = [[0] * width] * height
        self.is_uncovered = [[False] * width] * height
        self.marked = [[0] * width] * height    # 0 = unmarked, 1+ = what it's marked as

    def randomly_place_mines(self, num_mines):
        self.num_covered = width * height
        self.mine_grid = [[0] * width] * height
        self.clue_grid = [[0] * width] * height
        self.is_uncovered = [[False] * width] * height
        self.marked = [[0] * width] * height
        # TODO

    def uncover(self, x, y):
        # TODO
        
    def display(self):
        # display to STDOUT
        # TODO
