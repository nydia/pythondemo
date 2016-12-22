# -*- coding:utf-8 -*-
'''
Created on 2016年12月8日

@author: lvhq
'''

if __name__ == '__main__':
    #简单数据库
    #使用人名作为键的字典，每个人用另一个字典表示，其键‘phone’ 和 ‘addr’ 分别表示他们的电话号码和地址
    people = {
        'Alice' :{
            'phone' : '2341',
            'addr' : 'Foo drive 23'
        },
        'Beth' : {
            'phone' : '9102',
            'addr' : 'Bar street 42'
        },
        'Cecil' :{
            'phone' : '3158',
            'addr' : 'Baz avence 90'
        }
    }
    
    #针对电话号码和地址使用的描述性标签，会在打印输出的时候用到
    labels = {
        'phone' : 'phone number',
        'addr' : 'address'
    }
    
    name = raw_input('Name : ')
    
    #查找电话号码还是地址？
    request = raw_input('Phone number (p) address (a)? ')
    
    #使用正确的键
    if request == 'p' : key = 'phone'
    if request == 'a' : key = 'addr'
    
    # 如果名字是字典中的有效键才打印信息
    if name in people : print "%s's %s is %s." % \
       (name, labels[key], people[name][key])