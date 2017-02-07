# CSCI 2061, Assignment 10, Problem 01
# Robert Niemann


class Person(object):
    def __init__(self, name, age, address, typePerson):
        self.name = name
        self.age = age
        self.address = address
        self.typePerson = typePerson

    def restaurant(self):

    def order(self):
        
    def pay_bill(self, bill):
        
class Millionaire(Person):
    def __init__(self, name, age, address, typePerson, vacationHomes):
        self.name = name
        self.age = age
        self.address = address
        self.typePerson = typePerson
        self.vactionHomes = vacationHomes

        def restaurant(self):
            print('Restaurant: Driver, take me to Mannys Steakhouse')

        def order(self):
            print('Order: Caviar, filet mignon, lobster, and several bottles of your best wine!')

        def pay_bill(self, bill):
            total = (bill + (bill * 0.5))
            print('Bill: Here you go ${}! And keep the change!'.format(total))

class Teacher(Person):
    def __init__(self, name, age, address, typePerson, mortgage):
        self.name = name
        self.age = age
        self.address = address
        self.typePerson = typePerson
        self.mortgage = mortgage

        def restaurant(self):
            print('Restaurant: Honey, how about Chilis tonight?')

        def order(self):
            print('Order: Can I have the special? And how much for a tall beer?')

        def pay_bill(self, bill):
            total = (bill + (bill * 0.15))
            print('Bill: Are you sure {} is correct? OK, here is {}'.format(bill, total))

class Student(Person):
    def __init__(self, name, age, address, typePerson, rent):
        self.name = name
        self.age = age
        self.address = address
        self.typePerson = typePerson
        self.rent = rent

        def restaurant(self):
            print('Restaurant: McDonalds or Culvers?')

        def order(self):
            print('Order: Burger and fries please!')

        def pay_bill(self, bill):
            print('Bill: Can I owe you ten bucks or do the dishes?')

def main():
    persons = []
    again = 'Y'

    ## Input data for different people and add appropriate object to list
    while(again == 'Y' or again == 'y'):
        name = input('Please enter the name: ')
        age = input('Please enter the age: ')
        address = input('Please enter the address: ')
        typePerson = input('Please enter the type of person: ')
        
        if(typePerson == 'Millionaire' or typePerson =='millionaire'):
            vacationHome = input('How many vacation homes does he/she have?' )
            temp = Millionaire(name , age , address , typePerson , vacationHome)
            persons.append(temp)
            again = input('Go again?')

        elif(typePerson == 'Teacher' or typePerson == 'teacher'):
            mortgage = int(input('How much mortgage is remaining?'))
            temp = Teacher(name, age, address, typePerson, mortgage)
            persons.append(temp)
            again = input('Go again?')

        elif(typePerson == 'Student' or typePerson == 'student'):
            rent = int(input('How much is rent this month?'))
            temp = Student(name, age, address, typePerson, rent)
            persons.append(temp)
            again = input('Go again?')

        else:
            print('That is not a valid entry. Please start over!')
            again = 'Y'

        print()

    ## Display information for people in list
    for person in persons:
        print(person.typePerson, "", person.name)
        person.restaurant()
        person.order()
        bill = float(input(' What is the bill?'))
        person.pay_bill(bill)
        print()
      

if __name__ == '__main__': main()
