import pymongo
from flask import Flask,request,jsonify
app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://amitava_2112:Suman123@python.e0zfy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['Internship']
collection = database["Internship_data"]
@app.route('/mongo_insert',methods=['GET' , 'POST'])
def Insertion():
        '''this method is used to return the different types of Internship from database'''

        try:
            print('Ineourn Internship Form------------------------------------------------------------------')
            pcode=request.json['pcode']
            tech = request.json['tech']
            project = request.json['project']
            domain=request.json['domain']
            data = {
                "pcode":pcode,
                "tech": tech,
                "project": project,
                "domain": domain
            }
            collection.insert_one(data)
            return jsonify(("Data Inserted...."))
        except Exception as e:
            logging.exception(e)
            print(e, "No data found...")
@app.route('/mongo_search',methods=['GET' , 'POST'])
def Search():
        '''this method is used to return the different types of Internship from database'''

        try:
            print('Ineourn Internship Form------------------------------------------------------------------')
            pcode = request.json['pcode']
            l=[]
            d = collection.find({'pcode':pcode})
            l=list(d)
            print(l)
            return jsonify((str(l)))
        except Exception as e:
            logging.exception(e)
            print(e, "No data found...")
@app.route('/mongo_delete',methods=['GET' , 'POST'])
def Delete():
        '''this method is used to return the different types of Internship from database'''

        try:
            print('Ineourn Internship Form------------------------------------------------------------------')
            pcode = request.json['pcode']
            collection.delete_one({'pcode': pcode})
            return jsonify(("data deleted..."))
        except Exception as e:
            logging.exception(e)
            print(e, "No data found...")

@app.route('/mongo_update',methods=['GET' , 'POST'])
def Update():
    '''this method is used to return the different types of Internship from database'''

    try:
        print('Ineourn Internship Form------------------------------------------------------------------')
        pcode = request.json['pcode']
        tech=request.json['tech']
        collection.update_one({'pcode': pcode} , {'$set':{'tech': tech} })
        return jsonify(("data updated..."))
    except Exception as e:
        logging.exception(e)
        print(e, "No data found...")
if __name__=='__main__'  :
    app.run(debug=True)
