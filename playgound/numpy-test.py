# coding=utf-8
import os
import numpy as np
import cv2


def base_info():
    # 版本信息
    print(np.__version__)
    np.show_config()

    # 帮助文档查询
    help(np.random)

    # API 查询
    np.info(np.shape)

    # 命令行查询函数API
    print('python -c "import numpy;numpy.info(numpy.add)"')


def create_vector():
    # 创建vector
    zeros = np.zeros(10)
    ones = np.ones(10)
    np.empty(10, dtype = float, order = 'C')

    # list <--> np.arrary
    l = [1,2,3,4]
    z = np.asanyarray(l, dtype=np.int8)

    # from buffer
    s = b'hello world'
    a = np.frombuffer(s, dtype=np.str)
    print(a)


    # reverse a vector
    ones = ones[::-1]

    # Create a 3x3 matrix with values ranging from 0 to 8
    z = np.arange(9).reshape(3, 3)

    # Find indices of non-zero elements from [1,2,0,0,4,0]
    nz = np.nonzero(z)

    # Create a 3x3 identity matrix
    z = np.eye(3)

    # Create a 3x3x3 array with random values
    z = np.random.random((3, 3, 3))

    # Create a 10x10 array with random values and find the minimum and maximum values
    z = np.random.random((10, 10))
    zmin, zmax = z.min(), z.max()

    # Create a random vector of size 30 and find the mean value
    z = np.random.random(30)
    zmean = z.mean()

    # 20.Normalize a 5x5 random matrix
    z = np.random.random((5, 5))
    zmin, zmax = z.min, z.max()
    print((z-zmin)/(zmax-zmin))

    # Create a 2d array with 1 on the border and 0 inside
    z = np.ones((5, 5))
    z[1:-1, 1:-1] = 0

    # Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
    z = np.diag(1+np.arange(4), k=-1)

    # 17.Create a 8x8 matrix and fill it with a checkerboard pattern
    z = np.zeros((8,8), dtype=int)
    z[1::2, ::2] = 1 # a[1::2] 从第1个开始，每隔1个数取值
    z[::2, 1::2] = 1
    print(z)

    # 18.Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?。
    # np数组维度从外至内
    # 例如 （2,2,2）的数组 np.array([[[0, 1],[2, 3]],[[4, 5],[6, 7]]])
    # print(np.unravel_index(1, (2,2,2))) >>> (0,0,1)
    # print(np.unravel_index(2, (2,2,2))) >>> (0,1,0)
    # print(np.unravel_index(7, (2,2,2))) >>> (1,1,1)
    print(np.unravel_index(100, (6,7,8)))

    # 19.Create a checkerboard 8x6 matrix using the tile function
    z = np.tile(np.array([[0,1],[1,0]]), (4,3))

    # 21.Create a custom dtype that describes a color as four unisgned bytes (RGBA)
    color = np.dtype([("r", np.ubyte, 1),
                      ("g", np.ubyte, 1),
                      ("b", np.ubyte, 1),
                      ("a", np.ubyte, 1)])
    z = np.array([bytes('1', encoding='utf-8'), b's'], dtype=color)
    print(z)

    # 31.Create a vector of size 10 with values ranging from 0 to 1, both excluded
    z = np.linspace(0,1,12,endpoint=True)[1,-1]



def operations():
    # 22.Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
    # 矩阵乘法
    print(np.dot(np.ones((5, 3)), np.ones((3, 2))))
    # 点乘
    print(np.ones((3, 2)) * np.ones((3, 2)))

    # 23.Given a 1D array, negate all elements which are between 3 and 8, in place
    z = np.arange(11)
    z[(3<z) & (z<8)] *= -1

    # 27.How to round away from zero a float array
    # 远离zero取近似
    # np.copysign(a,b) 将a的符号变成b一样
    # np.trunc 向zero取近似int
    # np.around  np.round 四舍五入
    Z = np.random.uniform(-10,+10,10)
    print (np.trunc(Z + np.copysign(0.5, Z)))

    # 28.Extract the integer part of a random array using 5 different methods
    z = np.random.uniform(0, 10, 10)
    print(z-z%1)
    print(np.floor(z))
    print(np.ceil(z)-1)
    print(np.around(z-0.5))
    print(np.round(z-0.5))
    print(z.astype(int))
    print(np.trunc(z))

    # 29.Create a 5x5 matrix with row values ranging from 0 to 4
    z = np.zeros((5,5))
    print(z+np.arange(5))

    # 33. how to sum a small array faster than np.sum
    # 对数组用一种函数操作对每个元素迭代，可以计算累加/累乘等
    z=np.random.random(10)
    np.add.reduce(z)

    # 34. check two random array if they are equal
    # np.equal(a,b, relative thresh, absolute thresh)
    a = np.random.random((2,3))
    b = np.random.random((2,3))
    print(a==b)
    equal = np.allclose(a, b)
    print(equal)

    # 35.make a array immutable(read-only)
    z=np.zeros(10)
    z.flags.writeable=False
    z[0]=1

    # 


# 30. consider a generator function that generates 10 integers and use it to build an array
def generate():
    for x in range(10):
        yield x
        print(x)

z=np.fromiter(generate(), dtype=np.float, count=-1)
print(z)


def what_is_the_output():
    # nan  inf  float
    print(0*np.nan) # nan
    print(np.nan == np.nan) # False
    print(np.inf > np.nan) # False
    print(0.3 == 3 * 0.1) # False: never use '==' between 2 float numbers





if __name__ == '__main__':
    print('this is a test of numpy from "http://www.labri.fr/perso/nrougier/teaching/numpy.100/"', '\n\n')












