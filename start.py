#!/usr/bin/env python3

import configparser
import json
#import urllib.request as urllib2
import urllib.request

import config_check

load_code = config_check.check_dics
print('配置1列表：' + str(load_code))
for one in load_code:
    print('配置1详情：' + str(one))

#载入配置文件
load_config = configparser.ConfigParser()

#如果配置文件不存在，则新建
load_config.read("config_api.py")

#读取配置
#java_service_comm = load_config.get('java_service', 'zluser')

#获取所有sections
all_sections = load_config.sections()
print('sections列表：' + str(all_sections))

#获取sections中的options键值
for sections_alone in all_sections:
    print('当前options:' + sections_alone)

    '''
        if sections_alone == 'status':
            check_list = 'status'
        elif sections_alone == 'diskSpace':
            check_list = ''
        elif sections_alone == 'redis':
    
        elif sections_alone == 'db':
    '''

    #获取键值
    sections_comm = load_config.items(sections_alone)
    print('对应列表：' + str(sections_comm))

    #获取内容
    for options_alone in sections_comm:
        print('对应内容：' + str(options_alone))

        #获取键值
        project_name = options_alone[0]
        project_value = options_alone[1]
        print('分区：' + sections_alone + "|| 项目：" + project_name + '|| 值：' + project_value)

        #检测API
        open_html = urllib.request.urlopen(project_value)
        print('##############' + str(open_html))
        html_read = open_html.read().decode('utf-8')
        html_json = json.loads(html_read)
        print(html_json['status'])

        #验证返回的json
        for check_json in load_code:
            print('配置1键值对：' + str(check_json))

            #拆分键值对
            for k, v in check_json.items():
                print('打印键值对：' + str(k) + '::' + str(v))
                if v.isdigit():
                    '''决断数字大小'''
                    checkout_v = html_json[k]
                    if
                else:
                    '''判断字符串是否相同'''


                checkout_v = html_json[k]
                if checkout_v == str(v):
                    print('键值：' + str(k) + '返回正常' + str(checkout_v))

        #project_value = load_config.get(sections_alone, sections_comm)


        #内容检测
