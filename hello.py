from tkinter import *

def click_pattern_1():
    print('You selected pattern 1')


window = Tk()
window.geometry("500x500")
window.title("Digital Technologies Developmemt Limited")

label_pattern_selector = Label(window, 
    text="Choose a pattern", 
    font=('Arial', 40, 'bold'), 
    fg='green', 
    bg='black')

label_pattern_selector.pack()
label_pattern_selector.place(x=0, y=0)

button_pattern_1 = Button(window,
    text='Select pattern 1',
    command=click_pattern_1,
    font=('Arial', 30),
    fg='green',
    bg='black')

button_pattern_1.pack()
button_pattern_1.place(x=100, y=100)

entry_pattern_selectiob = Entry(window, 
    font=('Arial', 30)
    )

entry_pattern_selectiob.pack()
entry_pattern_selectiob.place(x=200, y=200)


window.mainloop()