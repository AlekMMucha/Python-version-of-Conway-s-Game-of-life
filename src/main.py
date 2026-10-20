import tkinter as tk
import collections.abc
import sys
import constants
from cell import Cell

def main():
    if len(sys.argv)<3:
        raise ValueError("Usage: python3 main.py <width> <height>")
    playing_matrix_x,playing_matrix_y = int(sys.argv[1]),int(sys.argv[2])
    Window,matrix = render(playing_matrix_x,playing_matrix_y)
    Window.bind("<space>", lambda event: game_loop(playing_matrix_x,playing_matrix_y,matrix,Window))
    Window.mainloop()

def create_matrix(width:int, height:int,Window:tk.Tk,list_of_row_frames:list[tk.Frame]) -> list[list[Cell]]:
    rows = []
    Window.pixel = tk.PhotoImage(width=1, height=1)
    for i in range(height):
        rows.append([Cell(tk.Button(master=list_of_row_frames[i],bd=0,highlightthickness=0,padx=0,pady=0,image=Window.pixel,width=constants.CELL_SIZE, height = constants.CELL_SIZE, bg = constants.CELL_COLOUR_DEAD), (i,j),False) for j in range(width)])
        for cell in rows[i]:
            cell.create_button_input()
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
    return matrix

def render(x,y):     
    Window = tk.Tk()
    Window.title("My python version of Conways Game of Life")
    Window.overrideredirect(False)
    Window.bind("<Escape>", lambda event: Window.destroy())
    Window.configure(background='black')
    matrix = pack_buttons(x,y,Window)
    Window.geometry("")
    return Window, matrix

def game_loop(width:int, height:int, matrix:list[list[Cell]],Window:tk.Tk):
    if Window.nametowidget('.').bind('<space>'): 
            for r in range(height):
                for c in range(width):
                    #matrix[r][c].block_button_input()
                    pass
            Window.unbind('<space>') # Preventing multiple game loops from starting

    for r in range(height):
        for c in range(width):
            cell = matrix[r][c]
            num_alive_neighbours = count_alive_neighbours(r,c,width,height,matrix)
            if cell.state == True:
                if num_alive_neighbours < 2 or num_alive_neighbours >3:
                    cell.next_state = False
                else:
                    cell.next_state = True
            else:
                if num_alive_neighbours == 3:
                    cell.next_state = True
                else:
                    cell.next_state = False
    for r in range(height):
        for c in range(width):
            cell = matrix[r][c]
            cell.state = cell.next_state
            cell.update_colour()
    Window.after(constants.GAME_LOOP_DELAY, lambda: game_loop(width,height,matrix,Window))

def count_alive_neighbours(r:int,c:int,width:int,height:int,matrix:list[list[Cell]])->int:
    alive_neighbours = 0
    alive_neighbours += 1 if r>0 and c>0 and matrix[r-1][c-1].state == True else 0
    alive_neighbours += 1 if r>0 and matrix[r-1][c].state == True else 0
    alive_neighbours += 1 if r>0 and c<width-1 and matrix[r-1][c+1].state == True else 0
    alive_neighbours += 1 if c>0 and matrix[r][c-1].state == True else 0
    alive_neighbours += 1 if c<width-1 and matrix[r][c+1].state == True else 0
    alive_neighbours += 1 if r<height-1 and c>0 and matrix[r+1][c-1].state == True else 0
    alive_neighbours += 1 if r<height-1 and matrix[r+1][c].state == True else 0
    alive_neighbours += 1 if r<height-1 and c<width-1 and matrix[r+1][c+1].state == True else 0
    return alive_neighbours




if __name__ == "__main__":
    main()