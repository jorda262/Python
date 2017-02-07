#This program asks the user to enter a number between 1-5.
#Each number corresponds to some type of arithmetic or to quit.
#Depending on the number the program will either quit or ask for
#more numbers and then perform the chosen operation between the
#two numbers. It will then print the results and loop until you quit.
def main():
    #Method for menu display
    def menu():
        print('**************** Calculator Program ****************\n')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Quit\n')

    #Call menu method
    menu()
    #Prompt the user for their choice
    choice = int(input('Enter your choice: '))

    #while loop for continuing process until user enters 5
    while choice != 5:
        #inner loop for getting numbers 1-4 for operations
        if choice > 0 and choice < 5:
            #user input for first and second number choices
            first = float(input('Enter a number: '))
            second = float(input('Enter another number: '))
            #series of if else statements for numbers 1-4
            if choice == 1:
                total = first + second
                print('The sum of {} and {} is {}.'.format(first,second,total))
            elif choice == 2:
                difference = first - second
                print('{} - {} is {}.'.format(first,second,difference))
            elif choice == 3:
                product = first * second
                print('The product of {} and {} is {}.'.format(first,second,product))
            elif choice == 4:
                quotient = first / second
                print('{} / {} is {}.'.format(first,second,quotient))

        #else statement to catch numbers not in the 1-4 spectrum
        else:
            print('Please choose between 1 and 5!\n')

        #Call menu method to reprint menu
        menu()
        #prompt user for their new choice for next loop iteration
        choice = int(input('Enter your choice: '))

    #if statement to catch "QUIT" option
    if choice == 5:
        print('\nAdios Senora/Senor! Hasta la vista!')
        
if __name__ == "__main__": main()
