#!/usr/bin/env python
# -*- coding:utf-8 -*- 

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: 2014.12.12
File Name   : parsing_module_dependency.py
Description : 
'''

## parsing_module_dependency.py
# python parsing_module_dependency.py <python模块包文件路径>
#
# 运行环境需要安装：pip, virtualenv
# 安装pip:
#   curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
#   python get-pip.py
# 安装virtualenv
#   pip install virtualenv
#
# eg: python parsing_module_dependency.py /tmp/nova-2014.1.tar.gz
#
# 脚本实现:
# 解析出指定模块包所依赖的所有模块包,生成依赖树文件：dependency_tree.log
# 注：如果想保留这些依赖模块，可注释掉倒数第一行有效代码
##

import sys,time,os
import re
import logging
import shutil # 文件的复制，移动等操作

TOPDIR    = os.getcwd()
PYPI_DIR  = TOPDIR + '/pypi'
INFO_LOG  = TOPDIR + '/run.log'
DEPENDENCY_TREE_LOG = TOPDIR + '/dependency_tree.log'
# 设置格式缩进度
INDENT = []

logging.basicConfig(filename=INFO_LOG, level=logging.DEBUG)

# 记录模块依赖关系
def readlog(content=''):
    logfile = DEPENDENCY_TREE_LOG
    try:
        fph = open(logfile, 'a')
        fph.write(''.join(INDENT) + content + '\n')
    except IOError as err:
        print(err)
    finally:
        fph.close()

# 清理缓存时创建的临时目录
def clean_temp_dir (tmp_dir):
    if os.path.isdir(tmp_dir):
        cmd='rm -rf ' + tmp_dir
        os.system( cmd )
    else:
        print 'Not clean dir: ' + tmp_dir
        logging.debug("Not clean dir: {0}".format(tmp_dir))
    print "---clean dir: " + tmp_dir

# 创建临时目录
def make_temp_dir ():
    temp_dir = '/tmp/' +  str(time.time())
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
        logging.debug("has exists dir: {0}".format(temp_dir))
    os.chdir(temp_dir)
    return temp_dir

# 解析requires.txt中的依赖模块
def parsing_requires_modules(module_dir, module_name):
    print "INFO: parsing_requires_modules ..."

    cmd = 'find ' + module_dir + ' -name "*require*txt"'
    output = os.popen(cmd)
    ret = output.read().strip()
    if not ret:
        print 'not found requires file'
        logging.info("not found requires file in: {0}".format(module_name))
        return
    else:
        files_list = ret.split('\n')
        logging.info("found requires file in: {0}".format(module_name))
        logging.info("--: {0}".format('='.join(files_list)))

    temp_dir = make_temp_dir()
    cache_dir = temp_dir + '/cache'
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
        logging.debug("has exists dir: {0}".format(temp_dir))

    os.chdir(cache_dir)

    for r_file in files_list:
        if os.path.isfile(r_file):
            cmd='virtualenv {0}; source {0}/bin/activate; pip install -r {1} --download={2} --no-use-wheel; deactivate'.format(module_name, r_file, cache_dir)
            os.system(cmd)

    pattern = re.compile(r".*[bg]?z[ip2]{0,3}$")
    for p_file in  os.listdir(cache_dir):
        packagefile = '/'.join([cache_dir, p_file])
        if pattern.match(packagefile):
            print 'need unpack file: ' + packagefile
            unpack_module_package( packagefile )
        else:
            print 'error file: ' + packagefile

    os.chdir(TOPDIR)
    clean_temp_dir(temp_dir)

# 创建临时目录，解压模块包
def unpack_module_package(package_dirname):
    print "#INFO: unpack_module_package ..."

    package_name    = os.path.basename(package_dirname)
    module_name     = '-'.join(package_name.split('-')[0:-1])
    pypi_module_dir = PYPI_DIR + '/' + module_name
    pypi_module_dirname = '/'.join([pypi_module_dir, package_name])

    # 验证将要解析的包是否存在
    if not os.path.exists(package_dirname):
        print "Please check the input pack file exists: " + package_dirname
        logging.error("Not found: {0}".format(package_dirname))
        return None
    if not re.match(r".*[bg]?z[ip2]{0,3}$", package_dirname):
        print "Please check the input pack file type: " + package_dirname
        return None

    ## 判断当前包是否已经解析完成
    if os.path.exists(pypi_module_dirname):
        print "has this module: " + package_name
        logging.info("has parsing module: {0}".format(package_name))
        return None
    else:
        # 缓存模块包到指定目录
        if not os.path.isdir(pypi_module_dir):
            os.makedirs(pypi_module_dir)
        shutil.copyfile(package_dirname, pypi_module_dirname)

    temp_dir = make_temp_dir()

    unpack_name=''
    if package_name.endswith('zip'):
        cmd = 'unzip ' + package_dirname
        os.system (cmd)
        unpack_name = package_name.replace('.zip', '')
    elif package_name.endswith('tgz'):
        cmd = 'tar zxvf ' + package_dirname
        os.system (cmd)
        unpack_name = package_name.replace('.tgz', '')
    elif package_name.endswith('tar.gz'):
        cmd = 'tar zxvf ' + package_dirname
        os.system (cmd)
        unpack_name = package_name.replace('.tar.gz', '')
    elif package_name.endswith('bz2'):
        cmd = 'tar jxf ' + package_dirname
        os.system (cmd)
        unpack_name = package_name.replace('.bz2', '')
    else:
        print "Unable to determine file type: " + package_name
        logging.error("Unable to determine file type: ".format(package_name))

    module_dir = temp_dir + '/' + unpack_name

    ## 解析当前包中的 requires 文件，缓存其中的模块包列表
    logging.info("start parsing module: {0}".format(package_name))
    readlog(package_name)
    INDENT.append('|  ')
    parsing_requires_modules(module_dir, module_name)
    if INDENT:
        INDENT.pop()
    else:
        logging.error("indent error !")

    ## 解析完成后，清理创建的临时目录
    clean_temp_dir(temp_dir)
    return True


if __name__ == '__main__':
    packagefile = sys.argv[1]
    if not packagefile.startswith('/'):
        packagefile = '/'.join([TOPDIR, packagefile])
    ret = unpack_module_package( packagefile )
    if ret:
        print '\nThe {0} parsing is complete'.format(os.path.basename(packagefile))

    os.remove(INFO_LOG)
    # 清理依赖包文件，如果需要依赖包，可把下面一行注释掉
    clean_temp_dir(PYPI_DIR)

## end script ##

