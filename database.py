import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='user@123',database='ineourn')
cur = con.cursor()
def login(userid, password):

    statement = f"SELECT emailid,pass1 from ineourn_student WHERE emailid='{userid}' AND pass1 = '{password}';"
    cur.execute(statement)
    #print(cur.fetchone())
    if not cur.fetchone():  # An empty result evaluates to False.
        return 0
    else:
        return 1
def course():
    cur.execute("SELECT * FROM ineourn_course")
    myresult = cur.fetchall()
    for x in myresult:
        print(x[1], x[2], x[3])
#print(login('sudhanshu@ineuron.ai','user@1234'))
#course()
def Neourn(n):
    statement = f"SELECT * from one_neourn WHERE id='{n}';"
    cur.execute(statement)
    myresult = cur.fetchall()
    for x in myresult:
        print(x[1],' ',x[2],' ', x[3])
def ineourn_jobs():
    lst=[]
    statement = f"SELECT * from ineourn_jobs;"
    cur.execute(statement)
    myresult = cur.fetchall()
    for x in myresult:
        lst.extend([x[1]+' ',x[3]+' '+x[4]])
    return lst
def ineourn_affiliates():
    lst = []
    statement = f"SELECT * from ineourn_affiliates;"
    cur.execute(statement)
    myresult = cur.fetchall()
    for x in myresult:
        lst.extend([x[1] +' - '+ x[2]])
    return lst
def iNeourn_Internship(tech,domain,project):
    statement = f"insert into ineourn_Internship(tech,domain,project) values('{tech}','{domain}','{project}');"
    cur.execute(statement)
    con.commit()
    statement1 = f"SELECT * from ineourn_Internship;"
    cur.execute(statement1)
    if not cur.fetchone():  # An empty result evaluates to False.
        return 0
    else:
        return 1

def iNeourn_user(name,emailid,pass1,phone):
    statement = f"insert into ineourn_student(name,emailid,pass1,phone) values('{name}','{emailid}','{pass1}','{phone}');"
    cur.execute(statement)
    con.commit()
    statement1 = f"SELECT * from ineourn_student;"
    cur.execute(statement1)
    if not cur.fetchone():  # An empty result evaluates to False.
        return False
    else:
        return True
#print(login('sudhanshu@ineuron.ai','User@123'))