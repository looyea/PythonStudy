

urls = ["http://test.com/?a={0}".format(str(i) ) for i in range(1,3) ]

for url in urls:
    print url