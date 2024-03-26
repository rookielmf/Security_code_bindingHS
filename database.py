import pymysql
import paramiko
from sshtunnel import SSHTunnelForwarder

def connect_database(query,traceability_code,id):
    # SSH 连接信息
    ssh_host = '47.96.14.194'
    ssh_port = 22
    ssh_username = 'thomas'
    ssh_password = 'beta!@#$4321'

    # SSH隧道本地端口
    local_port = 3306

    # 数据库连接信息
    database_host = '127.0.0.1'# 因为您将通过SSH隧道连接，所以这里是本地主机
    database_port = 3306
    database_username = 'root'
    database_password = 'LK5VhKSZx3'
    database_name = 'bw_erp'

    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_username,
            ssh_password=ssh_password,
            remote_bind_address=(database_host, database_port)) as tunnel:
        db_connection = pymysql.connect(host='127.0.0.1', user=database_username,
                               passwd=database_password, db=database_name,
                               port=tunnel.local_bind_port)
        # print("数据库连接成功")


        #执行查询等操作
        cursor = db_connection.cursor()
        cursor.execute(query,(traceability_code,id))
        #提交事务
        db_connection.commit()
        # cursor.execute(query)
        # results = cursor.fetchall()

        # 关闭数据库连接和SSH连接
        cursor.close()
        # 当完成所有操作后，关闭数据库连接
        db_connection.close()
        # tunnel.close()




# def query_table(db_connection,query):
#
#     # 执行查询等操作
#     cursor = db_connection.cursor()
#     cursor.execute(query)
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#     # 关闭数据库连接和SSH连接
#     cursor.close()
#     db_connection.close()
    # ssh_client.close()