import tkinter

class HorizontalScrollbarExample:
	def __init__(self):
		self.main_window = tkinter.Tk()

		self.listbox_frame = tkinter.Frame(self.main_window)
		self.listbox_frame.pack(padx = 20, pady = 20)

		self.listbox = tkinter.Listbox(
			self.listbox_frame, height = 0, width = 30)
		self.listbox.pack(side = 'top')
		self.scrollbar = tkinter.Scrollbar(
			self.listbox_frame, orient = tkinter.HORIZONTAL)
		self.scrollbar.pack(side = 'bottom', fill = tkinter.X)

		self.scrollbar.config(command = self.listbox.xview)
		self.listbox.config(xscrollcommand = self.scrollbar.set)

		data = [
			'The Burj Khalifa building is 2717 feet tall. ',
			'The Shanghai Tower is 2073 feet tall.',
			'The Abraj Al-Bait Clock Tower is 1971 feet tall.'
			'The Ping An Finance Center is 1965 feet tall.']

		for element in data:
			self.listbox.insert(tkinter.END, element)

		tkinter.mainloop()
if __name__ == '__main__':
	scrollbar_example = HorizontalScrollbarExample()


