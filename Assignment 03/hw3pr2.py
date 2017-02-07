#This program asks for the number of tests and number of
#students. Then it prompts the user for each test score
#for each student and test. It then gives you the average
#for each individual test and the entire sum of the tests.
def main():
    #Prompt user for number of students and number of tests
    numberOfStudents = int(input('Enter the number of students: '))
    numberOfTests = int(input('Enter the number of tests: '))
    testCount = 0 #variable for number of tests
    total = 0 #variable for storing total 
    average = 0 # variable for storing average
    #outer while loop for keeping track of number of tests
    while testCount < numberOfTests:
        print('\n*************Test {} Scores*************'.format(testCount+1))
        studentCount = 0 #variable for maintaining student count
        count = 0 #counter variable
        sum = 0 #variable for storing the total sum
        testCount = testCount + 1 #update testCount
        total = total + average #counter for total
        #inner while loop for keeping track of each students test scores
        while studentCount < numberOfStudents:
            #Prompt user for individual test scores
            score = int(input('Enter the score for test {} for student {}: '.format(testCount-1,count)))
            count = count + 1 #update count
            currentTest = count - 1 
            studentCount = studentCount + 1 #update student count
            sum = sum + score
            #check for end of while loop and print average
            if count == numberOfStudents:
                average = sum/numberOfStudents
                print('Average for test {} was {}\n'.format((testCount-1), average))
        finalTotal = total + average
    #after all while loop iterations print the entire student average on all tests
    if testCount == numberOfTests:
        totalAverage = finalTotal/numberOfTests
        print('Average for all three tests was {}'.format(totalAverage))               
                                 
if __name__ == "__main__": main()                                 
            
