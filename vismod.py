import tkinter as tk
from tkinter import ttk
from view_model import ViewModel
from add_slidebar import AddSlideBar
from config import WINDOW_WIDTH, WINDOW_HEIGHT

WINDOW_SIZE = str(WINDOW_WIDTH) + 'x' + str(WINDOW_HEIGHT)


class Vismod(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        notebook = ttk.Notebook(parent)
        add_slidebar_tab = AddSlideBar(notebook)
        view_model_tab = ViewModel(notebook)

        notebook.add(add_slidebar_tab, text='添加滑条')
        notebook.add(view_model_tab, text='查看模型')
        notebook.pack()

        operation_msg = tk.Label(parent, text="按住Ctrl键，配合鼠标进行旋转平移", anchor='center').pack(fill='both', side=tk.BOTTOM)


if __name__ == "__main__":
    root = tk.Tk()
    root.title('vismod')
    root.geometry(WINDOW_SIZE)
    Vismod(root).pack(fill="both", expand=True)
    root.mainloop()
