import pymysql


# 连接数据库

db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='12345678',
                     database='country1',
                     charset='utf8')

# 获取游标
cur = db.cursor()

# 插入数据
data_list = []

for x in range(200000):
    name = 'Py87_%s' % x
    data_list.append(name)

# 插入语句
# 一个包最大 allowed_packet is 10586
# max_stmt_length = 1024000  ins sql语句的字符串长度
ins = 'insert into students(name) values(%s)'

# 批量插入数据
# 每一次插入都是一次磁盘网络IO  提高单位频率上的效率
cur.executemany(ins, data_list)

# 提交
db.commit()

# 关闭
cur.close()
db.close()
