from math import pi



# Converts input angle in degrees into radians

def radians(angle):
	return angle*pi/180


'''
turtleGraph function.

Will return a vector of commands that will be plotted using the
turtlePlot function.

Input - LindenmayerString (string), System (string), N (int) (langle and rangle are of default type string)
output - turtleCommands (list)
'''

def turtleGraph(LindenmayerString,System,N,rangle='',langle=''):
	turtleCommands=[]
	distance=1 

	# Defining conditions for the Koch curve 

	if System=='Koch curve':
		if rangle=='': # <- checks if the angleChange function has been called
					   # If not, then we assume the standard conditions for the system.
			rangle=-120
			langle=60
			distance/=(3**N)
	
	# Defining the conditions for the Sierpinski triangle

	elif System=='Sierpinski triangle':
		if rangle=='':
			rangle=-60
			langle=60
			distance/=(2**N)
	
	# Defining system for dragon curve
	
	else:
		rangle=-90
		langle=90
		distance/=(N)
	
	# Iterating through string and appending corresponding turtle command

	for letter in LindenmayerString:
		if letter in ['S','A','B']:
			turtleCommands.append(distance)
		elif letter=='L':
			turtleCommands.append(radians(langle)) 
		else:
			turtleCommands.append(radians(rangle))
	return turtleCommands
