import pymysql
from pymysql import cursors

db =pymysql.connect(host ='127.0.0.1',port=3306,user='root',password ='123456',db ='jd')
cur = db.cursor()

insert_sql = """
            insert into medicine(pro_nums,pro_main_cate,pro_price,pro_store)
            VALUES(%s, %s, %s, %s)
        """
cur.execute(insert_sql,({'pro_main_cate': '补肾壮阳', 'pro_nums': '4724916', 'pro_price': '49.80', 'pro_store': '仲景宛西制药官方旗舰店'}))

db.commit()    # 这里是db来commit，而不是cur，达到刷新到数据库的目的。
