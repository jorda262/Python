#This program utilizes a dictionary of names and associated
#values and utilizes key-word arguments to go through all
#of the items and search for the highest score and return
#that score and the student associated with that score
def main():
    highScore(ann=100,bob=90,carol=80,dave=70)
    highScore(ann=100,bob=90,carol=80,dave=70, ed = 69)
    highScore(ann=100,bob=90)

#Function for finding the highest score and the student with that score    
def highScore(**kwargs):
    maximum = 0
    for i in kwargs:
        if kwargs[i] > maximum:
            maximum = kwargs[i]
            index = i
    print('The highest score was: {} {}\n'.format(index, maximum))
    
if __name__=="__main__": main()
