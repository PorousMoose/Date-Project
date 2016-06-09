def inputInt(prompt):
    i=None
    print('All inputs must be interger')
    i=input(prompt)
    try:
        i=int(i)
    except:
        print('Please input something valid')
            
    return i

def inputBoundInt(prompt,upperBound,lowerBound):
    i=upperBound+1
    while(i>upperBound or i<lowerBound):
        i=inputInt(prompt)
    return i

def isLeapYear(year):
    if(year%400==0):
        return True
    elif(year%100==0):
        return False
    elif(year%4==0):
        return True
    else:
        return False

def makeJump(jump,day,month,year):
    while(jump>1):
        if(isLeapYear(year) and month==1 and day==monthLength[month]):
            day+=1
        elif(month==11 and day>=monthLength[month]):
            day=1
            month=1
            year+=1
        elif(day>=monthLength[month]):
            day=1
            month+=1
        else:
            day+=1
        
        jump-=1
    print('%s/%s/%s'%(day,month,year))

if __name__ == "__main__":
    monthLength=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    
    month=inputBoundInt('Please Input Month: ',12,1)
    day=inputBoundInt('Please Input Day: ',monthLength[month],1)
    year=inputInt('Please Input Year: ')
    
    while(True):
        jump = inputInt('Please Input jump: ')
        if(jump<0):
            jump*=-1
        makeJump(jump,day,month,year)