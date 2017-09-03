> 整理常见排序算法，并用 Python 简单实现，默认将从小到大排序。
>
> 网上已经有很多的整理了，站在前辈的肩膀上，收获颇丰，望斧正！

| 排序方法 | 最坏时间复杂度    | 最优时间复杂度    | 平均时间复杂度          | 辅助空间           | 稳定性  |
| ---- | ---------- | ---------- | ---------------- | -------------- | ---- |
| 冒泡排序 | `O(n2)`    | `O(n)`     | `O(n2)`          | `O(1)`         | 稳定   |
| 选择排序 | `O(n2)`    | `O(n2)`    | `O(n2)`          | `O(1)`         | 不稳定  |
| 插入排序 | `O(n2)`    | `O(n)`     | `O(n2)`          | `O(1)`         | 稳定   |
| 快速排序 | `O(n2)`    | `O(nlogn)` | `O(nlogn)`       | `O(logn)~O(n)` | 不稳定  |
| 堆排序  | `O(nlogn)` | `O(nlogn)` | `O(nlogn)`       | `O(1)`         | 不稳定  |
| 希尔排序 | `O(n2)`    | `O(n1.3)`  | `O(nlogn)~O(n2)` | `O(1)`         | 不稳定  |
| 归并排序 | `O(nlogn)` | `O(nlogn)` | `O(nlogn)`       | `O(n)`         | 稳定   |

先谈谈排序的稳定性：

> 假设`ki=kj(i<=i<=n, 1<=j<=n, i!=j)`，且在排序前的序列中`ri`领先于`rj` (i<j)。如果排序后`ri`仍领先于`rj`，则称排序的方法是稳定的；反之，若可能使得排序后的序列中`rj`领先`ri`，则称所用的排序方法是不稳定的。

