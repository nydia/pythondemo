# -*- coding: utf-8 -*-
'''
Created on 2016年11月14日

@author: lvhq
'''

if __name__ == '__main__':
    
    '-------基本单位的练习----'
    '''
    a = input("x的值为：")
    b = input("y的值为：")
    c = a * b
    print("z值为："+str(c))
    
    '绝对值'
    d = abs(c)
    print("h的值为：" + str(d))
    
    print(pow(a, b))
    '''
    
#     numbers = [1,2,3,4,5,6,7,8,9,10]
#     temp = numbers[3:6:1]
    'print(temp)'
    
    
    'demo[2-3]'
    'Sentence : He\'s a very naught boy!'
    '''
    sentence = raw_input("Sentence:")
    screen_with = 80
    text_width = len(sentence)
    box_width = text_width + 6
    left_margin = (screen_with - box_width) // 2
    print
    print ' ' * left_margin+ '+' + '-' * (box_width - 2) + '+'
    print ' ' * (left_margin + 2) + '|' + ' ' * text_width      + '|'
    print ' ' * (left_margin + 2) + '|' +       sentence        + '|'
    print ' ' * (left_margin + 2) + '|' + ' ' * text_width      + '|'
    print ' ' * left_margin +  '+' + '-' * (box_width -2)  + '+'
    print
    '''
    
#     print(list('hello'))

#     name = list('Perl')
#     print(name)
    
#     name[2:] = list('ar')
#     print(name)

      
#     names = [101,5,90,6]
#     names.sort()
#     print(names)

#     x = [4,1,16,8,2]
#     y = x[:]
#     y.sort()
#     print(y)

    '元组'
#     print(3*(40+2,))

    
    
    
    
    
    
    
    
    
    