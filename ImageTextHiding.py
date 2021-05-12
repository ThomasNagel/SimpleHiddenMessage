from PIL import Image

im = Image.open("CuteCat.png")
pix = im.load()
x, y = im.size

filename = input("Please enter a png filename (same directory):")
im = Image.open(filename)
pix = im.load()
x, y = im.size

mode = input("Read Image (r)\nWrite Image(w)\n>")

if mode == "w":
	print("Writing selected")

	input_text = input("Enter a message:")

	t_index = 0

	stop = False
	for x_px in range(x):
		if stop:
			break
		for y_px in range(y):
			if(pix[x_px, y_px][3] != 0):
				if t_index >= len(input_text): #set all last numbers to 0 example: (230, 30, 120, 255)
					pix[x_px, y_px] = (pix[x_px, y_px][0] - pix[x_px, y_px][0] % 10, pix[x_px, y_px][1] - pix[x_px, y_px][1] % 10, pix[x_px, y_px][2] - pix[x_px, y_px][2] % 10, pix[x_px, y_px][3])
					stop = True
					break
				ascii_num = ord(input_text[t_index])
				pix[x_px, y_px] = (pix[x_px, y_px][0] - pix[x_px, y_px][0] % 10 + (ascii_num // 100 % 10), pix[x_px, y_px][1] - pix[x_px, y_px][1] % 10 + (ascii_num // 10 % 10) - 10 * (ascii_num // 10 % 10 > 5 and pix[x_px, y_px][1] >= 250), pix[x_px, y_px][2] - pix[x_px, y_px][2] % 10 + (ascii_num % 10) - 10 * (ascii_num % 10 > 5 and pix[x_px, y_px][2] >= 250), pix[x_px, y_px][3])
				t_index = t_index + 1

	new_filename = input("Please enter a new png filename:")
	im.save(new_filename)


elif mode == "r":
	print("Reading selected")

	message = str()

	stop = False

	for x_px in range(x):
		if stop:
			break
		for y_px in range(y):
			if(pix[x_px, y_px][3] != 0):
				num = pix[x_px, y_px][0] % 10 * 100 + pix[x_px, y_px][1] % 10 * 10 + pix[x_px, y_px][2] % 10
				if num == 0:
					stop = True
					break
				elif num <= 255:
					message = message + chr(num)

	print(message)

else:
	print("Error, wrong input")
