在 Python 中一切皆对象，所以 Python 中的函数也是**类对象**。

下面是函数的一些属性：

```python
In [1]: def foo():
   ...:     print('Hello World')
   ...:

In [2]: foo
Out[2]: <function __main__.foo>

In [3]: dir(foo)
Out[3]:
['__annotations__',
 '__call__',
 '__class__',
 '__closure__',
 '__code__',
 '__defaults__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__get__',
 '__getattribute__',
 '__globals__',
 '__gt__',
 '__hash__',
 '__init__',
 '__kwdefaults__',
 '__le__',
 '__lt__',
 '__module__',
 '__name__',
 '__ne__',
 '__new__',
 '__qualname__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__']
```

有一些比较重要的属性我们可以通过一些示例来理解：

`__call__`：

```python
# 所有的函数都是可调用对象，我们定义类实现 __call__() 就可以将类作为可调用对象进行调用
# 进一步模糊了类对象与函数之间的关系
In [1]: class Fib(object):
   ...:     def __init__(self):
   ...:         pass
   ...:     def __call__(self, num):
   ...:         a, b = 0, 1
   ...:         self.L = []
   ...:         for i in range(num):
   ...:             self.L.append(a)
   ...:             a, b = b, a + b
   ...:         return self.L
   ...:

In [2]: f = Fib()

In [3]: f(10)
Out[3]: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

`__doc__`, `__name-_`, `__module__`：

```python
In [1]: def foo():
   ...:     """print hello world"""
   ...:     print('Hello World')
   ...:

In [2]: foo.__doc__
Out[2]: 'print hello world'

In [3]: foo.__name__
Out[3]: 'foo'

In [4]: foo.__module__
Out[4]: '__main__'
```

> 待补充
