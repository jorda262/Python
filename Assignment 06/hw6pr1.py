#This program takes any number of arguments and then sums them
#and then returns the sum printed
def main():
    add(1)
    add(1,2,3)
    add()
    add(1,2,3,4,5)

#This function sums any given number of arguments   
def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)
        
if __name__=="__main__": main()
