import mysql.connector
class DBConnect:
    con=''
    def getConn():
        DBConnect.con = mysql.connector.connect(user='root',
                                          password='',
                                          host='localhost',
                                          database='banking')
        return DBConnect.con
    
