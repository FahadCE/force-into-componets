# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 19:37:25 2020

@author: FAHAD ANEES
"""

import math as m
def baseComponent(F,theta):
    fx=F*m.cos(theta*(m.pi)/180)
    fy=F*m.sin(theta*(m.pi)/180)
    print('fx='+str(round(fx,2)))
    print('fy='+str(round(fy,2)))
    
    # want to know more visit the following link
    # https://www.youtube.com/watch?v=0NeXcc_B9_o&list=PLHZy9r1OiTUda2KcyDBVHdVKoMwaNjxB-&index=6
