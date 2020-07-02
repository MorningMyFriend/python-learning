# coding=utf-8

import os
import numpy as np
import time
from time import sleep


def bubble_sort(nums):
    if len(nums)<2:
        return nums
    for i in range(len(nums)):
        for j in range(1, len(nums)-i):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return nums

def selecttion_sort(nums):
    return nums

def insertion_sort(nums):
    return nums


def quick_sort(nums):
    return nums


def main():
    nums = [1,5,6,3,9,2,7,8,4]
    print(nums)
    nums = bubble_sort(nums)
    print(nums)



def decorate(func):
    def clocked(a, b):
        t1 = time.time()
        c = func(a, b)
        t2 = time.time()
        print('clocked>>> time use:', t2-t1)
        return c
    return clocked 
        
    
    
@decorate    
def pause(a, b):
    print('pause>>>')
    sleep(1)
    return a+b
    
    
def test():
    
    a = 'abc'
    b = 'bcd'
    print(id(a[1]))
    print(id(b[0]))
    

if __name__ == '__main__':
    # main()
    test()
    