from LindenmayerIteration import LindIter
from turtleGraph import turtleGraph
from turtlePlot import turtlePlot


# A copy of chooseN from the main script

def chooseN():
	ans2=input("\nPlease enter the number of iterations you want to test: ")
	possibleIter=[str(i) for i in range(0,11)]
	while ans2 not in possibleIter:
		ans2=input("Input invalid. Please enter an integer between 0 and 10 (inclusive):  ")
		if ans2=='exit':
			sys.exit()
	return int(ans2)
'''
changeAngle function.

This is an extra function that will alter the right and left turning angles 
of the Koch curve and Sierpinski triangle.

Input -> None
Output -> Pyplot graph 

'''
def changeAngle():
	print("\nAltering angles.")
	print("For Koch curve enter: 1\nFor Sierpinski triangle enter: 2\n('exit' to return to main interface)")
	
	ans=input("Input: ")
	if ans=='exit':
		return 0
	# User chooses system

	while ans not in ['1','2']:
		ans=input("Invalid input. try again: (enter 'exit' to return to main interface): ")
		if ans=='exit':
			return 0
	
	# If system is Koch curve

	if ans=='1':
		print('\nDefining angles:')
		
		langle=''
		while type(langle) is str: # Making sure that we obtain a valid integer input 
			langle=input("\nEnter the value of the left turning angle: ")
			try:
				langle=int(langle)
			except ValueError:
				print("Invalid input, try again.")
			
		rangle=''
		while type(rangle) is str:
			rangle=input("\nEnter the value of the right turning angle: ")
			try:
				rangle=int(rangle)
			except ValueError:
				print("Invalid input, try again.")
			break
		rangle=-rangle # <- Right turning angle is made negative 
		
		# Obtaining vector of turtle commands

		N=chooseN()
		LindenmayerString=LindIter('Koch curve',N)
		turtleCommands=turtleGraph(LindenmayerString,'Koch curve',N,rangle=rangle,langle=langle)
		

	# If system is Sierpinski triangle
	
	if ans=='2':


		print('\nDefining angles:')
		
		langle=''
		while True:
			try:
				langle=int(input("Enter the value of the left turning angle: "))
			except ValueError:
				print("Invalid input, try again.")
			break
		rangle=''
		while True:
			try:
				rangle=int(input("Enter the value of the right turning angle: "))
			except ValueError:
				print("Invalid input, try again.")
			break
		rangle=-rangle
		N=chooseN()
		LindenmayerString=LindIter('Sierpinski triangle',N)
		turtleCommands=turtleGraph(LindenmayerString,'Sierpinski triangle',N,rangle=rangle,langle=langle)
	
	# Plotting the resulting graph

	turtlePlot(turtleCommands,'',N)
