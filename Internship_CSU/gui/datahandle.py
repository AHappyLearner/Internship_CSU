import cx_Oracle
class dataoperate(object):
    def initial(self,txt):#连接数据库
        self.conn=cx_Oracle.connect(txt)
        self.cursor=self.conn.cursor()
    def getcursor(self):
        return self.cursor
