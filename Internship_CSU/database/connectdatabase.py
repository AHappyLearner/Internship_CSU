
from cx_Oracle import *;

conn = connect('scott/zmk123_@192.168.1.101/demo')
cursor = conn.cursor();

sql_string = "SELECT *  FROM dept"
cursor.execute (sql_string)

result = cursor.fetchall()

print (cursor.rowcount)

for row in result:

    print(row)
cursor.close()
conn.close()
