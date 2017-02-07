#This program utilizes the mutable lists of Python and prompts
#the user for the number of employees and then uses for loops to
#ask for the employee information and then print the information.
def main():
    employeeList = [] #List to store employee names
    rateList = [] #list to store employee wage rates
    hoursList = [] #list to store employee hours
    wagesList = [] #list to store employee total wage

    #Payroll Program header
    print('****************  Payroll Program  ****************\n')
    #Data Input header
    print('****************    Data Input     ****************')
    #Prompt user for the number of employees
    numberOfEmployees = int(input('Please enter the number of employees: '))

    #for loop for getting user input for employee information
    for i in range((numberOfEmployees)):
        employeeList.append(input('\nEnter the employee name: '))
        rateList.append(float(input('Enter the employee wage rate: ')))
        hoursList.append(float(input('Enter the employee hours: ')))
        wagesList.append(((rateList[i]) * (hoursList[i])))

    #Payroll Data header
    print('****************  Payroll Data  ****************')

    #for loop for printing all of the employee information
    for i in range(0,numberOfEmployees):
        print('\nEmployee: {}'.format(employeeList[i]))
        print('   Hours: {}'.format(hoursList[i]))
        print('   Rate:  ${}/hr'.format(rateList[i]))
        print('   Wage:  ${}'.format(wagesList[i]))
    
if __name__ == "__main__": main()
