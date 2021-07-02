''' base data type
print(0.3 == 3 * 0.1) # false 计算采用浮点数近似, 0.1+0.2=0.30000...004
int("3.42") # error
"4.0" == 4 # false
bool("0") # true
bool("") # false tip: 0 , 空字符串, None在条件判断语句中等价于False, 其他数值都等价于True
'''

''' str
print('abcd'.index('D')) # error
print('abcd'.find('D')) # -1
print('{name}喜欢{fruit}'.format(name='李雷',fruit='苹果'))
s1.replace('Python', 'python') # 请将字符串里的Python替换成 python,并输出替换后的结果
print('this is a book'.startswith('this')) # endswith
print('python is'[2:20]) # thon is 切片，超出范围无异常
re.split('[时分秒]', s1) # split 默认空格、分行
'''

''' list tuple # 查找地址id(), 是否产生新对象
print([1,2,3] * 2) # [1, 2, 3, 1, 2, 3]
[1,2,3].insert(0,10) # 返回None, insert
[1,2,3] + [4], [1,2,3].append(4) # list 末尾新增元素
lst = [1, [2, 3]], lst[1][0] *= n # list 数字翻n倍
lst.count(max(lst))
lst[::-1] # 翻转 [start:end:step]

a = 1,2,3,'4' # 默认为元组
print((1,) * 2) # (1,1)
print((1) * 2) # 2 括号可理解为优先级,非元组
tuple 元素不能增删改, del tup 
'''

''' dict
dic['key'] = 'value' # 增加key-value对
dic.update(dic1) # 更新
dic.setdefault(item, 0)
'''
