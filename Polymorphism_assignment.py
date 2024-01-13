

class User:# Parent class
    name = 'No Name Provided'# all of these attributes will be inherited to the other classes
    email = ' '
    password = 'Pa55w0rd'
    account_number = 0
    
    def getCredentials(self):
        entry_name = input("Enter your name: ")
        entry_password = input("\nEnter your password: ")
        if (entry_name == self.name and entry_password == self.password):
            print("\nWelcome back, {}!".format(entry_name))
        else:
            print("\nThe password or name is incorrect.")

	
class Educator (User) :# Child class
    access_level = 10# these attributes are only for the child class Educator
    department = 'General'
    employeeId = 2370

# using the parent method changing the name to employeeId instead.
    def getCredentials(self):
        entry_name = input("Enter your employee ID: ")
        entry_password = input("\nEnter your password: ")
        if (entry_name == self.employeeId and entry_password == self.password):
            print("\nWelcome back, {}!".format(entry_name))
        else:
            print("\nThe password or Employee ID is incorrect.")


class Student (User) :# Child class
    mailing_address = ' ' # these attributes are only for the child class Student
    mailing_list = True
    studentAccount = 6947

# using the parent method changing the password to studentAccount instead.
    def getCredentials(self):
        entry_name = input("Enter your name: ")
        entry_password = input("\nEnter your Student Account number: ")
        if (entry_name == self.name and entry_password == self.studentAccount):
            print("\nWelcome back, {}!".format(entry_name))
        else:
            print("\nThe name or Student Accunt number is incorrect.")












	
