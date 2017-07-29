#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################
# 介绍：插入排序
# 环境：Python 3.5.2
# 日期：2017-05-20
# 版本：v1.0
##############################

__author__ = 'Windrivder'

from random import randint


def insertion_sort(List):
    n = len(List)
    for i in range(1, n):
        if List[i] < List[i - 1]:
            temp = List[i]
            index = i
            for j in range(i - 1, -1, -1):
                if List[j] > temp:
                    List[j + 1] = List[j]
                    index = j
                else:
                    break
            List[index] = temp
    return List


def insertion_sort_bisect(List):
    n = len(List)
    for i in range(1, n):
        temp = List[i]
        for j in range(i + 1, -1, -1):
            if j > 0 and temp < List[j - 1]:
                List[j] = List[j - 1]
                List[j - 1] = temp
    return List


if __name__ == '__main__':
    sort_list = [randint(1, 99) for i in range(20)]
    print('排序前：{}'.format(sort_list))
    insertion_sort(sort_list)
    print('排序后：{}'.format(sort_list))
