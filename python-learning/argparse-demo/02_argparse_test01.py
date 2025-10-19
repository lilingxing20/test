"""
argparse 是 Python 标准库中的一个模块，用于解析命令行参数。它提供了一个灵活且易用的方式来处理命令行输入，允许你定义期望的参数、自动生成帮助信息，并执行类型转换、验证等操作。

使用 argparse 模块的一般步骤如下：
    创建解析器：使用 ArgumentParser() 创建一个解析器对象。
    添加参数：通过 add_argument() 方法来定义你期望的命令行参数。
    解析参数：使用 parse_args() 方法解析传递给脚本的命令行参数。
"""

import argparse

def main():
    # 定义一个ArgumentParser实例:
    parser = argparse.ArgumentParser(
        prog='backup', # 程序名
        description='Backup MySQL database.', # 描述
        epilog='Copyright(r), 2025' # 说明信息
    )
    # 定义位置参数:
    parser.add_argument('outfile')
    # 定义关键字参数:
    parser.add_argument('--host', default='localhost')
    # 此参数必须为int类型:
    parser.add_argument('--port', default='3306', type=int)
    # 允许用户输入简写的-u:
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('--database', required=True)
    # gz参数不跟参数值，因此指定action='store_true'，意思是出现-gz表示True:
    parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')


    # 解析参数:
    args = parser.parse_args()

    # 打印参数:
    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')

if __name__ == '__main__':
    main()

"""
运行示例：
python argparse_test01.py backup.sql.gz -u root -p 123456 --database testdb -gz

运行结果：
parsed args:
outfile = backup.sql.gz
host = localhost
port = 3306
user = root
password = 123456
database = testdb
gzcompress = True
"""
