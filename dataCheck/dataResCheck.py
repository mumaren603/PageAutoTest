'''
用于业务登簿后数据库结果检查
'''
from dbAction.db import DBAction

class dataResCheck():
    def __init__(self,dbInfo):
        self.db_qj_conn = DBAction(dbInfo.get('qj'))
        self.db_dj_conn = DBAction(dbInfo.get('dj'))

    # 土地首次/转移/变更登记
    def landRegisterDataCheck(self,bdcdyh,qlrmc):
        try:
            sql_dj_jsydsyq = "select count(1) from djjgk.dj_jsydsyq where zt='1' and sfyx=1 and bdcdyh='" + bdcdyh + "'"
            res_dj_jsydsyq = self.db_dj_conn.SqlExecute(sql_dj_jsydsyq)
            print("dj_jsydsyq:", res_dj_jsydsyq,type(res_dj_jsydsyq))

            sql_dj_tdxx = "select count(1) from djjgk.dj_tdxx where zt='1' and sfyx=1 and bdcdyh='" + bdcdyh + "'and qlrmc='" + qlrmc + "'"
            res_dj_tdxx = self.db_dj_conn.SqlExecute(sql_dj_tdxx)
            print("dj_tdxx:", res_dj_tdxx,type(res_dj_tdxx))

            sql_dj_zdjbxx = "select count(1) from djjgk.dj_zdjbxx where zt='1' and sfyx=1 and bdcdyh='" + bdcdyh + "'and qlrmc='" + qlrmc + "'"
            res_dj_zdjbxx = self.db_dj_conn.SqlExecute(sql_dj_zdjbxx)
            print("dj_zdjbxx:", res_dj_zdjbxx,type(res_dj_zdjbxx))

            sql_dj_djb = "select count(1) from djjgk.dj_djb  where  zt='1'and sfyx=1 and zdzhdm='" + bdcdyh[:19] + "'"
            res_dj_djb = self.db_dj_conn.SqlExecute(sql_dj_djb)
            print("dj_djb:", res_dj_djb,type(res_dj_djb))

            sql_dj_djben = "select count(1) from djjgk.dj_djben where zt='1' and sfyx=1 and bdcdyh='" + bdcdyh +"'and qlrmc='" + qlrmc + "'"
            res_dj_djben = self.db_dj_conn.SqlExecute(sql_dj_djben)
            print("dj_djben:", res_dj_djben,type(res_dj_djben))

            sql_dj_zs = "select count(1) from djjgk.dj_zs where zt='1' and sfyx=1 and bdcdyh='"+ bdcdyh +"'and qlr='" + qlrmc + "'"
            res_dj_zs = self.db_dj_conn.SqlExecute(sql_dj_zs)
            print("dj_zs:", res_dj_zs,type(res_dj_zs))

            sql_dj_qlrgl = "select count(1) from  djjgk.dj_qlrgl where zt='1' and sfyx=1 and bdcdyh='"+ bdcdyh +"'and qlrmc='" + qlrmc + "'"
            res_dj_qlrgl = self.db_dj_conn.SqlExecute(sql_dj_qlrgl)
            print("dj_qlrgl:", res_dj_qlrgl,type(res_dj_qlrgl))

            sql_dj_qlr = "select count(1) from dj_qlr where zt='1' and sfyx=1 and id =(select ryqkid from dj_qlrgl where zt='1' and sfyx=1 and bdcdyh='"+ bdcdyh +"'and qlrmc='" + qlrmc + "')"
            res_dj_qlr = self.db_dj_conn.SqlExecute(sql_dj_qlr)
            print("dj_qlr:", res_dj_qlr, type(res_dj_qlr))

            if res_dj_jsydsyq and res_dj_tdxx and res_dj_zdjbxx and res_dj_djb and res_dj_djben and res_dj_qlrgl and res_dj_qlr and res_dj_zs:
                print("数据库数据归档正确!")
                return True
            else:
                print("数据库数据归档错误!")
                return False
        except Exception as e:
                print(e)
        finally:
            # 关闭数据库连接
            self.db_dj_conn.closeConn()
            self.db_qj_conn.closeConn()

    # 土地注销登记
    def landCancleRegisterDataCheck(self,bdcdyh):
        try:
            sql_dj_jsydsyq = "select count(1) from djjgk.dj_jsydsyq where zt='2' and sfyx=1 and bdcdyh='" + bdcdyh + "'"
            res_dj_jsydsyq = self.db_dj_conn.SqlExecute(sql_dj_jsydsyq)
            print("dj_jsydsyq:", res_dj_jsydsyq,type(res_dj_jsydsyq))

            sql_dj_tdxx = "select count(1) from dj_tdxx where zt='2' and sfyx=1 and bdcdyh='" + bdcdyh + "'"
            res_dj_tdxx = self.db_dj_conn.SqlExecute(sql_dj_tdxx)
            print("dj_tdxx:", res_dj_tdxx,type(res_dj_tdxx))

            sql_dj_zdjbxx = "select count(1) from dj_zdjbxx where zt='2' and sfyx=1 and bdcdyh='" + bdcdyh + "'"
            res_dj_zdjbxx = self.db_dj_conn.SqlExecute(sql_dj_zdjbxx)
            print("dj_zdjbxx:", res_dj_zdjbxx,type(res_dj_zdjbxx))

            sql_dj_djb = "select count(1) from dj_djb  where  zt='1'and sfyx=1 and zdzhdm='" + bdcdyh[:19] + "'"
            res_dj_djb = self.db_dj_conn.SqlExecute(sql_dj_djb)
            print("dj_djb:", res_dj_djb,type(res_dj_djb))

            sql_dj_djben = "select count(1) from dj_djben where zt='2' and sfzx=1 and sfyx=0 and bdcdyh='" + bdcdyh +"'"
            res_dj_djben = self.db_dj_conn.SqlExecute(sql_dj_djben)
            print("dj_jsydsyq:", res_dj_djben,type(res_dj_djben))

            sql_dj_zs = "select count(1) from dj_zs where zt='2' and sfyx=1 and bdcdyh='"+ bdcdyh +"'"
            res_dj_zs = self.db_dj_conn.SqlExecute(sql_dj_zs)
            print("dj_zs:", res_dj_zs,type(res_dj_zs))

            sql_dj_qlrgl = "select count(1) from  dj_qlrgl where zt='2' and sfyx=1 and bdcdyh='"+ bdcdyh +"'"
            res_dj_qlrgl = self.db_dj_conn.SqlExecute(sql_dj_qlrgl)
            print("dj_qlrgl:", res_dj_qlrgl,type(res_dj_qlrgl))

            sql_dj_qlr = "select count(1) from dj_qlr where zt='1' and sfyx=1 and id in(select ryqkid from dj_qlrgl where zt='2' and sfyx=1 and bdcdyh='"+ bdcdyh +"')"
            res_dj_qlr = self.db_dj_conn.SqlExecute(sql_dj_qlr)
            print("dj_qlr:", res_dj_qlr,type(res_dj_qlr))

            sql_dc_djdcbxx_his = "select count(1) from dc_djdcbxx_his where zt='2'and bdcdyh='"+ bdcdyh +"'"
            res_dc_djdcbxx_his = self.db_qj_conn.SqlExecute(sql_dc_djdcbxx_his)
            print("dc_djdcbxx_his:", res_dc_djdcbxx_his,type(res_dc_djdcbxx_his))

            if res_dj_jsydsyq and res_dj_tdxx and res_dj_zdjbxx and res_dj_djb and res_dj_djben and res_dj_qlrgl and res_dj_qlr and res_dj_zs:
                print("数据库数据归档正确!")
                return True
            else:
                print("数据库数据归档错误!")
                return False

        except Exception as e:
                print(e)
        finally:
            # 关闭数据库连接
            self.db_dj_conn.closeConn()
            self.db_qj_conn.closeConn()

    # 房屋登记
    def houseRegisterDataCheck(self,bdcdyh,qlrmc):
        try:
            sql_dj_fdcq2 = "select count(1) from dj_fdcq2 where zt='1' and sfyx=1 and bdcdyh='" + bdcdyh + "'"
            res_dj_fdcq2 = self.db_dj_conn.SqlExecute(sql_dj_fdcq2)
            print("dj_fdcq2:", res_dj_fdcq2,type(res_dj_fdcq2))

            sql_dj_hxx = "select count(1) from dj_hxx where zt='1' and sfyx=1 and bdcdyh='" + bdcdyh + "'"
            res_dj_hxx = self.db_dj_conn.SqlExecute(sql_dj_hxx)
            print("dj_hxx:", res_dj_hxx,type(res_dj_hxx))

            sql_dj_djben = "select count(1) from dj_djben t where zt='1' and sfyx=1 and sfysczql=1 and id in(select djbid from dj_fdcq2 where bdcdyh='" + bdcdyh + "')"
            res_dj_djben = self.db_dj_conn.SqlExecute(sql_dj_djben)
            print("dj_djben:", res_dj_djben,type(res_dj_djben))

            sql_dj_fdcq2_djben_zs = "select count(1) from dj_fdcq2_djben_zs where sfyx=1 and bdcdyh='" + bdcdyh + "'and qlrmc='" + qlrmc + "'"
            res_dj_fdcq2_djben_zs = self.db_dj_conn.SqlExecute(sql_dj_fdcq2_djben_zs)
            print("dj_fdcq2_djben_zs:", res_dj_fdcq2_djben_zs,type(res_dj_fdcq2_djben_zs))

            sql_dj_qlrgl ="select count(1) from  dj_qlrgl where zt='1' and sfyx=1 and ryzl='1'and bdcdyh='"+ bdcdyh +"'and qlrmc='" + qlrmc + "'"
            res_dj_qlrgl = self.db_dj_conn.SqlExecute(sql_dj_qlrgl)
            print("dj_qlrgl:", res_dj_qlrgl,type(res_dj_qlrgl))

            sql_dj_qlr = "select count(1) from dj_qlr where id in(select ryqkid from dj_qlrgl where zt='1' and sfyx=1 and ryzl='1'and bdcdyh='"+ bdcdyh +"'and qlrmc='" + qlrmc + "')"
            res_dj_qlr = self.db_dj_conn.SqlExecute(sql_dj_qlr)
            print("dj_qlr:", res_dj_qlr,type(res_dj_qlr))

            sql_dj_zs = "select count(1) from dj_zs where zt='1' and sfyx=1 and bdcdyh='" + bdcdyh + "'and qlr = '" + qlrmc + "'"
            res_dj_zs = self.db_dj_conn.SqlExecute(sql_dj_zs)
            print("dj_zs:", res_dj_zs,type(res_dj_zs))

            if res_dj_fdcq2 and res_dj_hxx and res_dj_fdcq2_djben_zs and res_dj_djben and res_dj_djben and res_dj_qlrgl and res_dj_qlr and res_dj_zs:
                print("数据库数据归档正确!")
                return True
            else:
                print("数据库数据归档错误!")
                return False

        except Exception as e:
                print(e)
        finally:
            # 关闭数据库连接
            self.db_dj_conn.closeConn()
            self.db_qj_conn.closeConn()

    # 公建配套登记
    def gjptRegisterDataCheck(self,bdcdyh):
        try:
            sql_yw_sqxx = "select ywh from YWBDK.yw_sqxx where ajzt='2' and bdcdyh='" + bdcdyh + "'"
            res_yw_sqxx = self.db_dj_conn.SqlExecute(sql_yw_sqxx)
            print("yw_sqxx:", res_yw_sqxx,type(res_yw_sqxx))

            sql_dj_fsssxx = "select count(1) from dj_fsssxx where zt='1' and sfyx=1 and bz2='" + sql_yw_sqxx + "'"
            res_dj_fsssxx = self.db_dj_conn.SqlExecute(sql_dj_fsssxx)
            print("dj_fsssxx:", res_dj_fsssxx,type(res_dj_fsssxx))

            sql_dj_jzwqfsyqyzgybf = "select count(1) from dj_jzwqfsyqyzgybf t where zt='1' and sfyx=1 and bz2='" + sql_yw_sqxx + "'"
            res_dj_jzwqfsyqyzgybf = self.db_dj_conn.SqlExecute(sql_dj_jzwqfsyqyzgybf)
            print("dj_jzwqfsyqyzgybf:", res_dj_jzwqfsyqyzgybf,type(res_dj_jzwqfsyqyzgybf))

            sql_dj_qlrgl ="select count(1) from  dj_qlrgl where sfyx=1 and  bz2='" + sql_yw_sqxx + "'"
            res_dj_qlrgl = self.db_dj_conn.SqlExecute(sql_dj_qlrgl)
            print("dj_qlrgl:", res_dj_qlrgl,type(res_dj_qlrgl))

            sql_dj_qlr = "select count(1) from dj_qlr where id in(select ryqkid from dj_qlrgl where sfyx=1 and  bz2='" + sql_yw_sqxx + "')"
            res_dj_qlr = self.db_dj_conn.SqlExecute(sql_dj_qlr)
            print("dj_qlr:", res_dj_qlr,type(res_dj_qlr))

            if sql_dj_fsssxx and sql_dj_jzwqfsyqyzgybf and sql_dj_qlrgl and sql_dj_qlr:
                print("数据库数据归档正确!")
                return True
            else:
                print("数据库数据归档错误!")
                return False

        except Exception as e:
                print(e)
        finally:
            # 关闭数据库连接
            self.db_dj_conn.closeConn()
            self.db_qj_conn.closeConn()


    # 抵押(土地、房屋)登记
    def dyRegisterDataCheck(self,bdcdyh,qlrmc):
        try:
            sql_dj_dy = "select count(1) from dj_dy where zt='1' and sfyx=1 and bdcdyh='" + bdcdyh + "'and qlrmc = '" + qlrmc + "'"
            res_dj_dy = self.db_dj_conn.SqlExecute(sql_dj_dy)
            print("dj_dy:", res_dj_dy)

            sql_dj_djben = "select count(1) from dj_djben where zt='1' and sfyx=1 and sfdy=1 and sfysczql=1 and id in(select djbid from dj_dy where bdcdyh='" + bdcdyh + "')"
            res_dj_djben = self.db_dj_conn.SqlExecute(sql_dj_djben)
            print("dj_djben:", res_dj_djben)

            sql_dj_dy_djben_zm = "select count(1) from dj_dy_djben_zm where sfyx=1 and sfdy=1 and bdcdyh='" + bdcdyh + "'and qlr = '" + qlrmc + "'"
            res_dj_dy_djben_zm = self.db_dj_conn.SqlExecute(sql_dj_dy_djben_zm)
            print("dj_dy_djben_zm:", res_dj_dy_djben_zm)

            sql_dj_qlrgl = "select count(1) from  dj_qlrgl where zt='1' and sfyx=1 and ryzl='4'and bdcdyh='"+ bdcdyh +"'and qlrmc='" + qlrmc + "'"
            res_dj_qlrgl = self.db_dj_conn.SqlExecute(sql_dj_qlrgl)
            print("dj_qlrgl:", res_dj_qlrgl)

            sql_dj_qlr = "select count(1) from dj_qlr where id in(select ryqkid from dj_qlrgl where zt='1' and sfyx=1 and ryzl='4'and bdcdyh='"+ bdcdyh +"'and qlrmc='" + qlrmc + "')"
            res_dj_qlr = self.db_dj_conn.SqlExecute(sql_dj_qlr)
            print("dj_qlr:", res_dj_qlr)

            sql_dj_zm = "select count(1) from dj_zm where zt='1' and sfyx=1 and bdcdyh='" + bdcdyh + "'and qlr = '" + qlrmc + "'"
            res_dj_zm = self.db_dj_conn.SqlExecute(sql_dj_zm)
            print("dj_zm:", res_dj_zm)

            if res_dj_dy  and res_dj_dy_djben_zm and res_dj_djben and res_dj_djben and res_dj_qlrgl and res_dj_qlr and res_dj_zm:
                print("数据库数据归档正确!")
                return True
            else:
                print("数据库数据归档错误!")
                return False
        except Exception as e:
                print(e)
        finally:
            # 关闭数据库连接
            self.db_dj_conn.closeConn()
            self.db_qj_conn.closeConn()

    # 查封登记
    def cfRegisterDataCheck(self,bdcdyh,cfwj):
        try:
            sql_dj_cf = "select count(1) from dj_cf where zt='1' and sfyx=1 and bdcdyh='" + bdcdyh + "'and cfwj = '" +cfwj + "'"
            res_dj_cf = self.db_dj_conn.SqlExecute(sql_dj_cf)
            print("dj_cf:", res_dj_cf)

            sql_dj_djben = "select count(1) from dj_djben where zt='1' and sfyx=1 and sfcf=1 and id in(select djbid from dj_cf where bdcdyh='" + bdcdyh + "')"
            res_dj_djben = self.db_dj_conn.SqlExecute(sql_dj_djben)
            print("dj_djben:", res_dj_djben)

            if res_dj_cf  and res_dj_djben :
                print("数据库数据归档正确!")
                return True
            else:
                print("数据库数据归档错误!")
                return False
        except Exception as e:
                print(e)
        finally:
            # 关闭数据库连接
            self.db_dj_conn.closeConn()
            self.db_qj_conn.closeConn()



