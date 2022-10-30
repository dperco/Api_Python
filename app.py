# let's import the flask



from email import message
import json
import mimetypes
from pstats import SortKey


from flask import Flask, jsonify, render_template, request,Response
import os
from bson import ObjectId, json_util
from requests import Response # importing operating system module
import numpy 
app = Flask(__name__)
# to stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


############################################# Create  BD , Collection  , in Mongodb ####################################

import pymongo
import os # importing operating system module
MONGODB_URI = 'mongodb://localhost'  # direccion base de datos
client=pymongo.MongoClient(MONGODB_URI)  #conexion con base de datos

db=client['thirty_days_python']  #creacion base de datos
collection=db['students']   #creacion de  coleccion en bd



##################################################### Routes  , GET  ,POST ,DELETE ,PUT  #############################

@app.route('/home') # this decorator create the home route
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = 'Welcome  FIRST API PYTHON'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')   #create  route about
def about():
    name = ' Python Programming'
    return render_template('about.html', name = name, title = 'About Us')



@app.route('/students',methods=['GET'])   # list  all  students  in  collection  DB Mongodb 
def get_students():
    students=db.students.find()
    respons=json_util.dumps(students,indent=4)
    return respons

@app.route('/students/<id>')  # search student for  id in mongo_id
def result_id(id):
     students = db.students.find_one({'_id':ObjectId(id)})
     respo= json_util.dumps(students)
     return respo

@app.route('/students/<id>',methods=['DELETE']) # delete students 
def del_id(id):
     db.students.delete_one({'_id':ObjectId(id)})
     respond=jsonify({'message':'Student = ' + id + 'was Delete succesfully'})
     return respond


@app.route('/post', methods= ['POST'])  # create in BD students 
def create_student():
    name =request.json['name']
    country=request.json['country']
    city=request.json['city']
    age=request.json['age']

    if name and country and city and age:
        db.students.insert_one({'name': name, 'country': country, 'city': city, 'age': age})
        response={'name': name, 'country': country, 'city': city, 'age': age}
    else:
       return  not_found()
    return response

@app.route('/students/<id>', methods= ['PUT'])  # modify  in BD students for id
def modify_student(id):
    name =request.json['name']
    country=request.json['country']
    city=request.json['city']
    age=request.json['age']

    if name and country and city and age:
        db.students.update_one({'_id':ObjectId(id)},{'$set': {
            'name': name, 
            'country': country,
             'city': city, 
             'age': age}})
        response=jsonify({'message':'Student = ' + id + 'was Update succesfully'})
    return response

@app.errorhandler(404)   #error message
def not_found(error=None):  
    response=jsonify({
        'message':'Resource Not Found:' + request.url,
        'status':404
    })
    response.status_code=404
    return response
  
################################################ SERVER  ######################################
if __name__ == '__main__':    #server port 5000
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)