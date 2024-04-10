from tkinter import *
window = Tk()

canvas_pattern_9 = Canvas(window, height=500, width=500, bg='white')

canvas_pattern_9.create_polygon(0,0,0,50,250,250, fill='purple')
canvas_pattern_9.create_polygon(0,90,0,140,250,250, fill='purple')
canvas_pattern_9.create_polygon(0,200,0,250,250,250, fill='purple')
canvas_pattern_9.create_polygon(0,250,0,300,250,250, fill='purple')
canvas_pattern_9.create_polygon(0,350,0,400,250,250, fill='purple')
canvas_pattern_9.create_polygon(0,500,0,450,250,250, fill='purple')

canvas_pattern_9.create_polygon(500,0,500,50,250,250, fill='purple')
canvas_pattern_9.create_polygon(500,90,500,140,250,250, fill='purple')
canvas_pattern_9.create_polygon(500,200,500,250,250,250, fill='purple')
canvas_pattern_9.create_polygon(500,250,500,300,250,250, fill='purple')
canvas_pattern_9.create_polygon(500,350,500,400,250,250, fill='purple')
canvas_pattern_9.create_polygon(500,500,500,450,250,250, fill='purple')

canvas_pattern_9.create_polygon(0,0,50,0,250,250, fill='purple')
canvas_pattern_9.create_polygon(90,0,140,0,250,250, fill='purple')
canvas_pattern_9.create_polygon(200,0,250,0,250,250, fill='purple')
canvas_pattern_9.create_polygon(250,0,300,0,250,250, fill='purple')
canvas_pattern_9.create_polygon(350,0,400,0,250,250, fill='purple')
canvas_pattern_9.create_polygon(500,0,450,0,250,250, fill='purple')

canvas_pattern_9.create_polygon(0,500,50,500,250,250, fill='purple')
canvas_pattern_9.create_polygon(90,500,140,500,250,250, fill='purple')
canvas_pattern_9.create_polygon(200,500,250,500,250,250, fill='purple')
canvas_pattern_9.create_polygon(250,500,300,500,250,250, fill='purple')
canvas_pattern_9.create_polygon(350,500,400,500,250,250, fill='purple')
canvas_pattern_9.create_polygon(500,500,450,500,250,250, fill='purple')

canvas_pattern_9.create_oval(245,245,255,255, fill='white')
canvas_pattern_9.create_line(0,250,500,250, fill='white', width=2)
canvas_pattern_9.create_line(250,0,250,500, fill='white', width=2)

canvas_pattern_9.pack()
window.mainloop()