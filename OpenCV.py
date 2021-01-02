#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 19:15:29 2021

@author: srilthe
"""

import numpy as np
import cv2
import gtk3



# image = cv2.imread('checkerboard.png')


image = gtk3.gdk.pixbuf_new_from_file()

cv2.imshow('Hey look at me!', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


