# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from SolPacker.packer import newPacker
from SolPacker.packer import *
import random 
import time


rectangles = [(100, 30), (40, 60), (30, 30),(70, 70), (100, 50), (30, 30),(55,77),(48,72)]
bins = [(300, 450)]#[(300, 450), (80, 40), (200, 150)]

packer = newPacker(mode=PackingMode.Online, 
         bin_algo=PackingBin.BBF, 
        pack_algo=MaxRectsBssf,
        sort_algo=SORT_AREA, 
        rotation=True)



# Add the bins where the rectangles will be placed
for b in bins:
	packer.add_bin(*b)
    
count=0
# Add the rectangles to packing queue
#for r in rectangles:
start = time.time()
for i in range(300):
    r=(random.randint(30, 70),random.randint(30, 70))
    count+=1
    #print("---------------------------------------------------------------")
    #print("Pack "+str(count)+" : Rectangle ("+str(r[0])+","+str(r[1])+")")
    #packer.add_rect(*(r[0],r[1]))
    packer.add_rect(*r)
    
   
    #print(packer._open_bins[0].__dict__)
    '''
    for abin in packer:
        print(abin.bid) # Bin id if it has one
        for rect in abin:
            print(rect)
    '''
end = time.time()
print("Pack time=", end - start)

'''
# Start packing
packer.pack()


# Obtain number of bins used for packing
nbins = len(packer)

# Index first bin
abin = packer[0]

# Bin dimmensions (bins can be reordered during packing)
width, height = abin.width, abin.height

# Number of rectangles packed into first bin
nrect = len(packer[0])

# Second bin first rectangle
rect = packer[0][0]

# rect is a Rectangle object
x = rect.x # rectangle bottom-left x coordinate
y = rect.y # rectangle bottom-left y coordinate
w = rect.width
h = rect.height
#looping over all of them

for abin in packer:
  print(abin.bid) # Bin id if it has one
  for rect in abin:
    print(rect)
#or using rect_list()

# Full rectangle list
all_rects = packer.rect_list()
for rect in all_rects:
	b, x, y, w, h, rid = rect

# b - Bin index
# x - Rectangle bottom-left corner x coordinate
# y - Rectangle bottom-left corner y coordinate
# w - Rectangle width
# h - Rectangle height
# rid - User asigned rectangle id or None
'''