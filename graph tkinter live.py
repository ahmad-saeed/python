#! py -2

from Tkinter import *
import time
import random

width = 700
height = 135
dataMax = 1023

# The window is an object of type tk
root = Tk()
root.title('Simple Plot')

# A canvas object is something you can draw on
# we put it into the root window
canvas = Canvas(root, width=width, height=height, bg = 'white')
canvas.pack()

# draw the wiggly line

# display window and wait for it to close
#root.mainloop()
    
originalData = [0] * width
while 1:
	canvas.delete("my_tag")
	time.sleep(0.01)
	# some meaningless x-y data points to plot
 	# the input data is in the range x = 0 to 100, and y = 0 to 250.
 	
 	
 	y = random.randint(1,dataMax)
 	originalData.remove(originalData[0])
 	originalData+=[y]
 	#print originalData
 	# rescale the data to lie in the graph range x = 100 to 400, y = 250 to 50
 	# remember y is zero at the top of the window. 
 	dataList = []
 	for (i,y) in enumerate(originalData):
 	 	dataList.append(( i, y/(dataMax/height)))

 	canvas.create_line(dataList, fill='blue',tags='my_tag')
 	root.update()
