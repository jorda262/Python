#This program determines the time it takes for sound to travek
#a specified distance through a specified material. It either
#returns the time, or catches incorrect user input
def main():
         #User menu
         print('Select a medium:\n')
         print('1. Air')
         print('2. Water')
         print('3. Steel\n')

         #Prompt user for choice
         choice = int(input('Enter your choice: '))

         #Validate choice is in menu range
         if choice > 0 and choice < 4:
              #Prompt user for distance
              distance = float(input('Enter the distance in feet: '))
              #Validate distance is in acceptable range
              if distance > 0:
                  #Conditionals to determine which menu item was entered
                  if choice == 1:
                      time = (distance / 1100.0)
                      print('\nA sound wave takes {} seconds to travel {} feet through air\n'.format(time,distance))
                  elif choice == 2:
                      time = (distance / 4900.0)
                      print('\nA sound wave takes {} seconds to travel {} feet through water\n'.format(time,distance))
                  elif choice == 3:
                      time = (distance / 16400.0)
                      print('\nA sound wave takes {} seconds to travel {} feet through steel\n'.format(time,distance))
              #Catch distance less than or equal to zero
              else:
                  print('\nDistance must be greater than 0')
         #Catch incorrect menu input                
         else:
             print('\nPlease choose between 1 and 3')

if __name__ == "__main__": main()
