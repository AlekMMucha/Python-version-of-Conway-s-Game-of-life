import tkinter as tk
import collections.abc
import constants

class Cell:
    def __init__(self, button: tk.Button, index:tuple[int, int], state:bool=False,next_state:bool=False):
        self.button = button
        self.index = index
        self.state = state
        self.next_state = next_state

    def toggle_state(self):
        self.state = not self.state
        self.update_colour()

    def update_colour(self):
        if self.state == True:
            self.button.config(bg = constants.CELL_COLOUR_ALIVE)
        else:
            self.button.config(bg = constants.CELL_COLOUR_DEAD)

    def block_button_input(self):
        self.button.config(command=None)

    def create_button_input(self):
        self.button.config(command = self.toggle_state)
