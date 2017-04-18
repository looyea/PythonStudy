# _*_ coding:utf-8 _*_

import random

def generateRandomArray(length, arrLowerBound, arrUpperBound):
    if not length:
        length = 10
    if not arrLowerBound:
        arrLowerBound = 0
    if not arrUpperBound:
        arrUpperBound = 0
    index = 0
    while index < length:
        yield random.randint(arrLowerBound,arrUpperBound)
        index += 1

def getDefaultArray(needPrintArray):
    sortArray = generateRandomArray(10, 0, 20)
    if needPrintArray:
        printArray(sortArray)
    return sortArray

def printArray(array):
    print u"当前数组内容：",
    for a in array:
        print a,
    print "\n"

if __name__ == "main":
    pass