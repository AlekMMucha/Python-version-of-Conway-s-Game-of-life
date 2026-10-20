import tkinter as tk
import collections.abc
import sys
import constants
from cell import Cell

def main():
    if len(sys.argv)<3:
        raise ValueError("Usage: python3 main.py <width> <height>")
    playing_matrix_x,playing_matrix_y = int(sys.argv[1]),int(sys.argv[2])
    Window = tk.Tk()
    Window.title("My python version of Conways Game of Life")
    Window.overrideredirect(False)
    Window.bind("<Escape>", lambda event: Window.destroy())
    Window.configure(background='black')
    ###Window.geometry(f"{playing_matrix_x*constants.CELL_SIZE}x{playing_matrix_y*constants.CELL_SIZE}")
    '''label = tk.Label(Window, text=f"this is a {playing_matrix_x*constants.CELL_SIZE}x{playing_matrix_y*constants.CELL_SIZE} window", font=("Arial", 12))
    label.pack()'''
    pack_buttons(playing_matrix_x,playing_matrix_y,Window)
    Window.geometry("")
    Window.mainloop()

def create_matrix(width:int, height:int,Window:tk.Tk,list_of_row_frames:list[tk.Frame]) -> list[list[Cell]]:
    rows = []
    Window.pixel = tk.PhotoImage(width=1, height=1)
    for i in range(height):
        rows.append([Cell(tk.Button(master=list_of_row_frames[i],bd=0,highlightthickness=0,padx=0,pady=0,image=Window.pixel,width=constants.CELL_SIZE, height = constants.CELL_SIZE, bg = constants.CELL_COLOUR_DEAD), (i,j),False) for j in range(width)])
    return rows

def pack_buttons(width:int, height:int,Window:tk.Tk):
    row_frames = [tk.Frame(Window) for _ in range(height)]
    for row_frame in row_frames:
        row_frame.pack(side="top",fill="x")
    matrix:list[list[Cell]] = create_matrix(width,height,Window,row_frames)
    for r in range(height):
        row_frames[r].pack(side="top",fill="x")
        for c in range(width):
            cell_to_pack = matrix[r][c]
            cell_to_pack.button.master = row_frames[r]
            cell_to_pack.button.pack(side="left")




if __name__ == "__main__":
    main()