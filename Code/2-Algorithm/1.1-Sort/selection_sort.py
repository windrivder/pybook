#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################
# 介绍：选择排序
# 环境：Python 3.5.2
# 日期：2017-05-20
# 版本：v1.0
##############################

__author__ = 'Windrivder'

from random import randint


def selection_sort(List):
    n = len(List)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if List[j] < List[min_index]:
                min_index = j
        List[min_index], List[i] = List[i], List[min_index]
    return List


if __name__ == '__main__':
    sort_list = [randint(1, 99) for i in range(20)]
    print('排序前：{}'.format(sort_list))
    selection_sort(sort_list)
    print('排序后：{}'.format(sort_list))
