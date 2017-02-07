#This program defines a classed called Mortgage and creates
#two instances of that class and send arguments in either
#the constructor or through setter function. It then
#performs various calculations to compute the monthly
#payment and the entire payment for the desired arguments.
class Mortgage:
    #Constructor for Mortage class with 3 parameters
    def __init__(self, loanAmount = 0, annualRate = 0, years = 0):      
        self.setLoanAmount(loanAmount)
        self.setAnnualRate(annualRate)
        self.setYears(years)

    #Setter function for Loan amount
    def setLoanAmount(self, amount):
        self._loanAmount = amount

    #Setter function for Annual rate
    def setAnnualRate(self, annualRate):
        self._annualRate = (annualRate/100)
        self._monthlyRate = (self._annualRate/12)

    #Setter function for Years
    def setYears(self, years):
        self._years = years
        self._numPayments = (self._years*12)

    #Getter function for Monthly Payments
    def getMonthlyPayment(self):
        section = ((1 + self._monthlyRate)**self._numPayments)
        return (((self._loanAmount)*(self._monthlyRate*(section)))/(section -1))

    #Getter function for Total Payments                                 
    def getPayBack(self):
        return (self.getMonthlyPayment() * self._numPayments)

#Main method
def main():
    #Instances of Mortgage class
    mortgage1 = Mortgage(1000, 12, 10)
    mortgage2 = Mortgage()
    
    mortgage2.setLoanAmount(2000)
    mortgage2.setAnnualRate(6)
    mortgage2.setYears(20)

    #Prints outs the desired output
    print('1st Mortgage is for ${}, {}% interest rate and a period of {} years'.format(mortgage1._loanAmount, mortgage1._annualRate, mortgage1._years))
    print('Monthly payment for 1st mortgage is $ {:.2f}'.format(mortgage1.getMonthlyPayment()))
    print('Total payments for 1st mortgage is $ {:.2f}'.format(mortgage1.getPayBack()))

    print('2nd Mortgage is for ${}, {}% interest rate and a period of {} years'.format(mortgage2._loanAmount, mortgage2._annualRate, mortgage2._years))
    print('Monthly payment for 2nd mortgage is $ {:.2f}'.format(mortgage2.getMonthlyPayment()))
    print('Total payments for 2nd mortgage is $ {:.2f}'.format(mortgage2.getPayBack()))

if __name__ == "__main__": main()
