#!/usr/bin/python3.2
#
# PiTFT_test1.py
#
# Try to figure out how to put output to the PiTFT screen.

# import
import os
import pygame
import time

class pyscope :
   screen = None;

   def __init__(self):
      disp_no = os.getenv("DISPLAY")
      if disp_no:
         print("I'm running under X display = {0}".format(disp_no))

      drivers = ['fbcon','directfb','svgalib']
      found = False
      for driver in drivers:
         if not os.getenv('SDL_VIDEODRIVER'):
            os.putenv('SDL_VIDEODRIVER', driver)
         try:
            pygame.display.init()
         except pygame.error:
            print('Driver: {0} failed.'.format(driver))
            continue
         found = True
         break

      if not found:
         raise Exception('No suitable video driver found!')

      #size = width, height = 320, 240
      size = (320, 240)
      print("Framebuffer size {0} x {1} ".format(size[0],size[1]))
      self.screen = pygame.display.set_mode(size)
      #clear the screen to start
      gray = 192, 192, 192
      self.screen.fill(gray)
      pygame.font.init()
      #render the screen
      pygame.display.update()

   def __del__(self):
      "Destructor to make sure pygame shuts down, etc"

   def test(self):
      # Fill the screen with Red
      red= 255,0,0
      self.screen.fill(red)
      # Update the display
      pygame.display.update()
  
# Create an instance of the PyScope class
scope = pyscope()
time.sleep(10)
scope.test()
time.sleep(10)


