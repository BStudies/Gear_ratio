#goal: last gear rotates 2x as fast as first
#given: list of pos ints: pegs


#notes: subtract distance between pegs
#find numbers such that last radius is first/2

#example 
'''
[4, 30, 50]
30-4 = radius 26
50-30 = radius 20
26 -> 12+14
20 -> 14+6

30-4 = radius a
50-30 = radius b

a -> c+d
b -> d+e
let e = c/2
==========
a = c+d
b = d +(c/2)
==========
Matrix
[c, d |a]
[c/2,d|b]

==========
Matrix
A = 
[1,1]
[1/2,1]

x=[c,d]
B=[a,b]

Solve rref of Ax=B, B=[peg[1]-peg[0], peg[2]-peg[1]]




return [c,c/2] if possible
else return [-1,-1]


[4,30,50,80,90]
a=26
b=20
c=30
d=10

a=f+g
b=g+h
c=h+i
d=i+j, j=f/2


[f,g|a]
[g,h|b]
[h,i|c]
[i,j|d] , j=f/2

[f,g,h,i,f/2]
[1,1,0,0,0  |a]
[0,1,1,0,0  |b]
[0,0,1,1,0  |c]
[0,0,0,1,1/2|d]





if bigger
a -> c+d
b -> d+e
f -> e+g

let g = c/2
a -> c+d
b -> d+e
f -> e+c/2


'''







			
			
			
			
			
#=============================================================








import sys

#returns list of 2 pos integers reprisenting numerator and denominator of first gears radius
#radius should be >= 1
#if impossible return [-1,-1]
def answer(pegs):

	lengths = []
	for j in range(1,len(pegs)):
		lengths.append(pegs[j]-pegs[j-1])
		
		
		
	#counters for matrix
	zeros = [0,1]
	ones = [zeros[1],3]
	zeros2 = [ones[1],len(lengths)+1]
	matrix = []
	
	
	
	
	
	#implement this setup
	'''			
	[f,g,h,i]
	[1,1,0,0 |a]
	[0,1,1,0 |b]
	[0,0,1,1 |c]
	[1/2,0,0,1 |d]
	'''
	
	
	
	
	
	
	newvec = []
	#first vector
	for j in range(0,2):
		newvec.append(1)
	for j in range(zeros2[0],zeros2[1]):
		newvec.append(0)
	matrix.append(newvec)	
		
		
		
		
		
		
		
	#middle matrix
	for j in range(1,len(lengths)-1):
		newvec = []
		#add zeros before
		for k in range(zeros[0],zeros[1]):
			newvec.append(0)
			
		#add ones
		for h in range(ones[0],ones[1]):
			newvec.append(1)
		#add zeros
		for i in range(zeros2[0],zeros2[1]-1):
			newvec.append(0)
		
		zeros[1] += 1
		ones[0]+=1
		ones[1]+=1
		zeros2[0]+=1
	
		
		matrix.append(newvec)
		
	
	
	
	
	
	
	
	#pre last vector
	newvec=[]
	
	myratio = .5				#change ratio
	newvec.append(myratio)
	for j in range(3,zeros2[1]):
		newvec.append(0)
	newvec.append(1)
	matrix.append(newvec)
	
	
		
		
		
		
		
	#last zero vector to make nxn matrix
	for j in range(0,len(lengths)):
		matrix[j].append(lengths[j])
	newvec=[]
	for j in range(0,zeros2[1]):
		newvec.append(0)
	matrix.append(newvec)
		
		

		
		
		
		
		
		
		


	print('===========')
	#myMatrix = Matrix(matrix)
	#myMatrix.display()
	#myMatrix.rref()
	
	
	
	
	
	
	
	
	
	#display matrix
	for vec in matrix:
		sys.stdout.write(str(vec[0]))
		for j in range(1,len(vec)):
			sys.stdout.write(',   ' + str(vec[j]))
		print()
	print('\n==============')
	
	
	
	
	
	#reff of matrix
	for j in range(0,len(matrix)):
		#find pivot
		if(matrix[j][j]!=0):
			#divide row by pivot to make pivot 1
			pivot = matrix[j][j]
			print('pivot: ' + str(pivot))
			for k in range(j,len(matrix[j])):
				matrix[j][k] = matrix[j][k]/pivot
				
				
				

			
			#make zeros under pivot jj 
			#k = row index under pivot, 
			'''
			pivot a
			[a,b,c]
			[d,e,f]
			[g,h,i]
			d=ad-d=0
			e=bd-e
			f=cd-f
			g=ag-g=0
			h=bg-h
			i=cg-i
			
			'''
			#make zeros below pivot
			print('zero below')
			for k in range(j+1,len(matrix)-1):
				x = matrix[k][j]
				print('subtracting' + str(x) + "*Row " + str(j) + ' from row ' + str(k) )
				for m in range(j,len(matrix[k])):
					matrix[k][m] = matrix[k][m] - matrix[j][m]*x
					
			
					
				
				
			#make zeros above pivot
			#multiply pivot by row above, the subtract
			print('zero above')
			for k in range(j-1,-1,-1):
				x = matrix[k][j]
				print('subtracting' + str(x) + "*Row " + str(j) + ' from row ' + str(k) )
				for m in range(0,len(matrix[k])):
					matrix[k][m] =  matrix[k][m] - matrix[j][m]*x 
				
			
				
				
			
		
		#row swap jto make pivot
		elif j != len(matrix):
			for k in range(j,len(matrix)):
				if matrix[k][k] != 0:
					tempvec = matrix[j] 		#copy old data
					matrix[j] = 	matrix[k]#assign new data
					matrix[k]=matrix[j]	#replace old data
					

					
		for vec in matrix:
			sys.stdout.write(str(vec[0]))
			for j in range(1,len(vec)):
				sys.stdout.write(',   ' + str(vec[j]))
			print()
		print('\n==============')
		#print('=================')
	
	
	
	
	
	illegal = False
	myanswer = []
	
	
	for j in range(0,len(matrix)):
		if matrix[j][len(matrix[j])-1] < 0:
			myanswer = [-1,-1]
			illegal = True
	
	if illegal == False:
		myanswer = [matrix[0][len(matrix[j])-1],1]

	for j in myanswer:
		print(j)
		
	return myanswer


			

answer([4,30,50, 70, 89, 100, 110])	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	