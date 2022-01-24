# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 15:15:50 2021

@author: Bence Mány
"""
import matplotlib.pyplot as plt 
import numpy as np

inp = open("test\\test0902_8.csv", "r")   

L = []
L = inp.read().splitlines()
for i in range(len(L)):
    L[i] = list(map(float, L[i].split(" ")))
inp.close()


K = []
for i in L:
    print(i)
    K.append(i)


plt.plot(K)
plt.legend(["pitch", "roll", "yaw", "0", "1", "2", "3"])
plt.show()