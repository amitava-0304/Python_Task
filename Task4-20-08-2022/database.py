import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='user@123',database='ineourn')
cur = con.cursor()
def Internship_Record(id):
    statement = f"SELECT * from ineourn_Internship WHERE id='{id}';"
    cur.execute(statement)
    myresult = cur.fetchall()
    lst = []
    for x in myresult:
        lst.extend([x[1] + ' ' + x[2] + ' ' + x[3]])
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

def Internship_update(id,tech):
    statement = f"update ineourn_Internship set tech='{tech}' WHERE id='{id}';"
    cur.execute(statement)
    con.commit()
    print(cur.rowcount)
    if cur.rowcount>=1:
        return True
    else:
        return False

def Internship_delete(id):
    statement = f"delete from ineourn_Internship WHERE id='{id}';"
    cur.execute(statement)
    con.commit()
    print(cur.rowcount)
    if cur.rowcount>=1:
        return True
    else:
        return False
#print(Internship_update(2,'tech1'))