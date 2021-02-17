import numpy as np
# from numba import jit
from secrets import choice
#from operator import itemgetter, attrgetter
from time import time, gmtime, localtime, sleep, strftime
from math import pi, sin
from tkinter import Tk, Canvas, Label, PhotoImage, mainloop, messagebox, TclError

#globals
#window (canvas) size
w_width = 220
w_height = 220

#app
#color_converter = '#%02x%02x%02x' % (64, 204, 208)
purple = '#%02x%02x%02x' % (138, 43, 226)
bkgr = '#%02x%02x%02x' % (230, 230, 250)

SNOWFLAKES = 100

class Fps:
    ticks = 0
    curtime, newtime = '', ''
    def __init__(self):
        self.curtime = strftime('%H:%M:%S')
        pass

    def update(self):
        self.ticks += 1
        self.newtime = strftime('%H:%M:%S')
        if self.newtime != self.curtime:
            print(f'\r[**] FPS:{self.ticks}', end='')
            self.curtime = self.newtime
            self.ticks = 0
    
    #class Fps
    pass

class SnowFlake:
    color = 'white'
    canvas_div = 4
    def __init__(self):

        self.pos = np.array([0.0, 0.0])
        self.vel = np.array([0.0, 0.05])
        self.acc = np.array([0.0, 0.0])
        self.gravity = np.array([0.0, 0.00001])

        self.size = choice(range(3,10))
         
        self.pos[0] = choice(range(2, w_width-2))
        self.pos[1] = choice(range(2, int(w_height/self.canvas_div)))
        
        self.angle = choice(range(0, 360))
        self.xoff = 0.0
        

        pass

    def applyForce(self, force):
        """
        applyForce
        add force to acceleration
        """
        # f = force
        # f *= self.size
        self.acc = force * self.size
        pass
    
    def render(self, canvas):
        """
        render snowflake
        """
        canvas.create_oval(self.pos[0]+self.xoff, self.pos[1],
                            self.pos[0]+self.xoff+self.size, self.pos[1]+self.size, fill=self.color, tag='drop')    
        
        pass
    
    def update(self):
        """
        update x y pos , do some math
        """

        self.applyForce(self.gravity)
             
        self.vel += self.acc 
        self.pos += self.vel 

        self.angle += 1 / self.size
        self.xoff = sin(self.angle * pi / 180) * self.size
        # print(f'xoff --> {self.xoff}')

        if self.pos[1] > w_height:
            self.x = choice(range(2, w_width-2))
            self.y = choice(range(2, int(w_height/self.canvas_div)))
            self.pos[0] = self.x
            self.pos[1] = self.y    
            #reset  
            self.vel[1] = 0.05
            self.acc = [0, 0]
            self.size = choice(range(3,10))
            self.angle = 0

        pass
    
    #class SnowFlake
    pass

#based on Coding Challenge #88: Snowfall
snow = []

fps = Fps()

def startup():
    print(f'[*] Startup')
    pass

def main():
    root = Tk()
    root.title('snow00')
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

    #make snow

    for d in range(0,SNOWFLAKES):
        sf_new = SnowFlake()
        snow.append(sf_new)


    #@jit(nopython=False)
    def snowwow():
        #draw
        #TODO sort by SSIZE , smalest FIRST
        #draw small first 
        sorted_snow = sorted(snow, key=lambda _snow: _snow.size)

        for dr in sorted_snow:
            dr.render(canvas=c)
            dr.update()
                   
        fps.update()
        
        #update
        c.update()
        c.delete('drop')
        c.after(0, snowwow)

        #ens of clock()	 
        pass

    snowwow()
    root.mainloop()
    # end main()
    pass

if __name__ == '__main__':
    startup()
    main()

#based on https://www.youtube.com/watch?v=cl-mHFCGzYk  Coding Challenge #88: Snowfall