import mysql.connector
import json

def lambda_handler(event,context):
    # TODO implement
    print(event)
    
mydb = mysql.connector.connect(
    host="104.248.51.139",
    user="python",
    password="python12345",
    database="customers"
)

mycursor = mydb.cursor()

sqlFormula = "INSERT INTO users (ID, name, city) VALUES (%s, %s, %s)"

with open(event, encoding="utf8") as json_file:
    data = json.load(json_file)


    print(data)
    for i, item in enumerate(data):
        ID = item.get("ID")
        print(ID)
        name = item.get("name")
        print(name)
        city = item.get("city")
        print(city)

        mycursor.execute(sqlFormula, (ID,	name, city))
        mydb.commit()

# mycursor.execute(sqlFormula, data)