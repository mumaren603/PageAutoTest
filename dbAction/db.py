#Author: ls Liu
import cx_Oracle as Oracle

'''这边需要优化，不能每条用例执行查数据都需要连接数据库，需要一次性连接后，所有用例在此连接上执行查询等操作'''
class DBAction():
    def __init__(self,dbConnInfo):
        self.conn = None
        try:
            self.conn = Oracle.connect(dbConnInfo)
            print("数据库连接信息：%s" %self.conn)
            print("数据库连接成功")
        except Exception as e:
            print(e)


    def SqlExecute(self,sql):
        cursor = self.conn.cursor()  #使用cursor()方法获取操作游标
        try:
            res = cursor.execute(sql)
            queryResult = res.fetchone()
            queryResult = queryResult[0]
            return queryResult
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            # conn.close()

    #单独写一个关闭连接操作而不是放在SqlExecute()里，是因为建立一次连接后可能会执行多次查询，最后统一关闭数据库连接。
    def closeConn(self):
        self.conn.close()

