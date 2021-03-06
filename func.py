"""
DO NOT MODIFY THE CODE
BELOW THIS LINE.
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
#If there are two tables, drop one here.
cursor.execute("DROP TABLE IF EXISTS USERNAME")
cursor.execute(sql)
# Execute code if finished.
print("Finished loading all tables......")

print("Now commiting.........")
#Function decs.
def putin(username, website):
    b = cursor.execute("INSERT INTO USERNAME(USERNAME, WEBSITE) VALUES(?, ?)", (username, website))
    conn.commit()
    print("Record inserted.......")
def displayout(website):
    cursor.execute("SELECT USERNAME FROM USERNAME WHERE WEBSITE=?", (website,))
    a = str(cursor.fetchone())
    a=a.replace("(","")
    a=a.replace(")","")
    a=a.replace(",","")
    print("The username for the website {} is: {}".format(website,a))
