#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Jul 22, 2017 07:37:08 PM
import sys
import os
import process3

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

#import app_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    #app_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1(w)
    #app_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("600x450+510+155")
        top.title("AMLP-OBC")
        top.configure(background="#99cd4e")
        top.resizable(False, False)

        def commandword():
            print(v.get())
            commandword = v.get()
            process3.calculate(commandword)
            # app1report.create_New_Toplevel_1(Tk(),commandword)
            os.startfile(os.getcwd() + "\\data3\\report_" + str(commandword) + ".dat")

        v = StringVar()



        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.08, rely=0.09, relheight=0.06
                , relwidth=0.2)
        self.Radiobutton1.configure(activebackground="#d9d9d9")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify=LEFT)
        self.Radiobutton1.configure(text='''Command Word 1''')
        self.Radiobutton1.configure(command=commandword)
        self.Radiobutton1.configure(variable=v)
        self.Radiobutton1.configure(value='F820')

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.42, rely=0.11, relheight=0.03
                , relwidth=0.2)
        self.Radiobutton2.configure(activebackground="#d9d9d9")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify=LEFT)
        self.Radiobutton2.configure(text='''Command Word 2''')
        self.Radiobutton2.configure(command=commandword)
        self.Radiobutton2.configure(variable=v)
        self.Radiobutton2.configure(value='F840')

        self.Radiobutton3 = Radiobutton(top)
        self.Radiobutton3.place(relx=0.73, rely=0.09, relheight=0.06
                , relwidth=0.21)
        self.Radiobutton3.configure(activebackground="#d9d9d9")
        self.Radiobutton3.configure(activeforeground="#000000")
        self.Radiobutton3.configure(background="#d9d9d9")
        self.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton3.configure(foreground="#000000")
        self.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton3.configure(highlightcolor="black")
        self.Radiobutton3.configure(justify=LEFT)
        self.Radiobutton3.configure(text='''Command Word 3''')
        self.Radiobutton3.configure(command=commandword)
        self.Radiobutton3.configure(variable=v)
        self.Radiobutton3.configure(value='F860')

        self.Radiobutton4 = Radiobutton(top)
        self.Radiobutton4.place(relx=0.08, rely=0.33, relheight=0.06
                , relwidth=0.21)
        self.Radiobutton4.configure(activebackground="#d9d9d9")
        self.Radiobutton4.configure(activeforeground="#000000")
        self.Radiobutton4.configure(background="#d9d9d9")
        self.Radiobutton4.configure(disabledforeground="#a3a3a3")
        self.Radiobutton4.configure(foreground="#000000")
        self.Radiobutton4.configure(highlightbackground="#d9d9d9")
        self.Radiobutton4.configure(highlightcolor="black")
        self.Radiobutton4.configure(justify=LEFT)
        self.Radiobutton4.configure(text='''Command Word 4''')
        self.Radiobutton4.configure(command=commandword)
        self.Radiobutton4.configure(variable=v)
        self.Radiobutton4.configure(value='F880')

        self.Radiobutton5 = Radiobutton(top)
        self.Radiobutton5.place(relx=0.42, rely=0.33, relheight=0.06
                , relwidth=0.2)
        self.Radiobutton5.configure(activebackground="#d9d9d9")
        self.Radiobutton5.configure(activeforeground="#000000")
        self.Radiobutton5.configure(background="#d9d9d9")
        self.Radiobutton5.configure(disabledforeground="#a3a3a3")
        self.Radiobutton5.configure(foreground="#000000")
        self.Radiobutton5.configure(highlightbackground="#d9d9d9")
        self.Radiobutton5.configure(highlightcolor="black")
        self.Radiobutton5.configure(justify=LEFT)
        self.Radiobutton5.configure(text='''Command Word 5''')
        self.Radiobutton5.configure(command=commandword)
        self.Radiobutton5.configure(variable=v)
        self.Radiobutton5.configure(value='F8A0')


        self.Radiobutton6 = Radiobutton(top)
        self.Radiobutton6.place(relx=0.73, rely=0.33, relheight=0.06
                , relwidth=0.2)
        self.Radiobutton6.configure(activebackground="#d9d9d9")
        self.Radiobutton6.configure(activeforeground="#000000")
        self.Radiobutton6.configure(background="#d9d9d9")
        self.Radiobutton6.configure(disabledforeground="#a3a3a3")
        self.Radiobutton6.configure(foreground="#000000")
        self.Radiobutton6.configure(highlightbackground="#d9d9d9")
        self.Radiobutton6.configure(highlightcolor="black")
        self.Radiobutton6.configure(justify=LEFT)
        self.Radiobutton6.configure(text='''Command Word 6''')
        self.Radiobutton6.configure(command=commandword)
        self.Radiobutton6.configure(variable=v)
        self.Radiobutton6.configure(value='F8C0')

        self.Radiobutton7 = Radiobutton(top)
        self.Radiobutton7.place(relx=0.08, rely=0.58, relheight=0.06
                , relwidth=0.2)
        self.Radiobutton7.configure(activebackground="#d9d9d9")
        self.Radiobutton7.configure(activeforeground="#000000")
        self.Radiobutton7.configure(background="#d9d9d9")
        self.Radiobutton7.configure(disabledforeground="#a3a3a3")
        self.Radiobutton7.configure(foreground="#000000")
        self.Radiobutton7.configure(highlightbackground="#d9d9d9")
        self.Radiobutton7.configure(highlightcolor="black")
        self.Radiobutton7.configure(justify=LEFT)
        self.Radiobutton7.configure(text='''Command Word 7''')
        self.Radiobutton7.configure(variable=v)
        self.Radiobutton7.configure(value='F8E0')

        self.Radiobutton8 = Radiobutton(top)
        self.Radiobutton8.place(relx=0.42, rely=0.58, relheight=0.06
                , relwidth=0.2)
        self.Radiobutton8.configure(activebackground="#d9d9d9")
        self.Radiobutton8.configure(activeforeground="#000000")
        self.Radiobutton8.configure(background="#d9d9d9")
        self.Radiobutton8.configure(disabledforeground="#a3a3a3")
        self.Radiobutton8.configure(foreground="#000000")
        self.Radiobutton8.configure(highlightbackground="#d9d9d9")
        self.Radiobutton8.configure(highlightcolor="black")
        self.Radiobutton8.configure(justify=LEFT)
        self.Radiobutton8.configure(text='''Command Word 8''')
        self.Radiobutton8.configure(variable=v)
        self.Radiobutton8.configure(value='F8F0')

        self.Radiobutton9 = Radiobutton(top)
        self.Radiobutton9.place(relx=0.73, rely=0.58, relheight=0.06
                , relwidth=0.21)
        self.Radiobutton9.configure(activebackground="#d9d9d9")
        self.Radiobutton9.configure(activeforeground="#000000")
        self.Radiobutton9.configure(background="#d9d9d9")
        self.Radiobutton9.configure(disabledforeground="#a3a3a3")
        self.Radiobutton9.configure(foreground="#000000")
        self.Radiobutton9.configure(highlightbackground="#d9d9d9")
        self.Radiobutton9.configure(highlightcolor="black")
        self.Radiobutton9.configure(justify=LEFT)
        self.Radiobutton9.configure(text='''Command Word 9''')
        self.Radiobutton9.configure(variable=v)
        self.Radiobutton9.configure(value='F800')

        self.Radiobutton10 = Radiobutton(top)
        self.Radiobutton10.place(relx=0.42, rely=0.82, relheight=0.06
                , relwidth=0.21)
        self.Radiobutton10.configure(activebackground="#d9d9d9")
        self.Radiobutton10.configure(activeforeground="#000000")
        self.Radiobutton10.configure(background="#d9d9d9")
        self.Radiobutton10.configure(disabledforeground="#a3a3a3")
        self.Radiobutton10.configure(foreground="#000000")
        self.Radiobutton10.configure(highlightbackground="#d9d9d9")
        self.Radiobutton10.configure(highlightcolor="black")
        self.Radiobutton10.configure(justify=LEFT)
        self.Radiobutton10.configure(text='''Command Word 10''')
        self.Radiobutton10.configure(variable=v)
        self.Radiobutton10.configure(value='F810')






if __name__ == '__main__':
    vp_start_gui()



