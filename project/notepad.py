# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:29:45 2019

@author: Nishu Sharma
"""

from tkinter import *
from tkinter import Menu
 
window = Tk()
T = Text(window, height=200, width=300)
T.pack()
T.insert(END, "")
 
window.title("Notepad")
 
menu = Menu(window)
new_item = Menu(menu)
new2_item = Menu(menu)
new3_item = Menu(menu)
new4_item = Menu(menu)
new5_item = Menu(menu)
 
new_item.add_command(label='New        Ctrl+N') 
new_item.add_command(label='open        Ctrl+O')
new_item.add_command(label='Save        Ctrl+S')
new_item.add_command(label='Save as') 
new_item.add_command(label='page Satup')
new_item.add_command(label='print        Ctrl+p')
new_item.add_command(label='Exit')
menu.add_cascade(label='File', menu=new_item)


new2_item.add_command(label='Undo     Ctrl+Z')
new2_item.add_command(label='Cut     Ctrl+x')
new2_item.add_command(label='copy     Ctrl+c')
new2_item.add_command(label='Paste     Ctrl+v')
new2_item.add_command(label='Delete     Del')
new2_item.add_command(label='Search with Bing     Ctrl+E ')
new2_item.add_command(label='Find     Ctrl+F')
new2_item.add_command(label='Find next     F3')
new2_item.add_command(label='Replace     Ctrl+H')
new2_item.add_command(label='Go to     Ctrl+G')
new2_item.add_command(label='Select All     Ctrl+A')
new2_item.add_command(label='Time / date     F5')
menu.add_cascade(label='Edit', menu=new2_item)



new3_item.add_command(label='Word Warp')
new3_item.add_command(label='Font..')
menu.add_cascade(label='Format', menu=new3_item)


new4_item.add_command(label='Zoom')
new4_item.add_command(label='Status bar')
menu.add_cascade(label='View', menu=new4_item)



new5_item.add_command(label=' View Help')
new5_item.add_command(label=' About Notepad')
menu.add_cascade(label='Help', menu=new5_item)
 
window.config(menu=menu)
 
window.mainloop()