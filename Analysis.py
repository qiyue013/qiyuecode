
"""
@Author  : 小猪佩琪
@Time    : 2019.10.12
@Desc : Less interests,More interest.(主流网站vip视频解析通道)
@Project : python_appliction
@FileName: c5.py
@Software: VScode

"""
import re
import tkinter as tk
import tkinter.messagebox as msgbox
import webbrowser
 
"""
帆帆专用视频解析
"""
 
 
class VideoParse:
    # 构造函数，用于初始化全部变量
    def __init__(self, width=600, height=200, background='gray'):
        self.w = width
        self.h = height
        self.bg = background
        self.title = '哆啦A梦屁股大  一个马桶装不下'
        self.root = tk.Tk(className=self.title)
        self.url = tk.StringVar()
        self.v = tk.IntVar()
        self.v.set(1)
        # 定义3个frame，frame 默认按从上往下排列
        # Frame空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        frame_3 = tk.Frame(self.root)
 
        # menu 菜单
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        menu1 = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='Menu', menu=menu1)
        menu1.add_command(label='about me', command=lambda: webbrowser.open('https://blog.csdn.net/zwx19921215'))
        menu1.add_command(label='exit', command=lambda: self.root.quit())
 
        # 控件内容设置
        # frame1 ，每个frame标签元素默认按从左只有排列
        group = tk.Label(frame_1, text='视频解析选项(默认Part 1)', padx=14, pady=14)
        tb1 = tk.Radiobutton(frame_1, text='Part 1', variable=self.v, value=1, width=10, height=3)
        tb2 = tk.Radiobutton(frame_1, text='Part 2', variable=self.v, value=2, width=10, height=3)
        # frame2
        label1 = tk.Label(frame_2, text="小仙女请输入网址：")
        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        label2 = tk.Label(frame_2, text=" ")
        play = tk.Button(frame_2, text="PLAY", font=('楷体', 12), fg='black', width=3, height=-1, command=self.video_play)
        label3 = tk.Label(frame_2, text=" ")
        # frame3
        label_explain = tk.Label(frame_3, fg='black', font=('楷体', 14),
                                 text='\nTip:小仙女（帆帆）专用')
 
        # 控件布局
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        group.grid(row=0, column=0)
        tb1.grid(row=0, column=1)
        tb2.grid(row=0, column=2)
        label1.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        label2.grid(row=0, column=2)
        play.grid(row=0, column=3, ipadx=10, ipady=10)
        label3.grid(row=0, column=4)
        label_explain.grid(row=1, column=0)
 
    """
    视频解析
    """
 
    def video_play(self):
        # 视频解析网站地址
        # 无名小站接口
        port_1 = 'http://www.wmxz.wang/video.php?url='
        # 思古解析接口
        port_2 = 'http://api.bbbbbb.me/jx/?url='
 
        # 正则表达是判定是否为合法链接
        if re.match(r'^https?:/{2}\w.+$', self.url.get()):
            if self.v.get() == 1:
                # 视频链接获取
                ip = self.url.get()
                # 浏览器打开
                webbrowser.open(port_1 + ip)
            elif self.v.get() == 2:
                ip = self.url.get()
                # 浏览器打开
                webbrowser.open(port_2 + ip)
 
        else:
            msgbox.showerror(title='error', message='视频地址错误！')
 
    """
    tkinter窗口居中设置
    """
 
    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int((ws / 2) - (self.w / 2))
        y = int((hs / 2) - (self.h / 2))
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))
        # 设置背景颜色
        # self.root.configure(background=self.bg)
 
    """
    窗口绘制事件
    """
 
    def event(self):
        # 禁止修改窗口大小
        self.root.resizable(False, False)
        # 窗口居中
        self.center()
        # Start GUI （调用tk mainloop 展示窗口）
        self.root.mainloop()
 
 
if __name__ == '__main__':
    # 实例化视频解析对象
    app = VideoParse()
    # 窗口绘制事件
    app.event()


