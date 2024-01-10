import tkinter
import tkinter.messagebox

class MyGUI:
	def __init__(self):

		self.main_window = tkinter.Tk()
		self.bottom_frame = tkinter.Frame(self.main_window)

		self.my_button = tkinter.Button(self.bottom_frame,
									text='Show Info',
									command=self.do_something)

		self.quit_button = tkinter.Button(self.bottom_frame,
									text='Quit',
									command=self.main_window.destroy)

		self.my_button.pack(side = 'left')
		self.quit_button.pack(side = 'left')

		self.bottom_frame.pack()

		tkinter.mainloop()

	def do_something(self):
		tkinter.messagebox.showinfo('Response',
								'Steven Marcus\n274 Baily Drive\nWaynesvill, NC 27999')

my_gui = MyGUI()
