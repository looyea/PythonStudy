# _*_ coding:utf-8 _*_
'''
N个元素,每次挑出最大或者最小,执行(n-1)次循环。实际上选择排序是最简单的一种排序算法，因为它的思想非常朴素，每趟都选出剩余中最大或者最小的排在已经排好的数据后面。

直接排序处理流程：

从待排序序列中，找到关键字最小的元素；
如果最小元素不是待排序序列的第一个元素，将其和第一个元素互换；
从余下的 N - 1 个元素中，找出关键字最小的元素，重复1，2步，直到排序结束。
'''

dataList =[8,4,2,6,5,7,1,0,3,9]

i = 0
dLen = len(dataList)

while (i < dLen):
    j = i + 1

    # 以下是另外一种查找的办法, 直接找最小值的标记，如果发现标记值比当前值还小，就新设置最小标记
    minIndex, oldMinIndex = i, i

    while (j < dLen):
        if dataList[j] < dataList[minIndex]:
            minIndex = j
            # print minIndex, dataList[minIndex]
        j += 1
    dataList[i], dataList[minIndex] = dataList[minIndex], dataList[i]

    print dataList
    i += 1