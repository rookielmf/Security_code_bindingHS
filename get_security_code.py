'''
@create : lisa
@file :security_code
@Date :2024/3/1
@desc :

'''
import os
from database import connect_database

def bind_security_code(folder_path,brand,HS_securitycode_id,num):
    secuirty_code_files = os.path.join(folder_path,brand + '_secuirty_code.txt')
    secuirty_code_files_out = os.path.join(folder_path,brand + '_secuirty_code_out.txt')
    # 打开文件
    with open(secuirty_code_files, 'r') as f:
        lines = f.readlines()  # 读取所有行
        if not lines or len(lines)<num:
            print("文件为空或不足num")
        else:
            #"文件不为空"
            lines.reverse()  # 反转顺序
            for i in range(num):# 从尾部开始循环
                lines[i] = lines[i].strip()  # 获取防伪码，去除末尾的换行符
                # 使用 split() 分隔，此处以逗号作为分隔符
                pieces = lines[i].split(',')
                traceability_code=pieces[0]
                secuirty_code_link=pieces[1]
                # 连接数据库
                query = "update bw_security_code.tbl_security_code set security_code= %s where id = %s;"
                connection = connect_database(query, traceability_code,HS_securitycode_id[i])

                print(lines[i])
                with open(secuirty_code_files_out, 'a') as f:
                    f.write(traceability_code+','+secuirty_code_link+'\n')

            del lines[:num]  # 删除前x行
            lines.reverse() #再次反转行列表，将其恢复到原始顺序
            # 若处理成功，则将空行写回文件
            with open(secuirty_code_files, 'w')as f:
                f.writelines(lines)





#连接数据库
# security_code1 = "58102086709778445"
# query = "SELECT id FROM bw_security_code.tbl_security_code where security_code =%s"
# connection = connect_database(query,security_code1)

