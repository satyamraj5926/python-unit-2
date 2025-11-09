def areaRectangle(length,breadth):
    '''
    objective: to compute the area of a rectangle
    Input parametres: length,breadth-numeric value
    return value: area-numeric value
     '''
    area=length*breadth
    return area

def areaSquare(side):
    ''' 
    objective: to compute the area of square
    Input parametres: side-numeric value
    return value: area-numeric value  
    '''
    area=areaRectangle(side,side)
    return area

def main():
    '''
    objective: to compute the area of rectangle and square
    Input parametres: none
    Return value: none
    '''
    print('enter the following values for rectangle')
    lengthRec=int(input('lenth: integer value'))
    breadthRec=int(input('breadth: integer value'))
    areaRec=areaRectangle(lengthRec,breadthRec)
    print('\n area of rectangle: ',areaRec)
    print()
    side=int(input('enter the value of side for square'))
    areasqu=areaSquare(side)
    print('\n area of square:',areasqu)
    print('\n end of the program')

if __name__=='__main__':
        main()





