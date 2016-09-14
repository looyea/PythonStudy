# _*_ coding:utf-8 _*_
"""
2-12.dir()内建函数。
（a）启动Python交互式解释器，通过直接键入dir()回车以执行dir()内建函数。
你看到什么？显示你看到的每一个列表元素的值，记下实际值和你想像的值。
答:
['In', 应该是输入, 累计输入了的命令列表
 'Out', 应该是输出, 累计输入命令之后输出的内容
 '_', 不知道, 上一条命令
 '_1', 不知道, 正确格式是_n是指顺序下来输出的第几条命令
 '__', 不知道,
 '___', 不知道
 '__builtin__', 内建的module?
 '__builtins__', 内奸module的集合?
 '__doc__', 文档对象
 '__name__', 当前模块名称对象, 目前是__main__
 '_dh', 不知道, 用户主目录
 '_i', 不知道
 '_i1', 不知道, 正确的格式是_in, 其中n对应顺序输入命令的次序, _in,则是直接输入那条命令,并且给出结果
  '_ih', 不知道
 '_ii', 不知道
 '_iii', 不知道
 '_oh', 不知道
 '_sh', 不知道
 'exit', 貌似是退出, 退出
 'get_ipython', 不知道,<bound method TerminalInteractiveShell.get_ipython of <IPython.terminal.interactiveshell.TerminalInteractiveShell object at 0x0000000003507588>>
 'quit']  貌似是退出, 退出

（b）你会问，dir()函数是干什么的？
我们已经知道在dir后边加上一对括号可以执行dir()内建函数，如果不加括号会如何？
试一试。
解释器返回给你什么信息？你认为这个信息表示什么意思？
答: 不加括号返回一个类型<function dir>, 表示dir是个函数

（c） type()内建函数接收任意的Python对象作为参数并返回他们的类型。
在解释器中键入 type（dir）,看看你得到的是什么？
答: builtin_function_or_method

（d）本练习的最后一部分，我们来瞧一瞧Python的文档字符串。
通过dir._doc_可以访问dir()内建函数的文档字符串。
print dir.__doc__可以显示这个字符串的内容。
许多内建函数、方法、模块及模块属性都有相应的文档字符串。
我们希望你在你的代码中也要书写文档字符串，它会对使用这些代码的人提供及时方便的帮助。
答:
"dir([object]) -> list of strings
If called without an argument, return the names in the current scope.
如果不适用参数调用, 那么就返回当前上下文的各个名称
Else, return an alphabetized list of names comprising (some of) the attributes
否则, 返回给定对象的所有构成属性名称和可访问的列表, 列表是名字的字母序排列.
of the given object, and of attributes reachable from it.
If the object supplies a method named __dir__, it will be used; otherwise
如果对象提供了__dir__, 就是使用对象的dir. 否则:
the default dir() logic is used and returns:
默认的dir方法的逻辑是如下内容:
  for a module object: the module's attributes.
  对于module对象, 是module的属性
  for a class object:  its attributes, and recursively the attributes of its bases.
  对于类对象, 是它的属性, 还有迭代访问其基类内容
  for any other object: its attributes, its class's attributes, and recursively the attributes of its class's base classes."
  对于其他对象,就是属性, 类属性, 还有迭代访问其各个基类属性
"""

