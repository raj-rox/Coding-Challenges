#Generate 3x3 magic matrices
def rotate90(m):
	m[][],m[][]
	return m
matrix=[[2,7,6],[9,5,1],[4,3,8]]
def displayMatrix( mat ):
     
    for i in range(0, N):
         
        for j in range(0, N):
             
            print (mat[i][j], end = ' ')
        print ("")
#M # Starting square
# rotate(M) # rotate clockwise 90 degrees
# rotate(rotate(M)) # rotate clockwise 180 degrees
# rotate(rotate(rotate(M))) # rotate clockwise 270 degrees
# refect(M,dim=rows) # reflect along row dimension
# reflect(M,dim=cols) # reflect along column dimension
# reflect(M,dim=diag) # reflection along main diagonal
# transpose(M) # reflection along off-diagonal
displayMatrix(matrix)
matrix1=rotate90(matrix)
displayMatrix(matrix1)