from tkinter import Frame, Button, Tk, messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        self.btn01 = Button(self)
        self.btn01["text"] = "点击送花"
        self.btn01.pack()
        self.btn01["command"] = self.sendingFollowers()

        self.btnQuit = Button(self, text="退出", command=root.destroy)
        self.btnQuit.pack()

    def sendingFollowers(self):
        messagebox.showinfo("送花", "送你99朵玫瑰花")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x100+200+300")
    root.title("一个经典的 GUI 程序类的测试")
    app = Application(master=root)
    root.mainloop()