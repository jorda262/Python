def main():
    addThree(4,5,6)
    addThree()
    addThree(4)

def addThree(a=1,b=2,c=3):
    total = a + b + c
    print('The sum of the three values is', total)
    
if __name__ == "__main__": main()
