import json
import mysql.connector


with open("petlebi_products.json","r", encoding="utf8") as f:
    data = json.load(f)

try:
    con = mysql.connector.connect(
        user = "root",
        password = "eren",
        host = "localhost",
        port = 3306
    )

    if con.is_connected():
        print("Connection is successful.")
except Exception as e:
    print("Connection failed!!")

fd = open("petlebi_create.sql","r")
createStatement = fd.read()
createCommands = createStatement.split(";")
fd.close()

fd = open("petlebi_insert.sql","r")
insertStatement = fd.read()
insertCommands = insertStatement.split(";")
fd.close()

cur = con.cursor()

for command in createCommands:
    try:
        if(command != ""):
            cur.execute(command)
            con.commit()
    except Exception as e:
        print("Error while executing create statements!")
        print(e)

for item in data:
    values = (item["url"],item["name"],item["barcode"],item["price"],item["stock"],item["description"],item["category"],item["id"],item["brand"])
    
    for command in insertCommands:
        try:
            cur.execute(command,values)
            con.commit()
        except Exception as e:
            print("Error while executing insert statements!")
            print(e)

cur.close()
con.close()