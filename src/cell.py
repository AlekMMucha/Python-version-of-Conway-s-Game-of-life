import tkinter as tk
import collections.abc
import constants
from main import playing_matrix_x, playing_matrix_y

class Cell:
    def __init__(self, button: tk.Button, index:tuple[int, int], state:bool=False):
        self.button = button
        self.index = index
        self.state = state
    
    def toggle_state(self):
        self.state = not self.state
        self.update_colour()

    def update_colour(self):
        if self.state == True:
            self.button.itemconfig(self.index, fill = constants.CELL_COLOUR_ALIVE)
        else:
            self.button.itemconfig(self.index, fill = constants.CELL_COLOUR_DEAD)

    def create_matrix(self, width:int, height:int) -> list[list[Cell]]:
        index_x = 1
        index_y = 1
        rows = []
        for i in range(height):
            rows.append([Cell(tk.Button(width=constants.CELL_SIZE, height = constants.CELL_SIZE, bg = constants.CELL_COLOUR_DEAD), (i,j),False) for j in range(width)])
        return rows

    def block_button_inputs(self):
        pass