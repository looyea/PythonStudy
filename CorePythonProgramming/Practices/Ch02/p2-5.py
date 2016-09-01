# _*_ coding:utf-8 _*_

print "while without range"
i = 0
while i <= 10:
    print i,
    i+=1
print
print "for without range"
for x in [0,1,2,3,4,5,6,7,8,9,10]:
    print x,
print
print "while with range"
alist = range(0, 11)
i = 0
while i < len(alist):
    print alist[i],
    i += 1
print
print "for with range"
for x in alist:
    print x,

