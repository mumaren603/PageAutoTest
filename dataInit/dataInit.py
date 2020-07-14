'''
数据初始化，即我们测试用例在运行过程中需要使用到数据预先准备好
'''

from dbAction.db import DBAction
class dataInit():
    def __init__(self,dbInfo):
        self.dbInfo = dbInfo
        self.db_qj_conn = DBAction(self.dbInfo.get('qj'))
        self.db_dj_conn = DBAction(self.dbInfo.get('dj'))

    ####################国有建设用地使用权##################
    # 土地首次登记数据
    def getLandFirstRegisterData(self):
        querySQL = "select bdcdyh from KJK.dc_djdcbxx where zt='1' and sfyx='0' and tdzl>'0' and dytdmjhj > '0' and qllx='3' and bdcdyh >'0' and rownum < 30 order by dbms_random.value()"
        queryRes = self.db_qj_conn.SqlExecute(querySQL)
        print("权籍查询数据：%s" % queryRes)
        # 检查该数据是否在登记平台做过登记,如果做过登记，发起流程会校验住，确保数据在权藉存在，在登记平台未做过登记
        queryJsydsyqSQL = "select count(1) from DJJGK.dj_jsydsyq where zt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        queryJsydsyqSQLRes = self.db_dj_conn.SqlExecute(queryJsydsyqSQL)
        print("登记平台数据条数为：%s" % queryJsydsyqSQLRes)
        if queryJsydsyqSQLRes:
            print("登记平台该土地信息已登记，重新获取数据！")
            return dataInit(self.dbInfo).getLandFirstRegisterData()  # 递归
        else:
            print("数据符合！数据为：%s" % queryRes)
            self.db_qj_conn.closeConn()
            self.db_dj_conn.closeConn()
            return queryRes

    # 土地转移/变更登记数据
    def getLandChangeRegisterData(self):
        querySQL = "select a.bdcdyh from (select djbid,bdcdyh from djjgk.dj_jsydsyq where qllx = '3' and zt = '1' and sfyx = 1 and bdcdyh not like '%9999%') a inner join (select id,bdcdyh from djjgk.dj_djben where sfdy = 0 and sfcf = 0 and sfzzdj = 0 and sfysczql = 1 and zt = '1' and sfyx = 1) b on a.djbid = b.id and rownum < 50 order by dbms_random.value()"
        queryRes = self.db_dj_conn.SqlExecute(querySQL)
        print("DJJGK查询数据：%s" % queryRes)
        #检查该数据是否存在待办件
        querySqxxSQL = "select count(1) from ywbdk.yw_sqxx where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxzbSQL = "select count(1) from ywbdk.yw_sqxxzb where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxSQLRes = self.db_dj_conn.SqlExecute(querySqxxSQL)
        querySqxxzbSQLRes = self.db_dj_conn.SqlExecute(querySqxxzbSQL)
        if querySqxxSQLRes or querySqxxzbSQLRes:
            print("该数据已在办理中，重新获取数据！")
            return dataInit(self.dbInfo).getLandChangeRegisterData()  # 递归
        else:
            print("数据符合！数据为：%s" % queryRes)
            self.db_qj_conn.closeConn()
            self.db_dj_conn.closeConn()
            return queryRes

    # 土地注销登记数据（没有房屋）
    def getLandCancleRegisterData(self):
        querySQL = "select a.bdcdyh from (select djbid,bdcdyh from djjgk.dj_jsydsyq where qllx = '3' and zt = '1' and sfyx = 1 and bdcdyh not like '%9999%') a inner join (select id,bdcdyh from djjgk.dj_djben where sfdy = 0 and sfcf = 0 and sfzzdj = 0 and sfysczql = 1 and zt = '1' and sfyx = 1) b on a.djbid = b.id and rownum < 50 order by dbms_random.value()"
        queryRes = self.db_dj_conn.SqlExecute(querySQL)
        print("DJJGK查询数据：%s" % queryRes)
        #检查该土地上是否存在现势房产
        queryHouseSQL = "select count(1) from djjgk.dj_fdcq2 where zt='1' and sfyx=1 and zddm='" + queryRes[:19] + "'"
        #检查该数据是否存在待办件
        querySqxxSQL = "select count(1) from ywbdk.yw_sqxx where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxzbSQL = "select count(1) from ywbdk.yw_sqxxzb where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        queryHouseSQLRes = self.db_dj_conn.SqlExecute(queryHouseSQL)
        querySqxxSQLRes = self.db_dj_conn.SqlExecute(querySqxxSQL)
        querySqxxzbSQLRes = self.db_dj_conn.SqlExecute(querySqxxzbSQL)
        if queryHouseSQLRes:
            print("该土地上存在现势房产，重新获取数据！")
            return dataInit(self.dbInfo).getLandCancleRegisterData()  # 递归
        elif querySqxxSQLRes or querySqxxzbSQLRes:
            print("该数据已在办理中，重新获取数据！")
            return dataInit(self.dbInfo).getLandCancleRegisterData()  # 递归
        else:
            print("数据符合！数据为：%s" % queryRes)
            self.db_dj_conn.closeConn()
            self.db_qj_conn.closeConn()
            return queryRes

    ####################国有建设用地使用权及房屋所有权##################
    # 商品房首次登记查询数据
    def getSpfFirstRegisterData(self):
        querySQL = "select a.bdcdyh from (select bdcdyh, fwbh, lszfwbh from kjk.dc_h_fwzk where zt = '1' and sfyx = '0' and fwxz > '0' and fwjg > '0' and fwyt1 > '0' and scjzmj > '0' and jgrq > '0' and bdcdyh like '%GB%' and (fwlx = '1' or fwlx = '2' or fwlx = '3' or fwlx = '4' or fwlx = '99'))a left join (select fwbh from kjk.dc_h where zt = '1' and bdcdyh > '0') b on a.fwbh = b.fwbh left join (select zddm, fwbh from kjk.dc_z where zt = '1') c on a.lszfwbh = c.fwbh left join (select zddm from kjk.dc_djdcbxx where zt = '1' and sfyx = '1') d on c.zddm = d.zddm  order by dbms_random.value()"
        queryRes = self.db_qj_conn.SqlExecute(querySQL)
        print("权籍查询数据为：%s" % queryRes)
        # 检查该数据是否存在待办件
        querySqxxSQL = "select count(1) from YWBDK.yw_sqxx t where t.SFYX = '1' and t.ajzt in ('1', '3', '6') and t.id in (select z.sqbid from ywbdk.yw_sqxxzb z where z.sfyx = '1' and bdcdyh = '" + queryRes + "')"
        # querySqxxSQL = "select count(1) from ywbdk.yw_sqxx where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        # querySqxxzbSQL = "select count(1) from ywbdk.yw_sqxxzb where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxSQLRes = self.db_dj_conn.SqlExecute(querySqxxSQL)
        # querySqxxzbSQLRes = self.db_dj_conn.SqlExecute(querySqxxzbSQL)
        if querySqxxSQLRes:
        # if querySqxxSQLRes or querySqxxzbSQLRes:
            print("该数据已在办理中，重新获取数据！")
            return dataInit(self.dbInfo).getSpfFirstRegisterData()  # 递归
        else:
            print("数据符合！数据为：%s" % queryRes)
            self.db_qj_conn.closeConn()
            self.db_dj_conn.closeConn()
            return queryRes


    # 自建房屋首次登记
    def getzjfwFirstRegisterData(self):
        querySQL = "select a.bdcdyh from （select * from dc_h_fwzk where zt = '1' and sfyx = '0' and fwlx = '1' or fwlx = '2' or fwlx = '3'  or fwlx = '4' or fwlx='5' or fwlx='99') a inner join (select * from dc_h where zt = '1') b on a.fwbh = b.fwbh inner join （select * from dc_z where zt = '1') c on a.lszfwbh = c.fwbh inner join (select * from dc_djdcbxx where zt = '1' and sfyx = '1') d on c.zddm = d.zddm where a.bdcdyh like '%GB%' order by dbms_random.value()"
        queryRes = self.db_qj_conn.SqlExecute(querySQL)
        print("权籍查询数据为：%s" % queryRes)
        # 检查该数据是否存在待办件
        querySqxxSQL = "select count(1) from YWBDK.yw_sqxx t where t.SFYX = '1' and t.ajzt in ('1', '3', '6') and t.id in (select z.sqbid from ywbdk.yw_sqxxzb z where z.sfyx = '1' and bdcdyh = '" + queryRes + "')"
        querySqxxSQLRes = self.db_dj_conn.SqlExecute(querySqxxSQL)
        if querySqxxSQLRes:
            print("该数据已在办理中，重新获取数据！")
            return dataInit(self.dbInfo).getzjfwFirstRegisterData()  # 递归
        else:
            print("数据符合！数据为：%s" % queryRes)
            self.db_qj_conn.closeConn()
            self.db_dj_conn.closeConn()
            return queryRes

        # 检查该数据是否存在土地抵押情况
        td_bdcdyh = queryRes.replace(queryRes[19:],'W00000000')
        queryTdDySQL= "select count(1) from dj_dy where zt='1' and sfyx=1 and bdcdyh='"+td_bdcdyh +"'"
        queryTdDySQLRes = self.db_dj_conn.SqlExecute(queryTdDySQL)
        # 检查该数据是否存在待办件
        querySqxxSQL = "select count(1) from ywbdk.yw_sqxx where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxzbSQL = "select count(1) from ywbdk.yw_sqxxzb where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxSQLRes = self.db_dj_conn.SqlExecute(querySqxxSQL)
        querySqxxzbSQLRes = self.db_dj_conn.SqlExecute(querySqxxzbSQL)
        if querySqxxSQLRes or querySqxxzbSQLRes:
            print("该数据已在办理中，重新获取数据！")
            return dataInit(self.dbInfo).getzjfwFirstRegisterData()  # 递归
        elif queryTdDySQLRes:
            print("该数据土地已被抵押，重新获取数据！")
            return dataInit(self.dbInfo).getzjfwFirstRegisterData()  # 递归
        else:
            print("数据符合！数据为：%s" % queryRes)
            self.db_qj_conn.closeConn()
            self.db_dj_conn.closeConn()
            return queryRes

    # 公建配套首次登记查询数据
    def getGjptFirstRegisterData(self):
        querySQL = "select distinct(d.bdcdyh) from （select * from kjk.dc_h_fwzk where zt = '1' and sfyx = '0' and (fwlx = '9901' or fwlx = '99')) a left join (select * from kjk.dc_h where zt = '1' and bdcdyh>'0') b on a.fwbh = b.fwbh left join （select * from kjk.dc_z where zt = '1') c on a.lszfwbh = c.fwbh left join (select * from kjk.dc_djdcbxx where zt = '1' and sfyx = '1') d on c.zddm = d.zddm where d.bdcdyh > '0' order by dbms_random.value()"
        queryRes = self.db_qj_conn.SqlExecute(querySQL)
        print("权籍查询数据为：%s" % queryRes)
        # 检查该数据是否存在待办件
        querySqxxSQL = "select count(1) from ywbdk.yw_sqxx where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxzbSQL = "select count(1) from ywbdk.yw_sqxxzb where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxSQLRes = self.db_dj_conn.SqlExecute(querySqxxSQL)
        querySqxxzbSQLRes = self.db_dj_conn.SqlExecute(querySqxxzbSQL)
        if querySqxxSQLRes or querySqxxzbSQLRes:
            print("该数据已在办理中，重新获取数据！")
            return dataInit(self.dbInfo).getGjptFirstRegisterData()  # 递归
        else:
            print("数据符合！数据为：%s" % queryRes)
            self.db_qj_conn.closeConn()
            self.db_dj_conn.closeConn()
            return queryRes


    #商品房首次转移登记查询数据
    def getSpfOrClfChangeRegisterData(self):
        querySQL = "select a.bdcdyh from (select * from dj_fdcq2 a where a.qllx=4 and a.zt=1 and a.sfyx=1 and a.bdcdyh not like '%9999%' and a.fwxz=0) a inner join (select * from dj_djben b where b.sfdy=0 and b.sfcf=0 and b.sfzzdj=0 and b.sfyg=0 and b.sfysczql=1 and b.zt=1 and b.sfyx=1) b on a.djbid=b.id and rownum <50 order by dbms_random.value()"
        queryRes = self.db_dj_conn.SqlExecute(querySQL)
        print("DJJGK查询数据：%s" % queryRes)
        # 检查该数据是否存在待办件
        querySqxxSQL = "select count(1) from ywbdk.yw_sqxx where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxzbSQL = "select count(1) from ywbdk.yw_sqxxzb where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxSQLRes = self.db_dj_conn.SqlExecute(querySqxxSQL)
        querySqxxzbSQLRes = self.db_dj_conn.SqlExecute(querySqxxzbSQL)
        if querySqxxSQLRes or querySqxxzbSQLRes:
            print("该数据已在办理中，重新获取数据！")
            return dataInit(self.dbInfo).getSpfFirstChangeData()  # 递归
        else:
            print("数据符合！数据为：%s" % queryRes)
            self.db_qj_conn.closeConn()
            self.db_dj_conn.closeConn()
            return queryRes

    ####################抵押权##################
    #土地首次抵押查询数据
    def getLandFirstDyData(self):
        querySQL = "select a.bdcdyh from (select djbid,bdcdyh from dj_jsydsyq where qllx = '3' and zt = '1' and sfyx = 1 and bdcdyh not like '%9999%') a inner join (select id,bdcdyh from dj_djben where sfdy = 0 and sfcf = 0 and sfzzdj = 0 and sfysczql = 1 and zt = '1' and sfyx = 1) b on a.djbid = b.id and rownum < 50 order by dbms_random.value()"
        queryRes = self.db_dj_conn.SqlExecute(querySQL)
        print("DJJGK查询数据：%s" % queryRes)
        # 检查该数据是否存在待办件
        querySqxxSQL = "select count(1) from ywbdk.yw_sqxx where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxzbSQL = "select count(1) from ywbdk.yw_sqxxzb where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxSQLRes = self.db_dj_conn.SqlExecute(querySqxxSQL)
        querySqxxzbSQLRes = self.db_dj_conn.SqlExecute(querySqxxzbSQL)
        if querySqxxSQLRes or querySqxxzbSQLRes:
            print("该数据已在办理中，重新获取数据！")
            return dataInit(self.dbInfo).getLandFirstDyData()  # 递归
        else:
            print("数据符合！数据为：%s" % queryRes)
            self.db_qj_conn.closeConn()
            self.db_dj_conn.closeConn()
            return queryRes

        # 土地抵押转移查询数据
    def getLandDyChangeData(self):
        querySQL = "select a.bdcdyh from (select djbid,bdcdyh from dj_jsydsyq where qllx = '3' and zt = '1' and sfyx = 1 and bdcdyh not like '%9999%') a inner join (select id,bdcdyh from dj_djben where sfdy = 1 and sfcf = 0 and sfzzdj = 0 and sfysczql = 1 and zt = '1' and sfyx = 1) b on a.djbid = b.id and rownum < 50 order by dbms_random.value()"
        queryRes = self.db_dj_conn.SqlExecute(querySQL)
        print("DJJGK查询数据：%s" % queryRes)
        # 检查该数据是否存在待办件
        querySqxxSQL = "select count(1) from ywbdk.yw_sqxx where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxzbSQL = "select count(1) from ywbdk.yw_sqxxzb where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxSQLRes = self.db_dj_conn.SqlExecute(querySqxxSQL)
        querySqxxzbSQLRes = self.db_dj_conn.SqlExecute(querySqxxzbSQL)
        if querySqxxSQLRes or querySqxxzbSQLRes:
            print("该数据已在办理中，重新获取数据！")
            return dataInit(self.dbInfo).getLandFirstDyData()  # 递归
        else:
            print("数据符合！数据为：%s" % queryRes)
            self.db_qj_conn.closeConn()
            self.db_dj_conn.closeConn()
            return queryRes

    #不动产首次抵押查询数据
    def getHouseFirstDyRegisterData(self):
        querySQL = "select a.bdcdyh from (select * from dj_fdcq2 a where a.qllx=4 and a.zt=1 and a.sfyx=1 and a.bdcdyh not like '%9999%' and a.fwxz=0) a inner join (select * from dj_djben b where b.sfdy=0 and b.sfcf=0 and b.sfzzdj=0 and b.sfyg=0 and b.sfysczql=1 and b.zt=1 and b.sfyx=1) b on a.djbid=b.id and rownum <50 order by dbms_random.value()"
        queryRes = self.db_dj_conn.SqlExecute(querySQL)
        print("DJJGK查询数据：%s" % queryRes)
        # 检查该数据是否存在待办件
        querySqxxSQL = "select count(1) from ywbdk.yw_sqxx where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxzbSQL = "select count(1) from ywbdk.yw_sqxxzb where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxSQLRes = self.db_dj_conn.SqlExecute(querySqxxSQL)
        querySqxxzbSQLRes = self.db_dj_conn.SqlExecute(querySqxxzbSQL)
        if querySqxxSQLRes or querySqxxzbSQLRes:
            print("该数据已在办理中，重新获取数据！")
            return dataInit(self.dbInfo).getLandFirstDyData()  # 递归
        else:
            print("数据符合！数据为：%s" % queryRes)
            self.db_qj_conn.closeConn()
            self.db_dj_conn.closeConn()
            return queryRes

    #不动产抵押转移查询数据
    def getHouseDyChangeRegisterData(self):
        querySQL = "select a.bdcdyh from (select * from dj_fdcq2 a where a.qllx=4 and a.zt=1 and a.sfyx=1 and a.bdcdyh not like '%9999%' and a.fwxz=0) a inner join (select * from dj_djben b where b.sfdy=1 and b.sfcf=0 and b.sfzzdj=0 and b.sfyg=0 and b.sfyy=0 and b.sfysczql=1 and b.zt=1 and b.sfyx=1) b on a.djbid=b.id and rownum <50 order by dbms_random.value()"
        queryRes = self.db_dj_conn.SqlExecute(querySQL)
        print("DJJGK查询数据：%s" % queryRes)
        # 检查该数据是否存在待办件
        querySqxxSQL = "select count(1) from ywbdk.yw_sqxx where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxzbSQL = "select count(1) from ywbdk.yw_sqxxzb where ajzt='1' and sfyx=1 and bdcdyh='" + queryRes + "'"
        querySqxxSQLRes = self.db_dj_conn.SqlExecute(querySqxxSQL)
        querySqxxzbSQLRes = self.db_dj_conn.SqlExecute(querySqxxzbSQL)
        if querySqxxSQLRes or querySqxxzbSQLRes:
            print("该数据已在办理中，重新获取数据！")
            return dataInit(self.dbInfo).getHouseDyChangeRegisterData()  # 递归
        else:
            print("数据符合！数据为：%s" % queryRes)
            self.db_qj_conn.closeConn()
            self.db_dj_conn.closeConn()
            return queryRes

    ####################查封登记##################
    #查封登记（土地）
    def getLandSeizureRegisterData(self):
        querySQL = "select a.bdcdyh from (select djbid,bdcdyh from dj_jsydsyq where qllx = '3' and zt = '1' and sfyx = 1 and bdcdyh not like '%9999%') a inner join (select id,bdcdyh from dj_djben where sfdy = 0 and sfcf = 0 and sfzzdj = 0 and sfysczql = 1 and zt = '1' and sfyx = 1) b on a.djbid = b.id and rownum < 50 order by dbms_random.value()"
        queryRes = db.DBAction(tzdj).SqlExecute(querySQL)
        return queryRes

    # #查封登记（房屋 ）
    # def getHouseSeizureRegisterData(self):
    #     querySQL = "select a.bdcdyh from (select * from dj_fdcq2 a where a.qllx=4 and a.zt=1 and a.sfyx=1 and a.bdcdyh not like '%9999%' and a.fwxz=0) a inner join (select * from dj_djben b where b.sfdy=0 and b.sfcf=0 and b.sfzzdj=0 and b.sfyg=0 and b.sfysczql=1 and b.zt=1 and b.sfyx=1) b on a.djbid=b.id and rownum <50 order by dbms_random.value()"
    #     queryRes = db.DBAction(tzdj).SqlExecute(querySQL)
    #     return queryRes