![排序](http://onu4svjbw.bkt.clouddn.com/17-5-21/52381893-file_1495359671102_a583.png)

# 冒泡排序 Bubble Sort 

## 原理介绍

**冒泡排序**是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢「浮」到数列的顶端。

冒泡排序演算法的运作如下：

1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

动画演示：

![Bubble_sort_animation](http://onu4svjbw.bkt.clouddn.com/17-5-21/75694908-file_1495349277684_166e6.gif)

## 代码实现

```python
In [1]: from random import randint

In [2]: def bubble_sort(List):
   ...:     n = len(List)
   ...:     for i in range(n):
   ...:         for j in range(1, n-i):
   ...:             if List[j-1] > List[j]:
   ...:                 List[j-1], List[j] = List[j], List[j-1]
   ...:     return List
   ...: 

In [3]: %timeit(bubble_sort([randint(1, 99) for i in range(20)]))
10000 loops, best of 3: 74 µs per loop
```

下面是改进后的冒泡排序，改进了两处，一是在某一趟遍历排序中，如果没有发生数据交换，则证明已经排序完成，这时就可以跳出遍历，我们用`flag`标记这个状态；二是在某一趟遍历排序中，如果最后发生了数据交换，那么这个位置之后的数据就应该是有序的了，我们将这个位置`p`标记为下次遍历的临界值。代码如下：

```python
In [4]: def bubble_sort_flag(List):
   ...:     p = n = len(List)
   ...:     for i in range(n):
   ...:         flag = True
   ...:         for j in range(1, p):   # 遍历到最后发生数据交换的位置
   ...:             if  List[j-1] > List[j]:
   ...:                 List[j-1], List[j] = List[j], List[j-1]
   ...:                 p = j   # 记录最后发生数据交换的位置
   ...:                 flag = False
   ...:         if flag:
   ...:             break
   ...:     return List
   ...: 

In [5]: %timeit(bubble_sort_flag([randint(1, 99) for i in range(20)]))
10000 loops, best of 3: 70.2 µs per loop
```

# 选择排序 Selection Sort

## 原理介绍

**选择排序**的主要优点与**数据移动**有关。如果某个元素位于正确的最终位置上，则它不会被移动。选择排序每次交换一对元素，它们当中**至少有一个将被移到其最终位置上**，因此对n个元素的表进行排序总共进行至多n-1次交换。在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种。

选择排序演算法的运作如下：

1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
2. 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3. 以此类推，直到所有元素均排序完毕。

动画演示：

![Selection_sort_animation](http://onu4svjbw.bkt.clouddn.com/17-5-21/43094580-file_1495349277834_f7e1.gif)

## 代码实现

```python
In [1]: from random import randint
   ...: 
   ...: def selection_sort(List):
   ...:     n = len(List)
   ...:     for i in range(n):
   ...:         min_index = i
   ...:         for j in range(i+1, n):
   ...:             if List[j] < List[min_index]:
   ...:                 min_index = j
   ...:         List[min_index], List[i] = List[i], List[min_index]
   ...:     return List
   ...: 

In [2]: %timeit(selection_sort([randint(1, 99) for i in range(20)]))
10000 loops, best of 3: 54.2 µs per loop
```

# 插入排序 Insertion Sort

## 原理介绍

**插入排序**在实现上，通常采用`in-place`排序（即只需用到`O(1)`的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

插入排序演算法的运作如下：

1. 从第一个元素开始，该元素可以认为已经被排序
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5. 将新元素插入到该位置后
6. 重复步骤2~5

动画演示：

![Insertion_sort_animation](http://onu4svjbw.bkt.clouddn.com/17-5-21/6408435-file_1495349277950_736.gif)

## 代码实现

```python
In [1]: from random import randint
   ...: 
   ...: def insertion_sort(List):
   ...:     n = len(List)
   ...:     for i in range(1, n):
   ...:         if List[i] < List[i-1]:
   ...:             temp = List[i]
   ...:             index = i
   ...:             for j in range(i-1, -1, -1):
   ...:                 if List[j] > temp:
   ...:                     List[j+1] = List[j]
   ...:                     index = j
   ...:                 else:
   ...:                     break
   ...:             List[index] = temp
   ...:     return List
   ...: 

In [2]: %timeit(insertion_sort([randint(1, 99) for i in range(20)]))
10000 loops, best of 3: 51.8 µs per loop
```

如果比较操作的代价比交换操作大的话，可以采用二分查找法来减少比较操作的数目。该算法可以认为是插入排序的一个变种，称为**二分查找插入排序**

```python
In [3]: def insertion_sort_bisect(List):  
   ...:     n = len(List)  
   ...:     for i in range(1, n):  
   ...:         temp = List[i]  
   ...:         for j in range(i+1, -1, -1):  
   ...:             if j>0 and temp < List[j-1]:  
   ...:                 List[j] = List[j-1]  
   ...:                 List[j-1] = temp  
   ...:     return List
   ...: 

In [4]: %timeit(insertion_sort_bisect([randint(1, 99) for i in range(20)]))
10000 loops, best of 3: 73.2 µs per loop
```

# 快速排序 Quick Sort

## 原理介绍

**快速排序** ，又称**划分交换排序**（partition-exchange sort），在平均状况下，排序n个项目要`Ο(n log n)`次比较。在最坏状况下则需要`Ο(n2)`次比较，但这种状况并不常见。事实上，快速排序通常明显比其他`Ο(n log n)`算法更快，因为它的内部循环（inner loop）可以在大部分的架构上很有效率地被实现出来。

快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。

快速排序演算法的运作如下：

1. 从数列中挑出一个元素，称为"基准"（pivot）
2. 重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为**分区（partition）**操作
3. 递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。

动画演示：

![Sorting_quicksort_anim](http://onu4svjbw.bkt.clouddn.com/17-5-21/38452746-file_1495351976539_16348.gif)

## 代码实现

```python
In [1]: from random import randint
   ...: 
   ...: def quick_sort(List):
   ...:     less = []
   ...:     greater = []
   ...:     if len(List) <= 1:
   ...:         return List
   ...:     pivot =List.pop()
   ...:     for x in List:
   ...:         if x <= pivot:
   ...:             less.append(x)
   ...:         else:
   ...:             greater.append(x)
   ...:     return quick_sort(less) + [pivot] + quick_sort(greater)
   ...: 

In [2]: %timeit(quick_sort([randint(1, 99) for i in range(20)]))
10000 loops, best of 3: 49 µs per loop
```

# 堆排序 Heap Sort 

## 原理介绍

**堆排序**是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

**堆节点的访问：**

通常堆是通过一维数组来实现的。在数组起始位置为0的情形中：

- 父节点 i 的左子节点在位置`(2*i+1)`
- 父节点 i 的右子节点在位置`(2*i+2)`
- 子节点 i 的父节点在位置`floor((i-1)/2)`

**堆的操作：**

在堆的数据结构中，堆中的最大值总是位于根节点(在优先队列中使用堆的话堆中的最小值位于根节点)。堆中定义以下几种操作：

- 最大堆调整（Max_Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
- 创建最大堆（Build_Max_Heap）：将堆所有数据重新排序
- 堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算

## 代码实现



# 希尔排序

## 原理介绍



## 代码实现



# 归并排序

## 原理介绍



## 代码实现



# 参考资料

- 本文原理介绍部分均选自维基百科：[冒泡排序](https://zh.wikipedia.org/wiki/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F) 、[选择排序](https://zh.wikipedia.org/wiki/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F) 、[插入排序](https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F) 、[快速排序](https://zh.wikipedia.org/wiki/快速排序) 、[堆排序](https://zh.wikipedia.org/wiki/堆排序) 、[希尔排序](https://zh.wikipedia.org/wiki/希尔排序) 、[归并排序](https://zh.wikipedia.org/wiki/归并排序)
- [白话经典算法之七大排序总结篇](http://blog.csdn.net/morewindows/article/details/7961256)
- [排序算法（Python版）](http://www.ttwshell.com/article/Sorting-Algorithm-Python-Code.html)
- [基本排序算法的Python实现](https://zhuanlan.zhihu.com/p/21839027)