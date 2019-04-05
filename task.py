from matrix import Matrix

def main():
    matrix1 = Matrix(1,2,3,4)
    matrix2 = Matrix(5,6,7,8)
    print ('The first Matrix is : ' )
    matrix1.printMatrix()
    print ('')
    
    print ('The second Matrix is : ' )
    matrix2.printMatrix()
    print ('')
  
    print ('m1+=m2:')
    matrix1 += matrix2
    matrix1.printMatrix()
    print ('')
    
    print ('m3=m1+m2:')
    matrix3 = matrix1+matrix2
    matrix3.printMatrix()
    print ('')
    
    print ('m1-=m2:')
    matrix1 -= matrix2
    matrix1.printMatrix()
    print ('')
    
    print ('m4=m1-m2:')
    matrix4 = matrix1 - matrix2
    matrix4.printMatrix()
    print ('')
    
    print ('m5=m1@m2:')
    matrix5 = matrix1 @ matrix2
    matrix5.printMatrix()
    print ('')
    
    print ('m6=m1+2:')
    matrix6 = matrix1 + 2
    matrix6.printMatrix()
    print ('')
    
    print ('m7=2+m1:')
    matrix7 = 2 + matrix1
    matrix7.printMatrix()
    print ('')
    
    print ('m8=m1-2:')
    matrix8 = matrix1 - 2
    matrix8.printMatrix()
    print ('')
    
    
if __name__== '__main__':
    main()
