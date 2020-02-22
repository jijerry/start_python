# !usr/bin/env python

# encoding:utf-8

'''

__Author__:jerry

功能：判断一个字符串是否是合法IP地址

'''

import re


def judge_legal_ip(one_str):
    '''

    正则匹配方法

    判断一个字符串是否是合法IP地址

    '''

    compile_ip = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')

    if compile_ip.match(one_str):

        return True

    else:

        return False


def judge_legal_ip2(one_str):
    '''

    简单的字符串判断

    '''

    if '.' not in one_str:

        return False

    elif one_str.count('.') != 3:

        return False

    else:

        flag = True

        one_list = one_str.split('.')

        for one in one_list:

            try:

                one_num = int(one)

                if one_num >= 0 and one_num <= 255:

                    pass

                else:

                    flag = False

            except:

                flag = False

        return flag


if __name__ == '__main__':

    ip_list = ['', '172.31.137.251', '100.10.0.1000', '1.1.1.1', '12.23.13', 'aa.12.1.2', '12345678', '289043jdhjkbh']

    for one_str in ip_list:

        if judge_legal_ip(one_str):  # 正则方法

            # if judge_legal_ip2(one_str): #字符串方法

            print('{0} is a legal ip address!'.format(one_str))

        else:

            print('{0} is not a legal ip address!'.format(one_str))