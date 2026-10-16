import tkinter as tk
import collections.abc
import sys
import constants
from cell import Cell

def main():
    playing_matrix_x,playing_matrix_y = int(sys.argv[1]),int(sys.argv[2])
    root = tk.Tk()
    root.title("My python version of Conways Game of Life")
    root.overrideredirect(False)
    root.bind("<Escape>", lambda event: root.destroy())
    root.configure(background='black')
    root.geometry(f"{playing_matrix_x*constants.CELL_SIZE}x{playing_matrix_y*constants.CELL_SIZE}")
    label = tk.Label(root, text=f"this is a {playing_matrix_x*constants.CELL_SIZE}x{playing_matrix_y*constants.CELL_SIZE} window", font=("Arial", 12))
    label.pack()
    root.mainloop()

def pack_buttons(width:int, height:int):
    matrix:list[list[Cell]] = Cell.create_matrix(width, height)


if __name__ == "__main__":
    main()