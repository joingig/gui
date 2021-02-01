import numpy as np
from secrets import choice
from time import time, gmtime, localtime, sleep, strftime
#from math import pi, sin, cos
from tkinter import Tk, Canvas, Label, PhotoImage, mainloop, messagebox, TclError

#globals
#window (canvas) size
w_width = 220
w_height = 220

#app
#color_converter = '#%02x%02x%02x' % (64, 204, 208)
purple = '#%02x%02x%02x' % (138, 43, 226)
bkgr = '#%02x%02x%02x' % (230, 230, 250)

RSIZE = [5,8,11]
RSPEED = [0.2,0.4,0.6]
RDROPS = 100

drops = []

#fps helpers
tick = 0
curtime, newtime = '', ''
curtime_sec, newtime_sec = 0, 0

def startup():
    print(f'[*] Startup')
    pass

def main():
    root = Tk()
    root.title('rainy 00')
    root.geometry(f'{w_width+5}x{w_height+5}')
    root.resizable(0, 0)
    c = Canvas(root, width=w_width, height=w_height)
    c.pack()
    try:
        bkgr_img = PhotoImage(file = 'E:\\GDrive\\rainy_city_night2.png')
        c.create_image(0, 0, image=bkgr_img, anchor='nw')
    except TclError as er:
        print(f'[*] Can\'t open background image.')
        messagebox.showerror(title='Error', message='Can\'t open background image.')
        pass

    curtime = strftime('%H:%M:%S')

    #animatronics block
    for d in range(1,RDROPS):
        drops.append(dict())
        drops[-1]['x'] = choice(range(2, w_width-2))
        drops[-1]['y'] = choice(range(2, int(w_height/2)))
        drops[-1]['size'] = choice(RSIZE)
        speed_index = RSIZE.index(drops[-1]['size'])
        drops[-1]['speed'] = RSPEED[speed_index]

    def rain():

        hh = localtime(time()).tm_hour
        mm = localtime(time()).tm_min
        ss = localtime(time()).tm_sec

        #draw
        for dr in drops:
            speed_index = RSIZE.index(drops[-1]['size'])
            c.create_line(dr['x'], dr['y'],
                          dr['x'], dr['y']+dr['size'], fill=purple, width=speed_index, tag='drop')
            # dr['speed'] += 0.005
            dr['y'] += dr['speed']
            if dr['y'] > w_height:
                dr['y'] = choice(range(2, int(w_height/2)))
                dr['x'] = choice(range(2, w_width-2))
                drops[-1]['size'] = choice(RSIZE)
                speed_index = RSIZE.index(drops[-1]['size'])
                drops[-1]['speed'] = RSPEED[speed_index]

        #fps counter
        global newtime
        global curtime
        global tick
        tick += 1
        newtime = strftime('%H:%M:%S')
        if newtime != curtime:
            curtime = newtime
            print(f'\r[**] FPS {tick}', end='')
            tick = 0
		
        #update
        c.update()
        c.delete('drop')
        c.after(0, rain)

        #ens of clock()	 
        pass

    rain()
    root.mainloop()
    # end main()
    pass

if __name__ == '__main__':
    startup()
    main()

#based on https://www.youtube.com/watch?v=KkyIDI6rQJI  Coding Challenge #4: Purple Rain in Processing