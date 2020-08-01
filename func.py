"""
This program is still not fully 
operational.
"""
import sqlite3

#Getting the sqlite connection
conn = sqlite3.connect('example.db')

#Creating a object out of that connection.
cursor = conn.cursor()


#Creating the table here
sql ='''CREATE TABLE USERNAME(
   USERNAME CHAR(100) NOT NULL,
   WEBSITE CHAR(1000)
)'''
#If there are two tables, drop one here. This way, the number of tables are always kept at n-1, where n = 2.
cursor.execute("DROP TABLE IF EXISTS USERNAME")
cursor.execute(sql)
# Execute code if finished.
print("Finished loading all tables.")

# Commiting
conn.commit()
print("Now commiting")
#Function decs.
def putin(username, website):
    b = cursor.execute("INSERT INTO TABLE USERNAME(USERNAME, WEBSITE) VALUES(?, ?)", (username, website))
    print("Records inserted")
def displayout(website):
    a = cursor.execute("SELECT USERNAME FROM USERNAME WHERE WEBSITE VALUES(?)", (website))
    print(a)
    
