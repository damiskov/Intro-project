import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, pi

'''
TurtlePlot function:

Will create the graph for the desired system and number of iterations.

Input - turtleCommands (list), System (string), N (int)
Output - pyplot graph

'''
def turtlePlot(turtleCommands,System,N):
	
	
	l=turtleCommands[0] # Defining l as the value of length in the turtle commands
	current_loc=[0,0] # Start location = Origin
	coordinates=[current_loc]
	
	if System=='Sierpinski triangle' and N%2!=0:
		angle=pi/3 # Altering the start orientation for the turtle (if system is sierpinski and number of iterations is odd)
	else: 
		angle=0


	rMat=np.array([[cos(angle),-sin(angle)],[sin(angle),cos(angle)]]) # defining the rotation matrix
	d=np.matmul(rMat,[1,0]) # Initial direction vector according to initial orientation

	# Looping through commands

	if System in ['Sierpinski triangle','Koch curve']:

		for i,command in enumerate(turtleCommands):
			
			if i%2==0:
				current_loc=[current_loc[0]+l*d[0],current_loc[1]+l*d[1]] # Moving the turtle 
				coordinates.append(current_loc) # Appending the new coordinates of the turtle
		
			else:
				angle=command
				rMat=np.array([[cos(angle),-sin(angle)],[sin(angle),cos(angle)]])
				d=np.matmul(rMat,d) # Changing the orientation of the direction vector
	
	# This particular section is for the dragon curve system. Its vector of commands does not consist of 
	# alternating forward and turn commands, so the following code is required.

	else:

		for i,command in enumerate(turtleCommands):
			
			if i%4==0:
				current_loc=[current_loc[0]+l*d[0],current_loc[1]+l*d[1]] # Moving the turtle 
				coordinates.append(current_loc) 
		
			else:
				angle=command
				rMat=np.array([[cos(angle),-sin(angle)],[sin(angle),cos(angle)]])
				d=np.matmul(rMat,d) # Changing the orientation of the direction vector
	
	# Showing the created plot

	plt.style.use('default')
	plt.axes().set_aspect('equal')
	x=[coordinate[0] for coordinate in coordinates]
	y=[coordinate[1] for coordinate in coordinates]
	plt.plot(x,y)
	plt.show()
