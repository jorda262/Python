# CSCI 2061, Assignment 05, Problem 01
# Taylor Jordan
# Employee Payroll Program


def main():
    #Top of the menu print-off
    print("**************** Payroll Program ****************")
    print()
    print("****************   Data Input    ****************")
    #Prompt the user for the number of employees
    numEmployees = int(input("Please enter the number of employees: "))
    print()
    #Four lists for storing the information
    employeeNames = []
    employeeRates = []
    employeeHours = []
    employeeWages = []

    #For-loop to go through inputted number of employees.
    for employeeNumber in range(numEmployees):
        while True:
            #Try part of exception handeling.
            try:
                name = readName(employeeNumber)
                rate = readRate()
                hours = readHours()
            #All four exception clauses to catch associated exception
            except ValueError as v:
                print(v)
                print('Please start over')

            except EmpNameError as e:
                print(e)
                print('Please start over')

            except RateError as r:
                print(r)
                print('Please start over')

            except HoursError as h:
                print(h)
                print('Please start over')
            #Else clause to perform desired action after checking for exceptions               
            else:
                employeeNames.append(name)
                employeeRates.append(rate)
                employeeHours.append(hours)
                employeeWages.append(employeeHours[employeeNumber] * employeeRates[employeeNumber])
                print()
                break
            print()
            print()

    print()
    #Print off after entering all of the employees
    print("****************  Payroll Data  ****************")
    for employeeNumber in range(numEmployees):
        print("Employee: {}".format(employeeNames[employeeNumber]))
        print("   Hours: {}".format(employeeHours[employeeNumber]))
        print("   Rate:  ${}/hr".format(employeeRates[employeeNumber]))
        print("   Wage:  ${}".format(employeeWages[employeeNumber]))
        print()

# Thrown if employee name is zero length
class EmpNameError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# Thrown if hourly rate <0 or > 20
class RateError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# Thrown if weekly hours <0 OR > 60
class HoursError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# function readName
def readName(i):
    count = i
    print('Data entry for employee {}'.format(count))
    name = input("Enter the employee name: ")    
    if len(name) > 0:
        if type(name) == str:
            return name
        else: raise ValueError("'Data entered in incorrect format'")
    else: raise EmpNameError('Name cannot be zero length')

# function readRate
def readRate():
    rate = input("Enter the employee wage rate (0..20): ")
    
    try:
        rate = float(rate)
    except:
        raise ValueError("'Data entered in incorrect format'")
    else:
        if (rate >= 0 and rate <= 20):
            return rate
        else: raise RateError('Hourly rate must be between 0 and 20')

# function readHours
def readHours():
    hours = input("Enter the employee hours (0..60): ")
    
    try:
        hours = float(hours)
    except:
        raise ValueError("'Data entered in incorrect format'")
    else:
        if hours >= 0 and hours <= 60:
            return hours
        else: raise HoursError('Hours must be between 0 and 60')

if __name__ == "__main__": main()

