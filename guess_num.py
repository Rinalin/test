#!/user/bin/env python
# -*- coding:utf-8 -*-
#计算机给出1-100的随机数，人来猜
import  random

random_num = random.randint(1,100)
print(random_num)
enter_num = int(input("请输入您猜的数字："))

while (random_num != enter_num ):
    if (random_num>enter_num):
        print("too small")
        enter_num = int(input("请输入您猜的数字："))
    if (random_num < enter_num):
        print("too large")
        enter_num = int(input("请输入您猜的数字："))
print("bingo")
1
