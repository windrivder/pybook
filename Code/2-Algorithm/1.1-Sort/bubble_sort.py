#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################
# 介绍：冒泡排序
# 环境：Python 3.5.2
# 日期：2017-05-20
# 版本：v1.0
##############################

__author__ = 'Windrivder'

from random import randint


def bubble_sort(List):
    n = len(List)
    for i in range(n):
        for j in range(1, n - i):
            if List[j - 1] > List[j]:
                List[j - 1], List[j] = List[j], List[j - 1]
    return List


def bubble_sort_back(List):
    n = len(List)
    for i in range(n):
        flag = True
        for j in range(n - 2, -1, -1):
            if List[j] > List[j + 1]:
                List[j + 1], List[j] = List[j], List[j + 1]
                flag = False
        if flag:
            break
    return List


def bubble_sort_flag(List):
    p = n = len(List)
    for i in range(n):
        flag = True
        for j in range(1, p):   # 遍历到最后发生数据交换的位置
            if List[j - 1] > List[j]:
                List[j - 1], List[j] = List[j], List[j - 1]
                p = j   # 记录最后发生数据交换的位置
                flag = False
        if flag:
            break
    return List


if __name__ == '__main__':
    sort_list = [randint(1, 99) for i in range(20)]
    print('排序前：{}'.format(sort_list))
    bubble_sort_back(sort_list)
    print('排序后：{}'.format(sort_list))
