#This program takes 0-4 arguments and then sums
#the numbers passed and the returns that value
#and the sum is then printed in main
def main():
    print(add(1,2,3,4))
    print(add(1,2,3))
    print(add(1,2))
    print(add(1))
    print(add())

#Add method that takes 0-4 arguments and uses a series
#of If-Elif-Else statements to correctly sum up the
#arguments not including the None value.
def add(first = None, second = None, third = 1, fourth = 1):
    sum = 0
    if first is None and second is None:
        sum = third + fourth
        return sum
    elif first is None:
        sum = second + third + fourth
        return sum
    elif second is None:
        sum = first + third + fourth
        return sum
    else:
        sum = first + second + third + fourth
        return sum

if __name__=="__main__": main()
