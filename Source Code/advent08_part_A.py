# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 10:17:41 2021

@author: Clara
"""

# Sorry for the seperate parts, I couldn't be bothered to split it into functions.
# If I have time and find the will I'll fix it 

import copy

with open(r"..\Inputs\08.txt") as file:
    data = list(map(int, file.read()))


layerSize = 25 * 6
numberOfLayers = len(data)/layerSize
 
layers = []
layerN = []
 
#get a two-dimensional array that represents the image at each layer
for i in range(len(data)):
    layerN.append(data[i])
    if((i+1)%layerSize == 0):
        layers.append(copy.copy(layerN))
        layerN.clear()
 
fewestZeros = 150
selectLayer = []
 
#find the layer with the fewest zeros
for x in layers:
    count = 0
    for y in range(len(x)):
        if(x[y]==0):
            count += 1
    if(count<fewestZeros):
        fewestZeros = count
        selectLayer = x

ones = 0
twos = 0
 
for i in selectLayer:
    if(i==1):
        ones += 1
    elif(i==2):
        twos += 1
 
print("Part A: Ones * Twos =", ones * twos)