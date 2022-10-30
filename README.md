# ApyPython01

Este  código  realiza un CRUD ,  en Python  con base de datos Mongodb , se crea una  base de datos  ,con objetos Json , y se pueden realizar todos los métodos que conocemos  en un CRUD de JavaScript , pero desde Python.

Herramientas  utilizadas :
         Python3 
         Mongodb
         MongodbAtlas
         Postman
         VsCode.
         
Algunos  conocimientos previos que se necesitan: utilizar Postman , crear base de datos Mongodb , ejecución básica archivos python :
         
1- se abre Python  desde  el VsCode .

2- instalamos o abrimos una base de datos de MongoDb ,ya sea  en forma local o en la nube ,lo que varia es el url de la base de datos .El nombre de la BD ,lo podemos crear  desde  el programa app.py  .el ejecutable del código.

3- nos aseguramos que la Bd este  activa ,si es en forma local  ,ejecutar  en una consola cmd ,  el comando  mongod ,que ejecuta  Mongodb .

4- en VsCode , abrimos el archivo app.py  ,  y lo ejecutamos ,en la salida d de terminal debería aparecer algo  como esto :
"........
    Running] python -u "e:\30diasconpython\Api\ApyPython01\ApyPython01\Api_python\app.py"
    * Serving Flask app 'app'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on all addresses (0.0.0.0)
    * Running on http://127.0.0.1:5000
    * Running on http://192.168.100.45:5000
    Press CTRL+C to quit
    * Restarting with stat
    * Debugger is active!
   * Debugger PIN: 462-790-057
.......".
  Si aparece así, esta todo ok , fíjense que aparece la dir Ip y Puerto donde se está ejecutando este servidor.
  
5- si abren MongoAtlas y se conectan a la Bd  ,creada  en app.py , si abren la colección Students ,deberían ver los registros cargados para la prueba .Estos los creo
   con  la herramienta Postman , realizando  los típicos POST , a las rutas   creadas en app.py.
   
6- cada ruta ,método , creación ,modificación ,.., están comentados  en el archivo  app.py .
