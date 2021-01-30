import numpy as np
# from secrets import choice
from time import time, gmtime, localtime, sleep, strftime
from math import pi, sin, cos
from tkinter import Tk, Canvas, PhotoImage, mainloop, messagebox, FIRST, LAST

#globals
#window (canvas) size
w_width = 200
w_height = 200
#window background color
w_bkgr = 'black'
#fps counters
curtime, newtime = '', ''
curtime_sec, newtime_sec = 0, 0

v1 = (w_width/2,w_height/2)
v2 = np.array([w_width/2+30, w_height/2-30])

def startup():
	print(f'[*] Startup')
		
	pass


def main():
	root = Tk()
	root.title('shitty cloock 00')
	root.geometry(f'{w_width+5}x{w_height+5}')
	# root.resizable(0, 0)
	c = Canvas(root, width=w_width, height=w_height, bg=w_bkgr)
	c.pack()

	curtime = strftime('%H:%M:%S')
	# curtime_sec = time()
	grad, tick = 0, 0
	
	#animatronics block
	#TODO precalculated area
	MARK_STEP = 30
	#Hour mark size
	MARK_SIZE = 3
	#Minute mark size
	MMARK_SIZE = 1
	MARK_DIST = 35
	h_marks = []
	m_marks = []
	for mark in range(1, 361, MARK_STEP):
		#+14 add Clock degree orientaion
		rad = (mark+14) * pi / 180
		
		xm = MARK_DIST*cos(rad)-MARK_DIST*sin(rad)
		ym = MARK_DIST*cos(rad)+MARK_DIST*sin(rad)
		#transfer
		ym += 100
		xm += 100
		c.create_oval(xm-MARK_SIZE, ym-MARK_SIZE, xm+MARK_SIZE, ym+MARK_SIZE, fill='white')		
		h_marks.append((rad, xm, ym))
		m_marks.append((rad, xm, ym))

		#draw minutes marks
		for mm_marks in range(1,5):
			#minute mark stepz
			mm_step = (MARK_STEP / 5) * mm_marks
			rad = (mark+14+mm_step) * pi /180
			xm = MARK_DIST*cos(rad)-MARK_DIST*sin(rad)
			ym = MARK_DIST*cos(rad)+MARK_DIST*sin(rad)
			#transfer
			ym += 100
			xm += 100
			c.create_oval(xm-MMARK_SIZE, ym-MMARK_SIZE, 
						  xm+MMARK_SIZE, ym+MMARK_SIZE, fill='white')		
			m_marks.append((rad, xm, ym))

	print(f'[**] Size of h_marks {len(h_marks)}')
	print(f'[**] Size of m_marks {len(m_marks)}')

	#coor lines
	# c.create_line(w_width/2, 0, w_width/2, w_height, arrow=FIRST, fill=f_white)
	# c.create_line(0, w_height/2, w_width, w_height/2, arrow=LAST, fill=f_white)
	# c.create_text(w_width/2+15, 0+5, text='Y', fill=f_white)
	# c.create_text(w_width-15, w_height/2+5, text='X', fill=f_white)

	while True:
		 
		#http://www.gamedev.ru/code/forum/?id=43830#:~:text=x1%3Dx*cos(angle,)%2Dx*sin(angle)%3B
		#https://compgraphics.info/2D/matrix_rotate.php
		#https://www.youtube.com/watch?v=OYuoPTRVzxY
		# rad = grad * pi / 180

		# X = x * cos(a) - y * sin(a);
		# Y = y * cos(a) + x * sin(a);
		#
		#cw
		# xn = 30*cos(rad)+30*sin(rad)
		# yn = (-1)*30*sin(rad)+30*cos(rad)
		#ccw
		# xn = 30*cos(rad)-30*sin(rad)
		# yn = 30*cos(rad)+30*sin(rad)
		#tranfer
		# yn += 100
		# xn += 100
		
		hh = localtime(time()).tm_hour
		mm = localtime(time()).tm_min
		ss = localtime(time()).tm_sec

		if hh > 12:
			hh -= 12

		H = h_marks[hh-5]
		M = m_marks[mm-25]
		S = m_marks[ss-25]

		c.create_line(v1,(H[1],H[2]),arrow=LAST, fill='white', width=2, tag='clock_hand')
		c.create_line(v1,(M[1],M[2]),arrow=LAST, fill='white', tag='clock_hand')
		c.create_line(v1,(S[1],S[2]),arrow=LAST, fill='white', tag='clock_hand')

		
		if grad < 360:
			grad += 1
		else:  
			grad = 0
		
		#update
		c.update()
		c.delete('clock_hand')
		
		tick += 1 
		newtime = strftime('%H:%M:%S')
		# newtime_sec = time()
		if newtime != curtime:
		 	curtime = newtime
		 	print(f'[**] FPS {tick}')
		 	tick = 0
			 
		pass

	# end
	# root.mainloop()
	pass

if __name__ == '__main__':
	startup()
	main()
   