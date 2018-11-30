import mysql.connector

import config

myDb = mysql.connector.connect(user='admin',
                                     password='admin',
                                     host='127.0.0.1',
                                     database='test_datawarehouse')

myCursor = myDb.cursor()
tblName = 'tbl_owner'
# query = 'SELECT OwnerName FROM {0}'.format(tblName)
# query = 'INSERT INTO {0} (OwnerName) VALUES ("{1}")'.format(tblName, "Barek")
query = 'SHOW TABLES'

myCursor.execute(query)

# myDb.commit()
myResults = myCursor.fetchall()

for result in myResults:
    print(result)

myDb.close()
