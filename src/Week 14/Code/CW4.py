import tkinter
import tkinter.messagebox

class MyGUI:

	def __init__(self):
		self.main_window = tkinter.Tk()

		self.my_button = tkinter.Button(self.main_window,
										text = 'Click Me!',
										command = self.do_something)
		self.my_button_quote1 = tkinter.Button(self.main_window,
										text = 'Quote1',
										command = self.quote1)
		self.my_button_quote2 = tkinter.Button(self.main_window,
										text = 'Quote2',
										command = self.quote2)
		self.my_button_quote3 = tkinter.Button(self.main_window,
										text = 'Quote3',
										command = self.quote3)
		self.quit_button = tkinter.Button(self.main_window,
										text = 'Quit',
										command = self.main_window.destroy)
		self.my_button.pack()
		self.my_button_quote1.pack()
		self.my_button_quote2.pack()
		self.my_button_quote3.pack()
		self.quit_button.pack()

		tkinter.mainloop()

	def do_something(self):
		tkinter.messagebox.showinfo('Response',
									'Thanks for clicking the button.')
	def quote1(self):
		tkinter.messagebox.showinfo('Response',
									'You can do it!')
	def quote2(self):
		tkinter.messagebox.showinfo('Response',
									'I believe in you!')
	def quote3(self):
		tkinter.messagebox.showinfo('Response',
									'Nothing is impossible!')
if __name__ == '__main__':
	my_gui = MyGUI()