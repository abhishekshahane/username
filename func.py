import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('example.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()


#Creating table as per requirement
sql ='''CREATE TABLE USERNAME(
   USERNAME CHAR(100) NOT NULL,
   WEBSITE CHAR(1000)
)'''
cursor.execute("DROP TABLE IF EXISTS USERNAME")
cursor.execute(sql)
print("Table created successfully........")

# Commit your changes in the database
conn.commit()
def putin(username, website):
    b = cursor.execute("INSERT INTO TABLE USERNAME(USERNAME, WEBSITE) VALUES(?, ?)", (username, website))
    print("Records inserted")
def displayout(website):
    a = cursor.execute("SELECT USERNAME FROM USERNAME WHERE WEBSITE VALUES(?)", (website))
    print(a)
    
