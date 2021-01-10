# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 10:26:54 2021

@author: Clara
"""


import copy
 
with open(r"..\Inputs\08.txt") as file:
    data = list(map(int, file.read()))
 
layerSize = 25*6
numberOfLayers = len(data)/layerSize
 
layers = []
layerN = []
image = []
 
#get a two-dimensional array that represents the image at each layer
for j in range(len(data)):
    layerN.append(data[j])
    if((j+1)%layerSize == 0):
        if(j!=0):
            layers.append(copy.copy(layerN))
            layerN.clear()
 
#For each pixel, search each layer for the top-most visible color
#and append it to the resulting image array
for x in range(layerSize):
    for y in layers:
        if(y[x]==2):
            continue
        elif(y[x]==1):
            image.append("#")
            break
        elif(y[x]==0):
            image.append(" ")
            break
 
for z in range(len(image)):
    if((z+1)%25 == 0):
        print(image[z])
    else:
        print(image[z], end=" ")