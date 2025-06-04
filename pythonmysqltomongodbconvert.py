pip install mysql-connector-python
pip install pymongo

  import mysql.connector
     mydb = mysql.connector.connect(
         host="your_host",
         user="your_user",
         password="your_password",
         database="your_database"
     )
     mycursor = mydb.cursor()
     
     from pymongo import MongoClient
     client = MongoClient("mongodb://your_user:your_password@your_host:27017/")
     db = client["your_database"]
     collection = db["your_collection"]
     
mycursor.execute("SELECT * FROM your_table")
result = mycursor.fetchall()
     