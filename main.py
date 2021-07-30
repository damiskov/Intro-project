from LindenmayerIteration import LindIter
from turtleGraph import turtleGraph
from turtlePlot import turtlePlot
from angleChange import changeAngle
import sys

'''
Main script for Lindenmayer project - David Miles-Skov (s204755)
'''


# Function that returns system of choice 
	
def chooseSys():
	systems={1:'Koch curve',2:'Sierpinski triangle',3:'Dragon curve'}
	for key,value in zip(systems.keys(),systems.values()):
		print('Enter: '+str(key)+' for '+value)
	ans1=input("\nChoice: ")
	while ans1 not in ['1','2','3']:
		ans1=input("Invalid input (Enter 'exit' to quit). Please try again:  ")
		if ans1=='exit':
			sys.exit()
	return systems[int(ans1)]


# chooseN - Allows user to input desired number of iterations and records input

def chooseN():
	ans2=input("\nPlease enter the number of iterations you want to test: ")
	possibleIter=[str(i) for i in range(0,11)]
	while ans2 not in possibleIter:
		ans2=input("Input invalid. Please enter an integer between 0 and 10 (inclusive):  ")
		if ans2=='exit':
			sys.exit()
	return int(ans2)
	
# genPlot - Creates command vector for turtle using turtleGraph and calls turtlePlot.

def genPlot(LindenmayerString,N,System):
	turtleCommands=turtleGraph(LindenmayerString,System,N)
	turtlePlot(turtleCommands,System,N)



# Initial interface and setting up of L-system

print("\nLindenmayer system project (David Miles-Skov: s204755)\n")

# Creating a dictionary of possible program functionality

choices={'1':'Choose different Lindenmayer system','2':'Change number of iterations','3':'Generate plots','4':'Alter the angles of Sierpinski or Koch','5':'Quit program'}

print("\nPlease select an initial Lindenmayer system\n")

system=chooseSys()
N=chooseN()
LindenmayerString=LindIter(system,N)

# Main loop

while True:
	print("\nCurrent system: "+system+"\nCurrent number of iterations: "+str(N))
	print("\nPlease select the integer corresponding to the desired process: \n")
	for key,val in zip(choices.keys(),choices.values()):
		print("Enter: "+key+" for: "+val)
	ans=input("\nInput: ")
	# Choosing appropriate function
	if ans=='1':
		system=chooseSys()
		N=chooseN()
		LindenmayerString=LindIter(system,N)
	elif ans=='2':
		N=chooseN()
		LindenmayerString=LindIter(system,N)
	elif ans=='3':
		print("\nGenerating plots\n")
		genPlot(LindenmayerString,N,system)
	elif ans=='4':
		changeAngle()
	elif ans=='5':
		print("\nTerminating program.")
		sys.exit()
	else:
		print("\nInvalid input")


