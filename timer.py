import tkinter as tk

from tkinter.messagebox import showerror, showinfo
import time

import timer_support


class Toplevel1:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'

        top.geometry("400x350+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1, 1)
        top.title("Timer")
        top.configure(background="#d9d9d9")

        self.top = top

        self.title_lbl = tk.Label(self.top)
        self.title_lbl.place(relx=0.0, rely=0.0, height=40, width=396)
        self.title_lbl.configure(background="#d9d9d9")
        self.title_lbl.configure(compound='left')
        self.title_lbl.configure(disabledforeground="#a3a3a3")
        self.title_lbl.configure(font="-family {Segoe UI} -size 24")
        self.title_lbl.configure(foreground="#000000")
        self.title_lbl.configure(text='''Timer''')

        self.counter_lbl = tk.Label(self.top)
        self.counter_lbl.place(relx=0.35, rely=0.243, height=110, width=116)
        self.counter_lbl.configure(background="#d9d9d9")
        self.counter_lbl.configure(compound='left')
        self.counter_lbl.configure(disabledforeground="#a3a3a3")
        self.counter_lbl.configure(font="-family {Segoe UI} -size 72")
        self.counter_lbl.configure(foreground="#000000")
        self.counter_lbl.configure(text='''00''')

        self.Spinbox1 = tk.Spinbox(self.top, from_=1.0, to=300.0)
        self.Spinbox1.place(relx=0.375, rely=0.714, relheight=0.086
                            , relwidth=0.25)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(font="-family {Segoe UI} -size 20")
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="blue")
        self.Spinbox1.configure(selectforeground="white")
        self.Spinbox1.configure(command=self.get_seconds)
        self.Spinbox1.bind("<Return>", self.get_seconds)

    def get_seconds(self, *args):
        seconds = self.Spinbox1.get()
        try:
            seconds = int(seconds)
            self.counter(seconds)

        except ValueError:
            showerror("Número inválido", "Por favor insira um valor válido em segundos")

    def counter(self, seconds):
        t_end = time.time() + seconds
        while time.time() < t_end:
            self.counter_lbl.configure(text="{:0>2d}".format(seconds))
            seconds -= 1
            self.top.update()
            time.sleep(1)
        self.counter_lbl.configure(text="00")
        showinfo("Finalizado", "Timer Finalizado!")


def start_up():
    timer_support.main()


if __name__ == '__main__':
    timer_support.main()
