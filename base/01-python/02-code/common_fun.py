#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# datetime： 2021/5/30 11:49 
# devteam： team
# author： xk
# email： lliu606@hotmail.com
# file： fun.py
# ide： PyCharm

def multiply_list(lst, n):
    '''
    列表里所有数字修改成原来的n倍
    '''
    if not lst:
        return None

    for idx, item in enumerate(lst):
        if isinstance(item, bool):
            continue
        if isinstance(item, list):
            multiply_list(item, n)
        if isinstance(item, (int, float)):
            lst[idx] = item * n


str_int_dic = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
}


def str_int(string):
    '''
    将字符串string转成整型int
    简单版
    '''
    ret = 0
    for item in string:
        int_val = str_int_dic[item]
        ret = ret * 10 + int_val

    return ret


def str_float(string):
    '''
    string转float
    '''
    str_arr = string.split('.')
    int_val = str_int(str_arr[0])
    float_val = str_int(str_arr[1])
    while float_val > 1:
        float_val = float_val * 0.1

    return int_val + float_val


def bubble_sort(lst):
    '''
    冒泡排序
    '''
    for i in range(len(lst) - 1, 1, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def quick_sort(lst):
    '''
    快速排序
    递归
    '''
    if len(lst) < 1:
        return lst

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    mid = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)


def yh_triangle(n):
    '''
    打印杨辉三角的前n行
    '''
    arr_list = [[0] * (2 * n + 1) for i in range(n)]
    for i in range(len(arr_list)):
        rows = arr_list[i]
        for j in range(len(rows)):
            if i == 0 and j == n:
                rows[j] = 1
            if i > 0 and 0 < j < 2 * n:
                arr_list[i][j] = arr_list[i - 1][j - 1] + arr_list[i - 1][j + 1]

            col = rows[j]
            temp = '' if col == 0 else col
            print(temp, end=' ')
            if j == len(rows) - 1:
                print()


def is_square(n):
    '''
    打印n内的完全平方数，逆向思维和简洁代码
    '''
    i = 1
    val = 1
    while val < n:
        val = i ** 2
        print(i, val)
        i = i + 1


def remove_duplicate(lst):
    '''
    flatten_list 扁平list,有序序列删除重复项
    nested_list 嵌套list,删除重复项
    '''
    if not lst and not isinstance(lst, list):
        return None

    is_flatten_list = not any(isinstance(item, list) for item in lst)
    if is_flatten_list:
        # 有序序列删除重复项，返回哨兵位，原list改变
        # 除了此方案采用哨兵占位，还可采用双list,set
        idx = 0
        for i in range(1, len(lst)):
            if lst[idx] != lst[i]:
                lst[idx + 1] = lst[i]
                idx = idx + 1

        return idx + 1

    nested_set = set()
    for item in lst:
        item.sort()
        nested_set.add(tuple(item))

    return nested_set


def combination_lst(lst, target):
    '''
    可能的序列，再经过remove去重
    序列中的元素和和目标值相等
    动态规划
    :param lst: flatten list, int
    :param target: value, int
    :return: 返回所有可能的序列
    '''
    ret_list = []
    for item in lst:
        if item == target:
            ret_list.append([item])
        elif item > target:
            continue
        else:
            other = target - item
            other_lst = combination_lst(lst, other)
            for temp_lst in other_lst:
                # 间接改变 other_lst
                temp_lst.append(item)
            ret_list.extend(other_lst)

    return ret_list


def sub_max_sum(lst):
    '''
    寻找连续子序列的最大和
    动态规划
    '''
    max_sum = lst[0]
    # pre_sum是动态的,最初等于列表的第一个元素
    pre_sum = lst[0]
    for i in range(1, len(lst)):
        # 前面的累积和如果小于0,当前值item加上一个负数只会比item更小
        # 因此将item赋值给pre_sum
        if pre_sum < 0:
            pre_sum = lst[i]
        else:
            # 前面的累积和是整数或者0,继续累加
            pre_sum = pre_sum + lst[i]

        # max_sum同步更新
        if pre_sum > max_sum:
            max_sum = pre_sum

    return max_sum


def check_inclusion(s1, s2):
    '''
    字符串s1, s2 判断s1的排列之一是否是s2的字串
    输入：abcb sdbacbsde
    输出：True
    1. 暴力解法，找出s1所有可能的排列，然后再s2中find
    2. 优化解法，把s1的信息存于dict中，s2符合条件的字串存于dict，比较dict
    '''
    if not s1 or not s2:
        return None

    s1_dic, s2_dic = {}, {}
    for c in s1:
        s1_dic.setdefault(c, 0)
        s1_dic[c] = s1_dic[c] + 1

    s1_len, s2_len = len(s1), len(s2)
    for i, c in enumerate(s2):
        s2_dic.setdefault(c, 0)
        s2_dic[c] = s2_dic[c] + 1

        idx = 1
        while idx < s1_len and (i + idx) < s2_len:
            temp = s2[i + idx]
            s2_dic.setdefault(temp, 0)
            s2_dic[temp] = s2_dic[temp] + 1
            idx = idx + 1

        if s1_dic == s2_dic:
            return True
        else:
            s2_dic.clear()

    return False
