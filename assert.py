def percent(marks,maxMarks):
    '''
    objective:to find percentage of student
    Input Parametres : marks,maxMarks-float
    Return value : percentage-float
    '''
    percentage=(marks/maxMarks)*100
    return percentage
def main():
    '''
    objective:to find percentage of student based on user input
    Input Parametres: none
    Return value: none
    '''
    maxMarks=float(input('enter the maxium marks'))
    assert maxMarks>0 and maxMarks<=600
    marks=float(input('enter the marks obtained'))
    assert marks>=0 and marks<=600
    percentage=percent(marks,maxMarks)
    print('percentage is',percentage)

if __name__=="__main__":
    main()    
