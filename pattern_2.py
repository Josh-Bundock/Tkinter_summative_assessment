from tkinter import *
window = Tk()

canvas_pattern_2 = Canvas(window, height=500, width=500)

canvas_pattern_2.create_oval(0, 0, 100, 100, fill='purple', width=0)
canvas_pattern_2.create_oval(100, 0, 200, 100, fill='white')
canvas_pattern_2.create_oval(200, 0, 300, 100, fill='purple', width=0)
canvas_pattern_2.create_oval(300, 0, 400, 100, fill='white')
canvas_pattern_2.create_oval(400, 0, 500, 100, fill='purple', width=0)

canvas_pattern_2.create_oval(0, 100, 100, 200, fill='white')
canvas_pattern_2.create_oval(100, 100, 200, 200, fill='purple', width=0)
canvas_pattern_2.create_oval(200, 100, 300, 200, fill='white')
canvas_pattern_2.create_oval(300, 100, 400, 200, fill='purple', width=0)
canvas_pattern_2.create_oval(400, 100, 500, 200, fill='white')

canvas_pattern_2.create_oval(0, 200, 100, 300, fill='purple', width=0)
canvas_pattern_2.create_oval(100, 200, 200, 300, fill='white')
canvas_pattern_2.create_oval(200, 200, 300, 300, fill='purple', width=0)
canvas_pattern_2.create_oval(300, 200, 400, 300, fill='white')
canvas_pattern_2.create_oval(400, 200, 500, 300, fill='purple', width=0)

canvas_pattern_2.create_oval(0, 300, 100, 400, fill='white')
canvas_pattern_2.create_oval(100, 300, 200, 400, fill='purple', width=0)
canvas_pattern_2.create_oval(200, 300, 300, 400, fill='white')
canvas_pattern_2.create_oval(300, 300, 400, 400, fill='purple', width=0)
canvas_pattern_2.create_oval(400, 300, 500, 400, fill='white')

canvas_pattern_2.create_oval(0, 400, 100, 500, fill='purple', width=0)
canvas_pattern_2.create_oval(100, 400, 200, 500, fill='white')
canvas_pattern_2.create_oval(200, 400, 300, 500, fill='purple', width=0)
canvas_pattern_2.create_oval(300, 400, 400, 500, fill='white')
canvas_pattern_2.create_oval(400, 400, 500, 500, fill='purple', width=0)

canvas_pattern_2.pack()
window.mainloop()