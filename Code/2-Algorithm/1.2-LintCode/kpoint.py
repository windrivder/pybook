#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Windrivder'


# Given some points and a point origin in two dimensional space, find k points out of the some points which are nearest to origin.
# Return these points sorted by distance, if they are same with distance, sorted by x-axis, otherwise sorted by y-axis.
# input: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
# output: [[1,1],[2,5],[4,4]]

from math import sqrt
from operator import itemgetter


k = 51
origin = [1, 90]
points = [[40,-23],[9,138],[429,115],[50,-17],[-3,80],[-10,33],[5,-21],[-3,80],[-6,-65],[-18,26],[-6,-65],[5,72],[0,77],[-9,86],[10,-2],[-8,85],[21,130],[18,-6],[-18,26],[-1,-15],[10,-2],[8,69],[-4,63],[0,3],[-4,40],[-7,84],[-8,7],[30,154],[16,-5],[6,90],[18,-6],[5,77],[-4,77],[7,-13],[-1,-45],[16,-5],[-9,86],[-16,11],[-7,84],[1,76],[3,77],[10,67],[1,-37],[-10,-81],[4,-11],[-20,13],[-10,77],[6,-17],[-27,2],[-10,-81],[10,-1],[-9,1],[-8,43],[2,2],[2,-21],[3,82],[8,-1],[10,-1],[-9,1],[-12,42],[16,-5],[-5,-61],[20,-7],[9,-35],[10,6],[12,106],[5,-21],[-5,82],[6,71],[-15,34],[-10,87],[-14,-12],[12,106],[-5,82],[-46,-45],[-4,63],[16,-5],[4,1],[-3,-53],[0,-17],[9,98],[-18,26],[-9,86],[2,77],[-2,-49],[1,76],[-3,-38],[-8,7],[-17,-37],[5,72],[10,-37],[-4,-57],[-3,-53],[3,74],[-3,-11],[-8,7],[1,88],[-12,42],[1,-37],[2,77],[-6,77],[5,72],[-4,-57],[-18,-33],[-12,42],[-9,86],[2,77],[-8,77],[-3,77],[9,-42],[16,41],[-29,-37],[0,-41],[-21,18],[-27,-34],[0,77],[3,74],[-7,-69],[-21,18],[27,146],[-20,13],[21,130],[-6,-65],[14,-4],[0,3],[9,-5],[6,-29],[-2,73],[-1,-15],[1,76],[-4,77],[6,-29]]


def kclosest(points, origin, k):
    kclosest_list = []
    dis_list = [sqrt(pow((point[0] - origin[0]), 2) +
                     pow((point[1] - origin[1]), 2)) for point in points]
    dis_list = [(i, dis) for i, dis in zip(range(len(dis_list)), dis_list)]
    dis_list.sort(key=lambda d: d[1])
    kclosest_list = [points[dis_list[i][0]] for i in range(k)]
    kclosest_list.sort(key=itemgetter(0,1))
    return kclosest_list


if __name__ == '__main__':
    print(kclosest(points, origin, k))
