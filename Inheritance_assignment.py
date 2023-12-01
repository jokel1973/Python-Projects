

class User:# Parent class
	name = 'No Name Provided'# all of these attributes will be inherited to the other classes
	email = ' '
	password = 'Pa55w0rd'
	account_number = 0

	
class Educator (User) :# Child class
	access_level = 10#these attributes are only for the child class Educator
	department = 'General'

	
class Student (User) :# Child class
	mailing_address = ' ' # these attributes are only for the child class Student
	mailing_list = True
