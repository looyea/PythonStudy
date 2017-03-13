districts = [u"东城",u"西城",u"朝阳",u"海淀",u"昌平",u"房山",u"大兴",u"顺义",u"通州",u"密云",u"丰台",u"怀柔",u"延庆",u"石景山", u"门头沟"]

addr = u"石景山八角北里31号楼"

for dist in districts:
    if addr.find(dist) >= 0:
        print("good")
    else:
        print("bad")

#
# aDict = {"dist":"haha"}
# if "a" in aDict:
#     print("good")
# else:
#     print("bad")