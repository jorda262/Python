#This program creates a database then adds a list in the form
#of a four column table. It then utilizes CRUD functionality to
#create, retrieve, update (not included here because of tuple use),
#and delete from the database. It prompts the user to add rows and
#lets them choose when to stop. It then reprints the database in tabular
#form and then makes the user search for a single student in the database
#and prints that individual users row. It then asks you to delete a sinlge row
#and then prints the final table.

import sqlite3

#Create portion of CRUD
def insert(db, row):
    db.execute('insert into students (name, age, class, gpa) values (?, ?, ?, ?)', (row[0], row[1], row[2], row[3]))
    db.commit()

#Retrieve portion of CRUD
def retrieve(db, name):
    cursor = db.execute('select * from students where name = ?', (name,))
    print(cursor.fetchone())

#Delete portion of CRUD
def delete(db, name):
    db.execute('delete from students where name = ?', (name,))
    db.commit()

#Row-factory print rows function
def disp_rows(db):
    cursor = db.execute('select * from students order by gpa')
    for row in cursor:
        print('(\'{}\', {}, \'{}\', {})'.format(row[0], float(row[1]), row[2], row[3]))

def main():
    studentList = [ ('Ann Annson', 19, 'Freshman', 3.0),
                    ('Bill Billson', 20, 'Sophmore', 3.4),
                    ('Carl Carlson', 21, 'Junior', 4.0),
                    ('Dawn Dawnson', 22, 'Senior', 2.7)]

    #Creates the students.db database
    db = sqlite3.connect('students.db')
    print('After creation database is: ')
    db.execute('drop table if exists students')
    db.execute('create table students (name TEXT PRIMARY KEY, age NEAR, class TEXT, gpa REAL)')   

    #Adds the full studentList
    for each in studentList:
        insert(db, each)

    #Prints the entire database in table form
    disp_rows(db)
    print()

    #Boolean flag while loop for adding desired number of students
    flag = 'y'
    while (flag.lower() == 'y'):
        name = input('Please enter student name: ')
        age = input('Please enter student age: ')
        year = input('Please enter student year: ')
        gpa = float(input('Please enter student gpa: '))
        insert(db, (name, age, year, gpa))
        flag = input('Go again? ')

    #Prints uopdated table from database
    print('\nAfter additions, database is: ')
    disp_rows(db)
    print()

    #Prompts user to search database and then displays their row
    search = input('Student to search for? ')
    retrieve(db, search)
    print()

    #Prompts user to delete a student from the database
    bye = input('Student to delete? ')
    delete(db, bye)

    #Prints uopdated table from database
    print('\nAfter deletion, database is:')
    disp_rows(db)

if __name__ == "__main__": main()
