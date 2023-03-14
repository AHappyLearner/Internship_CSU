
from cx_Oracle import *

conn = connect('scott/zmk123_@3316jf2639.qicp.vip:21413/demo')
cursor = conn.cursor()

sql_string = "select * from dept"
cursor.execute(sql_string)
conn.commit()

# conn.commit()
result = cursor.fetchall()
for row in result:
    print(row)
#
# print (cursor.rowcount)
# for row in data:
#     row=str(row)
#     print(row)
#     row.replace('(','')
#     row.replace(')','')
#     row.replace(',','')
#     print(row)
#
# print(len(data))
cursor.close()
conn.close()

