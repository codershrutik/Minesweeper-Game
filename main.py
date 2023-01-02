from tkinter import *
from unit import Cell
import configparser
import new

WIDTH=1400
HEIGHT=720
GRID_SIZE=6
CELL_COUNT=GRID_SIZE ** 2
MINES_COUNT=(CELL_COUNT) // 4

root = Tk()
# Override the configure of the window
root.configure(bg="grey")
root.geometry(f'{configparser.WIDTH}x{configparser.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='#5D6D7E',
    width=configparser.WIDTH,
    height=new.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='#5D6D7E',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)

game_title.place(
    x=new.width_prct(30), y=0
)

center_frame = Frame(
    root,
    bg='black',
    width=new.width_prct(75),
    height=new.height_prct(75)
)
center_frame.place(
    x=new.width_prct(30),
    y=new.height_prct(30),
)

for x in range(configparser.GRID_SIZE):
    for y in range(configparser.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
# Call the label from the Cell class
Cell.create_cell_count_label(top_frame)
Cell.cell_count_label_object.place(
    x=new.width_prct(42), y=new.height_prct(15)
)

Cell.randomize_mines()


# Run the window
root.mainloop()