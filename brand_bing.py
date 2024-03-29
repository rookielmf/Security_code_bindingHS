from get_security_code import bind_security_code
import os

def main():
    folder_path = input("请选择防伪码的测试环境 (输入 1 为 test 环境, 输入 2 为 beta 环境): ")
    if folder_path == "1":
        folder_path = "data_test"
    elif folder_path == "2":
        folder_path = "data_beta"
    else:
        print("无效输入，退出...")
        return

    brands = [
        'elfbar', 'lostmary', 'ELFLIQ', 'FunkyRepublic', 'EBDesign',
        'EBCREATE', 'FUNKY_LANDS', 'HIDESEEK', 'RabBeatsVape', 'LOSTY_LOSTY',
        'MAD_EYES', 'OFF_STAMP', 'URBAN_TALE', 'LOSGAL', 'MARYLIQ'
    ]

    print("品牌编号（1-15）:")
    for i, brand in enumerate(brands, 1):
        print(f"{i}. {brand}", end='\t')
        if i % 5 == 0:  # 每打印5个品牌换行
            print()

    brand_selection = input("请选择需要创建防伪码的品牌编号: ")
    if not brand_selection.isdigit() or int(brand_selection) < 1 or int(brand_selection) > 15:
        print("无效输入，退出...")
        return

    brand_index = int(brand_selection) - 1
    selected_brand = brands[brand_index]

    secuirty_code_out_files = os.path.join(folder_path, selected_brand + '_secuirty_code_out.txt')

    with open(secuirty_code_out_files, 'w'):
        pass

    HS_security_id = [17641, 17642, 17643, 17644, 17645]
    num = len(HS_security_id)
    print(num)

    bind_security_code(folder_path, selected_brand, HS_security_id, num)


if __name__ == '__main__':
    main()
