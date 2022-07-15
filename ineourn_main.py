import logging
import re
import password
import database
from itertools import count
logging.basicConfig(filename='loginfo.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s  %(message)s')


class Signup:
    studentId = 0
    Name = ""
    Email = ""
    Pass1 = ""
    Pass2 = ""
    Contact = ""

    def Student_Signup(self):
        '''this method is used to creation for a new user'''
        logging.info("Student Registration Form:")
        try:
            print('Student Registration Form:')
            print('---------------------------')
            self.Name = input("Enter your name : ")
            assert len(self.Name) != 0, "Name is empty."
            logging.error("empty string")
            self.Email = input("Enter the Email : ")
            pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
            assert re.match(pat, self.Email), "Invalid Email."
            logging.error("Invalid Email.")
            self.Pass1 = input("Enter The Password:")
            if password.pass_check(self.Pass1) != 1:
                raise Exception("Sorry, Password Creation Failed!!!")
            logging.error("Invalid password")
            self.Pass2 = input("Enter The Password again:")
            if password.pass_check(self.Pass2) != 1:
                raise Exception("Sorry, Password Creation Failed!!!")
            logging.error("Invalid password")
            self.Contact = input("Enter The Contact:")
            assert self.Pass1==self.Pass2, "Passwords are not matched"
            Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
            assert Pattern.match(self.Contact), "Invalid no."
            logging.error("Invalid no.")
            #database.iNeourn_user(self.Name,self.Email,self.Pass1,self.Contact)
            if database.iNeourn_user(self.Name,self.Email,self.Pass1,self.Contact) != True:
                raise Exception("Sorry,Signup Failed!!!")
            else:
                print("Signup Done....")
        except Exception as e:
            logging.exception(e)
            print(e, "Please Re-enter...")


class Login:
    userid = ""
    password = ""
    '''this method is used for login'''
    def Student_Login(self):
        try:
            print('Please Enter your Login details:')
            print('---------------------------')
            self.userid = input("Enter your Email :")
            self.password = input("Enter your password :")
            #print(database.login(self.userid, self.password))
            if database.login(self.userid, self.password) != 1:
                raise Exception("Sorry, Login Failed!!!")
            else:
                print("Success@@@")


        except Exception as e:
            logging.exception(e)
            print(e, "Please Re-enter...")
class Course:
    '''this method is used to return the different types courses of  ineourn from database'''
    def Student_Course(self):
        try:
            print('Ineourn Course Library------------------------------------------------------------------')
            database.course()
            assert database.course(), "No data found...2!!!!"
        except Exception as e:
            logging.exception(e)
            print(e, "No data found...")

class OneNeourn:

    def __init__(self,n):
        self.n=n

    def __neourn(self):
        '''this method is used to return the different types of one neourn from database'''
        try:
            print('One Neourn Details------------------------------------------------------------------')
            database.Neourn(self.n)
            logging.error("No data found...2!!!!")
        except Exception as e:
            logging.exception(e)
            print(e, "No data found...")

class Blog:


    def blog(self):
        '''this method is used to return the different types of blogs '''


        try:
                blogs = ['BigData', 'Blockchain', 'DataSciene']
                return blogs

        except Exception as e:
            logging.exception(e)
            print(e, "Error while fetching the blogs...")


class Neourn_jobs:

    def jobs(self):
        '''this method is used to return the different types of jobs from database'''
        try:

            print('Ineourn Jobs------------------------------------------------------------------')
            lst=database.ineourn_jobs()
            if lst==None:
                raise Exception('No data found...2!!!!')
            else:
                for i in lst:
                    print(i)
            logging.error("No data found...2!!!!")
        except Exception as e:
            logging.exception(e)
            print(e, "No data found...")
class Neourn_affiliates:

    def affiliates(self):
        '''this method is used to return the different types of jobs from database'''
        try:
            print('Ineourn Affiliates------------------------------------------------------------------')
            lst=database.ineourn_affiliates()
            if lst==None:
                raise Exception('No data found...2!!!!')
            else:
                for i,j in zip(count(),lst):
                    print(i,j)
            logging.error("No data found...2!!!!")
        except Exception as e:
            logging.exception(e)
            print(e, "No data found...")
class Neourn_Internship:

    tech=""
    project=""
    domain=""
    def Internship(self):
        '''this method is used to return the different types of Internship from database'''
        try:
            print('Ineourn Internship Form------------------------------------------------------------------')
            self.tech = input("Select your Technology : ")
            self.project = input("Select your Project : ")
            self.domain=input("Select your Domain : ")
            #print(database.iNeourn_Internship(self.tech, self.project,self.domain))
            if database.iNeourn_Internship(self.tech, self.project,self.domain) != 1:
                raise Exception("Sorry, Failed!!!")
            else:
                print("Project Created....")
        except Exception as e:
            logging.exception(e)
            print(e, "No data found...")

class Main:
    ch = 1
    while ch != 8:
        print('\tMAIN MENU')
        print('---------------------------')
        print('\t1. NEW USER CREATION')
        print('\t2. Login')
        print('\t3. Exit')
        print('---------------------------')
        print("\tSelect Your Option: ")
        ch = input()
        if ch == '1':
            w = Signup()
            w.Student_Signup()
        elif ch == '2':
            w = Login()
            w.Student_Login()
            print("Login Success....")
            while ch!=7:
                print('-------------------------------------')
                print('\tWelcome to ineuron')
                print('\t1. Course Library')
                print('\t2. Ineuron Blogs')
                print('\t3. Ineuron One Neourn')
                print('\t4. Ineuron Jobs')
                print('\t5 .Neourn Aaffiliates')
                print('\t6 .Neourn Internship')
                print('\t7. Exit...')
                print('-------------------------------------')
                ch1 = input()
                if ch1=='1':
                    w=Course()
                    w.Student_Course()
                elif ch1=='2':
                    w=Blog()
                    print(w.blog())
                elif ch1=='3':
                    print('-------------------------------------')
                    print('\tWelcome to One Neuron')
                    print('\t1. Tech Neuron')
                    print('\t2. Kids Neuron')
                    print('-------------------------------------')
                    n=int(input("Enter your choice:"))
                    w=OneNeourn(n)
                    w._OneNeourn__neourn()
                elif ch1=='4':
                    w=Neourn_jobs()
                    w.jobs()
                elif ch1=='5':
                    w=Neourn_affiliates()
                    w.affiliates()
                elif ch1=='6':
                    w=Neourn_Internship()
                    w.Internship()
                elif ch1=='7':
                    break
        elif ch == '3':
            break
        else:
            print("Invalid choice:")
            ch = input("Please RE-Enter your choice again: ")
        print("Re-enter your data:")
