from flask import Flask,request,jsonify
import logging
import database
from itertools import count
logging.basicConfig(filename='loginfo.log', level=logging.INFO,format='%(asctime)s %(levelname)s %(name)s  %(message)s')
app = Flask(__name__)

@app.route('/inser',methods=['GET' , 'POST'])
def Internship():
        '''this method is used to return the different types of Internship from database'''

        try:
            print('Ineourn Internship Form------------------------------------------------------------------')
            tech = request.json['tech']
            project = request.json['project']
            domain=request.json['domain']
            #print(database.iNeourn_Internship(self.tech, self.project,self.domain))
            if database.iNeourn_Internship(tech, project,domain) != 1:
                raise Exception("Sorry, Failed!!!")
            else:
                return jsonify(("Project Created...."))

        except Exception as e:
            logging.exception(e)
            print(e, "No data found...")
@app.route('/fetch',methods=['GET' , 'POST'])
def Internship_Data():
        '''this method is used to return the different types of jobs from database'''
        try:
            print('Ineourn Affiliates------------------------------------------------------------------')
            id = request.json['id']
            lst=database.Internship_Record(id)
            if lst==None:
                raise Exception('No data found...2!!!!')
            else:
                for i,j in zip(count(),lst):
                    print(i,j)
            return jsonify(lst)
            logging.error("No data found...2!!!!")
        except Exception as e:
            logging.exception(e)
            print(e, "No data found...")
@app.route('/update',methods=['GET' , 'POST'])
def Internship_Update():
        '''this method is used to return the different types of jobs from database'''
        try:
            print('Ineourn Affiliates------------------------------------------------------------------')
            id = request.json['id']
            tech=request.json['tech']
            if database.Internship_update(id,tech) != True:
                raise Exception("Sorry, Failed!!!")
            else:
                return jsonify(("Data Updated...."))
            #logging.error("No data found...2!!!!")
        except Exception as e:
            logging.exception(e)
            print(e, "No data found...")

@app.route('/delete',methods=['GET' , 'POST'])
def Internship_Delete():
        '''this method is used to return the different types of jobs from database'''
        try:
            print('Ineourn Affiliates------------------------------------------------------------------')
            id = request.json['id']
            if database.Internship_delete(id) != True:
                raise Exception("Sorry, Failed!!!")
            else:
                return jsonify(("Data Deleted...."))
            #logging.error("No data found...2!!!!")
        except Exception as e:
            logging.exception(e)
            print(e, "No data found...")
if __name__=='__main__'  :
    app.run(debug=True)
