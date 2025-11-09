def areaRectangle(length,breadth):
    '''
    objective: to compute the area of a rectangle
    Input parametres: length,breadth-numeric value
    return value: area-numeric value
     '''
    area=length*breadth
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
    print('\n end of the program')

if __name__=='__main__':
        main()



    