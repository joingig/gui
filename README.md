# gui

Random gui and graphics algo snippets.

- DOOM [fire](fir00.py) algorithm. python3, tk.
  
  ![](./imgs/fir00.png)
  
  or with little bit improvments:
  
  ```python
  #TODO burn!
  for x in range(0, w_width, 3):
      for y in range(0, w_height, 3):
          if fire[y*w_height+x] > 0:
              spreadFire(y*w_height+x)
  ```
  
  ![](./imgs/fir01.png)

- junk looking [clock](clock00.py). python3, tk.
  
  ![](./imgs/klock.png)
