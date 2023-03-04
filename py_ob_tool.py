import os
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename

from obfuscate_tools import identifier_obfuscate


class PyObTool:
    def __init__(self):
        # 主窗体
        self.window = Tk()

        self.window.title('py混淆工具')
        # self.window.iconphoto(False, PhotoImage(file='parser.ico'))

        screen_w = self.window.winfo_screenwidth()  # 屏幕宽度
        screen_h = self.window.winfo_screenheight()  # 屏幕高度
        window_w = 280
        window_h = 90
        x = (screen_w - window_w) / 2
        y = (screen_h - window_h) / 2
        self.window.geometry("%dx%d+%d+%d" % (window_w, window_h, x, y))

        # 混淆标识符长度
        self.replacement_length = 1
        # 目标文件路径
        self.path = None

        # label
        self.lb = Label(self.window, text="混淆标识符长度：")

        # 下拉框
        self.ddl = ttk.Combobox(self.window, width=3)
        self.ddl['value'] = tuple(x for x in range(1, 41))
        # self.ddl.current(len(self.ddl['value']) - 1)
        self.ddl.current(0)
        self.ddl['state'] = 'readonly'
        self.ddl.bind("<<ComboboxSelected>>", self.get_replacement_length)
        # 选择文件按钮
        self.b1 = Button(self.window, text='选择源文件', width=10, height=1, command=self.select_file)
        # 执行按钮
        self.b2 = Button(self.window, text='生成', width=6, height=1, command=self.execute_obfuscate)

        # 排版
        self.b1.place(x=30, y=10)
        self.lb.place(x=30, y=50)
        self.ddl.place(x=130, y=50)
        self.b2.place(x=190, y=46)
        self.window.resizable(0, 0)

    # 开启主窗体
    def mainloop(self):
        self.window.mainloop()

    # 获取标识符长度下拉框选项值
    def get_replacement_length(self, event):
        self.replacement_length = self.ddl.get()

    # 选择文件按钮事件
    def select_file(self):
        self.path = askopenfilename(title='Please choose a python file',
                                    initialdir='./',
                                    filetypes=[('Python source file', '*.py')])

    # 生成混淆文件按钮
    def execute_obfuscate(self):
        if self.path is None or self.path == "":
            messagebox.showinfo(title='WARN', message='请选择要混淆的代码文件')
            return
        else:
            identifier_obfuscate(self.path,
                                 os.path.dirname(self.path),
                                 self.replacement_length)
            messagebox.showinfo(title='SUCCESS', message='生成成功，文件名：obfuscate.py')


if __name__ == '__main__':
    PyObTool().mainloop()
