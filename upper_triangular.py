#!usr/bin/env/python 3
#A PYTHON SCRIPT TO CONVERT ANY nxn MATRIX TO UPPER TRIANGULAR FORM
n=int(input('Enter the size of matrix(nxn)'))
matrix=[[0]*n for i in range(0,n)]
#print(matrix)
m=matrix
for i in range(0,n):
	for j in range(0,n):
		m[i][j]=int(input('Enter element {0}{1}  '.format(i+1,j+1)))

for i in range(0,n):
	for j in range(i+1,n):
		temp=float(m[j][i]/m[i][i])
		for k in range(i,n):
			m[j][k]=m[j][k]-temp*m[i][k]
for i in range(0,n):
	for j in range(0,n):
		print(m[i][j],end="\t\t\t")
	print()
	

