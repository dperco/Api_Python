

# let's import the flask
from socket import setdefaulttimeout
from flask import Flask, render_template
import pymongo
import os # importing operating system module
MONGODB_URI = 'mongodb://localhost'
client=pymongo.MongoClient(MONGODB_URI)
#client = pymongo.MongoClient(MONGODB_URI)
# Creating database
#db = client.Cluster0
db=client['thirty_days_python']
collection=db['students']
# Creating students collection and inserting a document
#db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
#print(client.list_database_names())
#db = client.python0
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
#print(client.list_database_names())
#app = Flask(__name__)
#if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
#    port = int(os.environ.get("PORT", 5000))
#    app.run(debug=True, host='0.0.0.0', port=port)

#db = client.python0
db.students.insert_one({'name': 'asia', 'country': 'Finland', 'city': 'portu', 'age': 45})
#print(client.list_database_names())

db.students.insert_one({'name': 'pedro', 'country': 'uganda', 'city': 'popey', 'age': 25},
                       {'name': 'paco', 'country': 'Congo', 'city': 'manila', 'age': 33})