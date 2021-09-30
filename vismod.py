import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pybullet as p
import pybullet_data


class Vismod(tk.Tk):
    def __init__(self):
        super().__init__()
        # tk.Tk().withdraw()
        self.title("Vismod")
        self.geometry("500x300")
        self.file_name = tk.StringVar()

        self.label = tk.Label(self, text="文件路径:", padx=5, pady=5)
        # self.label.grid(row=0,column=1)
        self.label.pack(pady=5)

        #        self.show_label = tk.Label(self, textvariable=self.file_name, padx=5, pady=5)
        #        self.show_label.pack()
        show_msg = tk.Message(self, textvariable=self.file_name, width=300)
        # show_msg.grid(row=1,column=1)
        show_msg.pack(pady=10)

        self.button_open = tk.Button(self, text="打开", command=self.select_file, width=7)
        # self.button_open.grid(row=3,column=1)
        self.button_open.pack(pady=5)

        self.button_view = tk.Button(self, text="查看", command=lambda: self.view_model(self.filename), width=7)
        # self.button_view.grid(row=4,column=1)
        self.button_view.pack(pady=5)

        operation_msg = tk.Label(self, text="按住Ctrl键，配合鼠标进行旋转平移", anchor='center').pack(fill='both', side=tk.BOTTOM)

    def select_file(self):
        filetypes = (('urdf files', '*.urdf'), ('sdf files', '*.sdf'))
        self.filename = fd.askopenfilename(title='Open a file', filetypes=filetypes)
        self.file_name.set(self.filename)
        # showinfo(title='Selected File',message=filename)
        # print(filename)

    def view_model(self, filename):
        Pybullet(filename)


class Pybullet:
    def __init__(self, filename):
        p.connect(p.GUI)
        urdf_root_path = pybullet_data.getDataPath()
        # p.loadURDF(os.path.join(urdf_root_path,"plane.urdf"))
        try:
            p.loadURDF(filename)
            # tk.messagebox.showinfo(title="操作方法",message="按住Ctrl键，配合鼠标键进行拖动旋转平移等操作。")
        except:
            tk.messagebox.showerror(title="导入模型失败",
                                    message="导入模型失败，请检查模型是否依赖了其他文件 (如urdf中import了其他stl文件)，urdf文件及其依赖文件应该放在同一个文件夹中。")
            p.disconnect()

        p.resetDebugVisualizerCamera(cameraDistance=1.5,
                                     cameraYaw=0,
                                     cameraPitch=-40,
                                     cameraTargetPosition=[0, -0.35, 0.2])
        try:
            while True:
                p.stepSimulation()
        except:
            pass

        # p.disconnect()


if __name__ == '__main__':
    root = Vismod()
    root.mainloop()