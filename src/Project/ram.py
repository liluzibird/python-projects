ram = bytearray(100)

def write(position, buffer): #ram position
	ram[position:position+len(buffer)] = buffer

def read(position, length): #read from ram position
	return ram[position:position+length]

def main():

	inp = input("Enter your input here: ") #user input
	write(0, inp.encode("ASCII")) #write user input to ram position 0
	print(read(0, len(inp)).decode("ASCII")) #read user input at ram position 0

main()


#https://stackoverflow.com/questions/59320564/how-to-access-and-change-color-channels-using-pil
#https://towardsdatascience.com/image-manipulation-in-python-cbb86a61cf0
