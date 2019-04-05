# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:49:45 2019

@author: mafal
"""
import math

class Matrix:
    def __init__(self, *arg):
        self.numberRows = int(math.sqrt(len(arg)))
        self.argsList = arg
        self.matrix = Matrix.createMatrix(self,self.argsList)
        self.pos = 0

        try:
            if (math.sqrt(len(arg)) - int(math.sqrt(len(arg)))):
                raise Exception ('The matrix is not a square')
        except:
            print('Unexpected error!')#, sys.exc_info()[0])
    
    def __getitem__(self,index):
        return self.matrix[index]

    def __setitem__(self,index,value):
        self.matrix[index] = value
    
    def createMatrix(self,argsList):
        matrix = []            
        for i in range(self.numberRows):
            rowList = []
            for j in range(self.numberRows):
                rowList.append(argsList[self.numberRows * i + j])
                
            matrix.append(rowList)
        
        self.matrix = matrix
        return matrix
    
    def printMatrix(self):
        for i in range(self.numberRows):
            stringAux = ''
            for j in range(self.numberRows):
                stringAux += str(self.matrix[i][j])
                stringAux +=' '
            print(stringAux)
        
        
    
    def __add__(self,matrix2):
        if(type(matrix2) == int):
            listAux = list(matrix2 for i in range(self.numberRows*self.numberRows))
            matrix2 = Matrix(*listAux)
        result = list(0 for i in range(self.numberRows*self.numberRows))
        matrix = Matrix(*result)
        for i in range(self.numberRows):
            for j in range(self.numberRows):
                matrix[i][j] = self.matrix[i][j] + matrix2[i][j]
        
        return matrix
    
    def __radd__(self, other):
        return self.__add__(other)
  
    def __iadd__(self,matrix2):
        result = list(0 for i in range(self.numberRows*self.numberRows))
        matrix = Matrix(*result)
        for i in range(self.numberRows):
            for j in range(self.numberRows):
                matrix[i][j] = self.matrix[i][j] + matrix2[i][j]
            
        self.matrix = matrix
        return self.matrix
    
    def __sub__(self,matrix2):
        if(type(matrix2) == int):
            listAux = list(matrix2 for i in range(self.numberRows*self.numberRows))
            matrix2 = Matrix(*listAux)
        result = list(0 for i in range(self.numberRows*self.numberRows))
        matrix = Matrix(*result)
        for i in range(self.numberRows):
            for j in range(self.numberRows):
                matrix[i][j] = self.matrix[i][j] - matrix2[i][j]
            
        
        return matrix
    def __rsub__(self, other):
        return self.__sub__(other)
    
    def __isub__(self,matrix2):
        result = list(0 for i in range(self.numberRows*self.numberRows))
        matrix = Matrix(*result)
        for i in range(self.numberRows):
            for j in range(self.numberRows):
                matrix[i][j] = self.matrix[i][j] - matrix2[i][j]
            
        self.matrix = matrix
        return self.matrix
    
    def __matmul__(self,matrix2):
        result = list(0 for i in range(self.numberRows*self.numberRows))
        matrix = Matrix(*result)
        for i in range(self.numberRows):
           for j in range(self.numberRows):
                for k in range(self.numberRows):
                    matrix[i][j] += self.matrix[i][k] * matrix2[k][j]
        return matrix
    
    
    def __iter__(self):
        return self
