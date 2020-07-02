# coding=utf-8
from array import array
import math
import numbers
from functools import singledispatch

# 重载
@singledispatch
def func(a):
    print(type(a))
    
@func.register(int)
def _numeric(a:int):
    print(a)
    
@func.register(list)
def _array(a):
    [print(i) for i in a]

# vector2d
class Vector2d:
    
    def __init__(self):
        self._x = None
        self._y = None
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, v):
        self._x = v

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, v):
        self._y = v
    
    @classmethod
    def createVector2d(cls, x, y):
        instance = cls()
        instance.x = x
        instance.y = y
        return instance
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
        
    def __repr__(self):
        return "({0:f},{1:f})".format(self._x, self._y)
    
    def __str__(self):
        return "({0:f},{1:f})".format(self._x, self._y)
    
    def __eq__(self, value):
        return tuple(self) == tuple(value)
        # return self._x == value.x and self._y == value.y
    
    def __abs__(self):
        return math.sqrt(sum(x**2 for x in self))
    

class Vector_v2():
    typecode = 'd'
    
    def __init__(self, componets):
        self._componets = array(self.typecode, componets)
        
    def __iter__(self):
        return (i for i in self._componets)
    
    def __repr__(self):
        return "".join([str(x) for x in self._componets])
    
    # 可切片:
    def __len__(self):
        return len(self._componets)
    
    def __getitem__(self, index):
        # 只能返回数组
        # return self._componets[index]
        
        # 使用 slice 返回同类型
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._componets[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indeces must be integers'
            raise TypeError(msg.format(cls=cls))
        
    # 动态存取属性： 还是用 @property 舒服
    # 属性查找顺序 my_obj.x: 检查实例名为x的属性-> 类my_obj.__class__中查找->顺着继承树查找->调用my_obj类中的__getattr__方法，传入self的x
    
    attr_names = 'xyz'
    
    def __getattr__(self, name):
        cls = type(self)
        if len(name)==1:
            pos = cls.attr_names.find(name)
            if 0<= pos < len(self._componets):
                return self._componets[pos]
        
        msg = '{.__name__!r} object has no attr {!r}'
        raise AttributeError(msg.format(cls, name))    
    
    # 必须配套 setattr， 否则赋值时会创建一个 my_obj.x, 但 my-obj._componets不变
    def __setattr__(self, name, value):
        cls = type(self)
        if len(name)==1:
            if name in cls.attr_names:
                error = 'read only attr {attr_name!r}'
            else:
                error = ' '
            if error:
                msg = error.format(attr_name=name)
                raise AttributeError(msg)
        return super().__setattr__(name, value)
    
    def __eq__(self, other):
        return len(self)==len(other) and all(a==b for a,b in zip(self, other))

v = Vector_v2(range(5))
print(v, v[2:5])
print(v.x)
print(v.d)
