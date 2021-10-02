import tkinter as tk
import logx
import tkinter.filedialog as fd
import pybulletx
import os
from config import WINDOW_HEIGHT, WINDOW_WIDTH

logger = logx.setup_logger('add_slidebar')


class AddSlideBar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.file_name = tk.StringVar()

        # if history.history:
        #     self.filename = history.history[-1]
        #     self.file_name.set(self.filename)

        self.label = tk.Label(self, text="文件路径:", padx=5, pady=5)
        self.label.pack(pady=10)

        show_msg = tk.Message(self, textvariable=self.file_name, width=300)
        show_msg.pack(pady=10)

        self.button_open = tk.Button(self, text="打开", command=self.select_file, width=7)
        self.button_open.pack(padx=WINDOW_WIDTH * 0.3, pady=5)

        self.button_view = tk.Button(self, text="查看", command=lambda: self.add_slidebar(self.filename), width=7)
        self.button_view.pack(pady=10)

        # operation_msg = tk.Label(self, text="按住Ctrl键，配合鼠标进行旋转平移", anchor='center').pack(fill='both', side=tk.BOTTOM,pady=30)

        self.filetypes = (('All files', '*'), ('urdf files', '*.urdf'), ('sdf files', '*.sdf'))
        self.extension_types = []

        for i in range(1, len(self.filetypes)):
            self.extension_types.append(self.filetypes[i][1][1:])
        logger.debug(f'self.extension_types={self.extension_types}')

    def select_file(self):
        try:

            self.filename = fd.askopenfilename(title='Open a file', filetypes=self.filetypes)
        except:
            tk.messagebox.showerror(title='错误', message='打开文件失败')

        if os.path.splitext(self.filename)[-1] not in self.extension_types:
            tk.messagebox.showerror(title='类型错误', message='不能打开此类文件，请重新选择')
            self.filename = None
            self.file_name.set('')
        else:
            self.file_name.set(self.filename)
        # showinfo(title='Selected File',message=filename)
        # print(filename)

    def add_slidebar(self, filename):
        if filename:
            pybulletx.Pybullet(filename).add_slidebar()
        else:
            tk.messagebox.showerror(title='文件错误', message='请先选择文件')
