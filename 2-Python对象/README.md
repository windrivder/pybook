在 python 中，标识一个对象唯一身份的是：对象的`id`，对象类型和值。其中对象的`id`可以类比为 C 语言中的指针，在 Python 中没有指针，但是所有对象都可以看作指针。为什么要说这些呢？因为我们对 Python 对象进行操作时需要理解透这些才能免一些陷阱。

# 浅拷贝与深拷贝

**浅拷贝：**前面我们已经理解了，标识一个对象唯一身份的是对象的`id`，对象类型和值，那么什么是浅拷贝呢？浅拷贝就是创建一个相同类型和值但不同`id`的新对象，其中对象中的值是来自原对象的引用，所以浅拷贝产生的新对象中可变对象的值发生改变时**原对象的值也会随之改变**。

**工厂函数、切片操作、copy 模块中的 copy 操作**都是浅拷贝，浅拷贝典型的使用场景就是对象自身发生改变的同时需要保持对象中的值完全相同，如 List 排序：

```python
In [1]: import copy

In [2]: def sorted_list(olist, key=None):
   ...:     copied_list = copy.copy(olist)
   ...:     copied_list.sort(key=key)
   ...:     return copied_list
   ...:

In [3]: a = [3, 5, 2, 6, 1]

In [4]: b = sorted_list(a)

In [5]: b
Out[5]: [1, 2, 3, 5, 6]

In [6]: id(b) == id(a)
Out[6]: False
```

**深拷贝：**理解了浅拷贝，深拷贝就变得简单了。深拷贝就是完完全全地拷贝了一个对象，该对象的值不再是引用自原对象，而是新开辟的地址，所以我们对深拷贝创建的对象可以随意操作而不必担心原对象的改变。深拷贝需要依赖 copy 模块的 deepcopy 操作：

```python
In [1]: a = [1, 2]

In [2]: b = [a, a]

In [3]: b
Out[3]: [[1, 2], [1, 2]]

In [4]: from copy import deepcopy

In [5]: c = deepcopy(b)

In [6]: c[0].append(3)

In [7]: c
Out[7]: [[1, 2, 3], [1, 2, 3]]

In [8]: b
Out[8]: [[1, 2], [1, 2]]

In [9]: id(b[0]) == id(c[0])
Out[9]: False

In [10]: id(c[0]) == id(c[1])
Out[10]: True
```

同时，我们在定义类时可以定义`__copy__`和`__deepcopy__`来定制 copy 的行为：

```python
In [1]: class CopyObj(object):
   ...:     def __repr__(self):
   ...:         return 'Hello'
   ...:     def __copy__(self):
   ...:         return 'World'
   ...:

In [2]: obj = CopyObj()

In [3]: print(obj)
Hello

In [4]: import copy

In [5]: copyobj = copy.copy(obj)

In [6]: print(copyobj)
World
```

**判断对象类型：**

```python
In [1]: num = 123

In [2]: if type(num) is int:
   ...:     print('num is Integer')
   ...: else:
   ...:     print('num is not Integer')
   ...:
num is Integer

In [3]: if isinstance(num, int):    # 推荐
   ...:     print('num is Integer')
   ...: else:
   ...:     pass
   ...:
num is Integer
```

下面我们来简单学习一些 Python 对象。

# Bool 与 None

调用`bool()`可以检查变量的真假值`True`或`False`。

`if`语句通过判断布尔类型来控制程序的执行路径，同时在 Python 中数据有隐式的真假值，可以使代码变得简短有效，如下：

 类型  | False             | True
:--: | :---------------- | :---------------------------------
 布尔  | False （与0等价）      | True （与1等价）
字符串  | ""（空字符串）          | 非空字符串，例如 " ", "blog"
 数值  | 0, 0.0            | 非0的数值，例如：1, 0.1, -1, 2
 容器  | [], (), {}, set() | 至少有一个元素的容器对象，例如：[0], (None,), ['']
None | None              | 非None对象

```python
In [1]: id(None)
Out[1]: 10743840

In [2]: a = None

In [3]: id(a)
Out[3]: 10743840

In [4]: L = []

In [5]: if L is not None:
   ...:     print('L is {}'.format(L))
   ...: else:
   ...:     print('L is empty')
   ...:
L is []

In [6]: if L:    #3 正确的判断形式
   ...:     print('Do something...')
   ...: else:
   ...:     print('Do other thing...')
   ...:
Do other thing...
```

`#3`执行中会调用`__nonzero__()`来判断自身对象是否为空并返回`0/1`或`True/False`，如果没有定义该方法，Python 将调用`__len__()`进行判断，返回`0`表示为空。如果一个类既没有定义`__len__()`又没有定义`__nonzero__()`，该类实例用 if 判断为`True`。

# 数据类型转换

函数         | 描述
---------- | ----------------
`int(x)`   | 将 x 转换为整数
`float(x)` | 将 x 转换为浮点数
`str(x)`   | 将 x 转换为字符串
`hex(x)`   | 将整数 x 转换为十六进制字符串
`oct(x)`   | 将整数 x 转换为八进制字符串
`bin(x)`   | 将整数 x 转换为二进制字符串
`chr(x)`   | 将整数 x 转换为字符
`ord(x)`   | 将字符 x 转换为整数

同时，`list()`、`tuple()`、`dict()`和`set()`可以进行列表、元组、字典和集合转换。

# 自定义数据类型

Python 允许通过继承去自定义数据类型，很多第三方库或框架有类似的应用，这里简单实现了一个：

```python
class CustomDict(dict):
    '''Simple dict but support access as x.y style.'''

    def __init__(self, names=(), values=(), **kw):
        super(CustomDict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(
                r"'CustomDict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
```

> 待补充
