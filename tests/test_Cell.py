import unittest
from src.cell import Cell
import tkinter as tk
import src.constants as constants

class TestCell(unittest.TestCase):
    def test_cell_creation(self):
        new_cell = Cell(button=None,index=(0,0),state=False)
        self.assertEqual(new_cell.state, False)
        self.assertEqual(new_cell.index, (0,0))

    def test_update_colour(self):
        root = tk.Tk()
        button = tk.Button(root, width=10, height=5)
        new_cell = Cell(button=button, index=(0,0), state=False)
        new_cell.update_colour()
        self.assertEqual(new_cell.button.cget("bg"), constants.CELL_COLOUR_DEAD)
        new_cell.state = True
        new_cell.update_colour()
        self.assertEqual(new_cell.button.cget("bg"), constants.CELL_COLOUR_ALIVE)

    def test_toggle_state(self):
        root = tk.Tk()
        button = tk.Button(root,width=10, height=5)
        new_cell = Cell(button=button, index=(0,0),state=False)
        new_cell.toggle_state()
        self.assertEqual(new_cell.state, True)
        self.assertEqual(new_cell.button.cget("bg"), constants.CELL_COLOUR_ALIVE)

    def test_block_button_input(self):
        pass  # This test is a placeholder since the method is not implemented yet
        