#This program utilizes a function called Month Days that
#takes 0-2 arguments. The first argument is the desired
#month to start at 0 <-> January, 1 <-> February and so on.
#The next argument is the number of months you wish to cycle
#through. The program then prints the number of days in all
#the associated months requessted.
def main():
    for i in monthDays(3,3):
        print(i)
    print()
    for i in monthDays():
        print(i)
    print()

#Month Days Method
def monthDays(start = 0, months = 12):
    if (start+months) <= 12:
        daysList = [31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(start, start+months):
            yield daysList[i]
    else:
        #Raised if start and months sum to greater than 12.
        raise IndexError('The sum of the arguments cannot exceed twelve(12).')
    
if __name__ == "__main__": main()
