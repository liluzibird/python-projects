import tkinter

class MyGUI:
	def __init__(self):

		self.main_window = tkinter.Tk()

		self.label = tkinter.Label(self.main_window, text = "Hello World!")
		self.labelFirstname = tkinter.Label(self.main_window, text = "John")
		self.labelLastname = tkinter.Label(self.main_window, text = "Doe")
		self.labelAge = tkinter.Label(self.main_window, text = "21")


		self.label.pack()
		self.labelFirstname.pack()
		self.labelLastname.pack()
		self.labelAge.pack()

		tkinter.mainloop()

if __name__ == '__main__':
	my_gui = MyGUI()