'''
LindIter function.

Will return the Lindenmayer string corresponding to 
the system chosen and number of iterations passed

Input -> System (string), N (int)
Output -> LindenmayerString (string)

'''
def LindIter(System,N):
	LindenmayerString=''


	if System=='Koch curve':
		LindenmayerString='S'
		for i in range(N):
			new_str=''
			for letter in LindenmayerString:
				if letter=='S':			# Koch curve has 1 ruleset
					new_str+='SLSRSLS'
				else:
					new_str+=letter
			LindenmayerString=new_str
	

	if System=='Sierpinski triangle':
		LindenmayerString='A'
		for i in range(N):
			new_str=''
			for letter in LindenmayerString: # A,B -> Move forward
				if letter=='A':				 # L,R -> Turn left/right
					new_str+='BRARB'
				elif letter=='B':
					new_str+='ALBLA'
				else:
					new_str+=letter
			LindenmayerString=new_str
	

	if System=='Dragon curve':
		LindenmayerString='AX'
		for i in range(N):
			new_str=''
			for letter in LindenmayerString:
				if letter=='X':
					new_str+='XRYAR' # Dragon curve has 2 rulesets, with X and Y not representing a turtle command
				elif letter=='Y':
					new_str+='LAXLY'
				else:
					new_str+=letter
			LindenmayerString=new_str
	

	return LindenmayerString