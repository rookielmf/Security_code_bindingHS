'''
@create : lisa
@file :security_code
@Date :2024/3/6
@desc :
'''
from get_security_code import bind_security_code
import os

def main():
    # folder_path = 'data_test'  # 文件夹路径
    folder_path = 'data_beta'  # 文件夹路径
    #品牌站枚举
    brands = ['elfbar','lostmary','ELFLIQ','FunkyRepublic','EBDesign','EBCREATE','FUNKY_LANDS','HIDESEEK','RabBeatsVape','LOSTY_LOSTY','MAD_EYES','OFF_STAMP','URBAN_TALE','LOSGAL','MARYLIQ']

    secuirty_code_out_files = os.path.join(folder_path,brands[0]+'_secuirty_code_out.txt')  # 输出文件路径

    #调用绑定防伪码方法之前清空OUT TXT
    with open(secuirty_code_out_files,'w'):
        pass
    #HS数据库防伪码ID枚举
    HS_security_id =[17641,17642,17643,17644,17645]
    #HS数据库防伪码ID数量
    num = len(HS_security_id)
    print(num)
    #调用绑定防伪码方法
    bind_security_code(folder_path,brands[0],HS_security_id,num)

if __name__ == '__main__':
    main()
