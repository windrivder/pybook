#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################
# 介绍：快速排序
# 环境：Python 3.5.2
# 日期：2017-05-21
# 版本：v1.0
##############################

__author__ = 'Windrivder'

from random import randint

def quick_sort(List):
    less = []
    greater = []
    if len(List) <= 1:
        return List
    pivot =List.pop()
    for x in List:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    return quick_sort(less) + [pivot] + quick_sort(greater)


# 出自《Python cookbook》的 Python 快速排序
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + \
               [pivot] + \
               qsort([x for x in arr[1:] if x >= pivot])


# 以及一行代码的实现
qs = lambda xs : ( (len(xs) <= 1 and [xs]) or [ qs( [x for x in xs[1:] if x < xs[0]] ) + [xs[0]] + qs( [x for x in xs[1:] if x >= xs[0]] ) ] )[0]


if __name__ == '__main__':
    sort_list = [randint(1, 99) for i in range(20)]
    print('排序前：{}'.format(sort_list))
    sorted_list = quick_sort(sort_list)
    print('排序后：{}'.format(sorted_list))
