#This program asks the user to type in a sentence.
#It then keeps asking them for more until
#the user says no. It then prionts out the
#number of charcters, alphabetic characters,
#white spaces characters, and the total word count.
def main():
    file = open('sentences.txt', 'w')
    again = 'Y'
    chars = 0
    alphaChars = 0
    nums = 0
    spaces = 0
    words = 0

    #boolean while loop for writing sentences to a file
    while(again.lower() == 'y'):
        temp = input('Please enter a sentence: ')
        file.write(temp + '\n')
        again = input('Go again? ')
        
    #Closes the file that was written to
    file.close()

    #Opens the file created by the user
    file = open('sentences.txt', 'r')
    print()
    print('File contents are:')

    #For loops for processing characters
    for line in file:
        temp = line.strip()
        print(temp)
        
        for char in temp:
            chars += 1
            if char.isalpha():
                alphaChars += 1
            if char.isdigit():
                nums += 1
            if char.isspace():
                spaces += 1

        temp = line.split()

        for each in temp:
            words += 1

    #Prints out the table in a two column table
    print('Character count:\t\t\t{}'.format(chars))
    print('Alphabetic character count:\t\t{}'.format(alphaChars))
    print('Numeric character count:\t\t{}'.format(nums))
    print('Whitespace character count:\t\t{}'.format(spaces))
    print('Word count:\t\t\t\t{}'.format(words))

if __name__ == "__main__": main()
