#https://www.youtube.com/watch?v=JGZ04Bi-sOc&ab_channel=nETSETOS 
#nxn matrix rotation
def rotate90(m):
	#Transpose matrix
	for i in range(len(m)):
		for j in range(i,len(m[0])):
			m[i][j],m[j][i]=m[j][i],m[i][j]
	#Reverse
	for i in range(0,int(len(m)/2)):
		for j in range(0,len(m[0])):
			m[j][i],m[j][len(m)-i-1]=m[j][len(m)-i-1],m[j][i]
	return m
def displayMatrix(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            print (mat[i][j], end = ' ')
        print ("")

matrix=[[2,7,6,1],[9,5,1,2],[4,3,8,3],[1,2,3,4]]
displayMatrix(matrix)
print()
matrix1=rotate90(matrix)
displayMatrix(matrix1)
