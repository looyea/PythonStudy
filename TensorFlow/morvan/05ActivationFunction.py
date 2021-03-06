# *.* coding=utf-8 *.*

import tensorflow as tf


'''
激励函数，就是针对某一方面的有反应的方程
方程在不同条件下表现的内容不一样。有时候，有很高的值，有时候有很低的值
常见的激励方程有：
1、线性方程
2、分段函数
3、Ramp方程
4、Sigmoid函数
5、arttan三角函数
6、标准正态分布
不同的激励函数，解决的问题不同

激励方程，一般都是在layer2以后，在起将要输出的值，经过激励方程，看看哪些
需要被激励，哪些不需要。剩下的就被传入到下一步的预测值。

不过在tensorflow中有有预定义的激励方程，可以google下，当然先翻墙

tf.nn.relu ＜0 = 0 》0 变成线性关系了
relu6 升级，但是不常用
tf.nn.softplus 分类
dropout减少过拟合影响
sigmoid
tanh 某些问题上方式
以上这些都是为了解决非线性的问题。

那么之后的例子中会应用到这些内容！
'''

