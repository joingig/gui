#import numpy
from secrets import choice
from time import time, sleep, strftime
from tkinter import Tk, Canvas, PhotoImage, mainloop, messagebox

#globals
#window (canvas) size
w_width = 200
w_height = 200
#window background color
w_bkgr = 'black'
#fps counters
curtime, newtime = '', ''
curtime_sec, newtime_sec = 0, 0

# palette = []
f_palette = [
'#070707',   #rich black fogra \ modern name 
'#1f0707',
'#2f0f07',
'#470f07',
'#571707',
'#671f07',
'#771f07',
'#8f2707',
'#9f2f07',
'#af3f07',
'#bf4707',
'#c74707',
'#DF4F07',
'#DF5707',
'#DF5707',
'#D75F07',
'#D7670F',
'#cf6f0f',
'#cf770f',
'#cf7f0f',
'#CF8717',
'#C78717',
'#C78F17',
'#C7971F',
'#BF9F1F',
'#BF9F1F',
'#BFA727',
'#BFA727',
'#BFAF2F',
'#B7AF2F',
'#B7B72F',
'#B7B737',
'#CFCF6F',
'#DFDF9F',
'#EFEFC7',
'#FFFFFF'    # mr. White
]

fire = []

#bit of precalculatings
f_white = f_palette[-1]
f_black = f_palette[0]
p_len = len(f_palette)
# f_len = 0

def startup():
	print(f'[*] Startup')
	print(f'[*] Creatign arrays')

	print(f'[*] size of fix DOOM f_palette {len(f_palette)}')
	
	#init fire buf/list with black       fire buf store palette indeces
	for pf in range(0,w_width*w_height):
		fire.append(0)   # palette[0] == black 

	f_len = len(fire)
	print(f'[*] size of fire {f_len}')
	
	pass

def main():

	root = Tk()
	root.title('fire00')
	root.geometry(f'{w_width+5}x{w_height+5}')
	# root.resizable(0, 0)
	c = Canvas(root, width=w_width, height=w_height, bg=f_black)
	c.pack()
	# img = PhotoImage(width=w_width, height=w_height)
	# c.create_image((w_width//2, w_height//2), image=img, state="normal")
    

	curtime = strftime('%H:%M:%S')
	# curtime_sec = time()
	tick = 0
	#animatronics block / Doom var
	def spreadFire(ffrom=0): 
		f_decay = choice([0,1,2,3])
		if fire[ffrom] - f_decay < 0:
			f_decay = 1
		to = ffrom - w_width
		fire[to] = fire[ffrom] - f_decay

	while True:
		
		#flush fire bootom with zeroes  (f_palette[0] == black)
		for pix in range(0, w_width):
			fire[w_width*(w_height-1)+pix] = 0
			fire[w_width*(w_height-3)+pix] = 0

		#step one: drop random fire pixels on bottom 
		for pix in range(0, w_width):
			if choice([0,1,2]) == 1:
				# f_palette[p_len -1] == f_white
				fire[w_width*(w_height-1)+pix] = p_len -1
				fire[w_width*(w_height-3)+pix] = p_len -1
			

		#TODO burn!
		for x in range(0, w_width):
			for y in range(0, w_height):
				if fire[y*w_height+x] > 0:
					spreadFire(y*w_height+x)
      
		#copy fire array 2 canvas
		for y in range(0, w_height, 2):
			for x in range(0, w_width, 2):
				if fire[y*w_height+x] != 0:
					# print(
					#  	f'fire[y*w_height+x] = {fire[y*w_height+x]},color from fire[y*w_height+x] : {f_palette[fire[y*w_height+x]]}'
					#  	)
					c.create_rectangle((x, y)*2, outline=f_palette[fire[y*w_height+x]])	
		
		#check pallete
		# h = 0
		# for color in  reversed(palette):
		# 	c.create_line(0,w_height-h,w_width,w_height-h,fill=color)
		# 	h += 3
		
		#speed test. generate bunch of random rectangles (1000rects ~20FPS)
		# for x in range(1,500):
		# 	x = choice(range(0,w_width))
		# 	y = choice(range(0,w_height))
		# 	c.create_rectangle((x,y)*2,outline="white")
		
		#update
		c.update()
		# root.update()
		# sleep(0.05)

		#clear 
		c.delete("all")
		
		tick += 1 
		newtime = strftime('%H:%M:%S')
		# newtime_sec = time()
		if newtime != curtime:
		 	curtime = newtime
		 	print(f'\r[**] FPS {tick}', end='')
		 	tick = 0

		# if (newtime_sec - curtime_sec) > 1:
		# 	curtime_sec = newtime_sec
		# 	print(f'[**] second loop ! FRS {tick}')
		# 	tick = 0
		
		# while True:
		pass 

	# end
	# root.mainloop()
	pass

if __name__ == '__main__':
	startup()
	main()

#doom fire https://fabiensanglard.net/doom_fire_psx/
#fire collection https://github.com/filipedeschamps/doom-fire-algorithm
#https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python
#color_converter = '#%02x%02x%02x' % (64, 204, 208)
#filename = (len(argv) > 1 and argv[1]) or 'ora-lp.gif' # name on cmdline?
#https://lodev.org/cgtutor/fire.html