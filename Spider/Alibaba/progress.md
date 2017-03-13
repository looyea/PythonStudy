首先通过网页直接获取所有其北京方面的内容

工作内容列表地址是:
https://job.alibaba.com/zhaopin/socialPositionList/doList.json?pageSize=960

其中pageSize自己定义, 这里定义成960, 其实完全可以定义成1000, 甚至更多,
但是出于职业道德方面的考虑, 暂时不予进行那么多的内容处理

实际抓取的结果, 每页最多500条! 所以需要多次抓取


经过测试, 抓取出来的数据, 都是完整的JSON结构, 需要后端处理一下才可以使用.
好处是, 可以直接插入MongoDB数据库了.