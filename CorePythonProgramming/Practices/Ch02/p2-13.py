# _*_ coding:utf-8 _*_
"""
利用dir()找出sys模块中更多的东西。
（a）启动Python交互解释器，执行dir()函数，然后键入import sys以导入sys模块。再次执行 dir()函数以确认sys模块被正确的导入。
然后执行dir（sys）,你就可以看到sys模块的所有属性了。
（b）显示sys模块的版本号属性及平台变量。记住在属性名前一定要加sys.,这表示这个属性是sys模块的。
其中version变量保存着你使用的Python解释器版本，platform属性则包含你运行Python时使用的计算机平台信息。
（c）最后，调用sys.exit()函数。这是一种热键之外的另一种退出Python解释器的方式。
"""

"""
dir(sys)
['__displayhook__', 输出对象到系统标准输出中, 然后保存在__builtin__._对象中
 '__doc__', 文档对象
 '__excepthook__', 处理异常, 并且打印追踪信息到sys.stderr上
 '__name__',
 '__package__',
 '__stderr__',
 '__stdin__',
 '__stdout__',
 '_clear_type_cache', 清楚内部类型查询缓存
 '_current_frames', 返回一个字典, 里面映射了所有的线程还有当前线程的id, 只是用做特殊用途
 '_getframe',  返回当前调用堆栈的针, 可以给返回的深度(整数) 作为参数, 但是不能超过堆栈本身的深度. 默认深度是0
 '_mercurial', 返回的是当前系统用的python解释器种类,
 'api_version', api版本
 'argv', 运行命令行的时候, 输入的参数数列,
 'builtin_module_names',打印出所有内建函数列表
 'byteorder',   不知道啥意思
 'call_tracing',  call_tracing(func, args)用来保存调试栈信息的内容
 'callstats', callstats()
 'copyright',
 'displayhook',
 'dllhandle',
 'dont_write_bytecode',
 'exc_clear',
 'exc_info',
 'exc_type',
 'excepthook',
 'exec_prefix',
 'executable',
 'exit',
 'flags',
 'float_info',
 'float_repr_style',
 'getcheckinterval',
 'getdefaultencoding',
 'getfilesystemencoding',
 'getprofile',
 'getrecursionlimit',
 'getrefcount',
 'getsizeof',
 'gettrace',
 'getwindowsversion',
 'hexversion',
 'long_info',
 'maxint',
 'maxsize',
 'maxunicode',
 'meta_path',
 'modules',
 'path',
 'path_hooks',
 'path_importer_cache',
 'platform', 平台变量
 'prefix',
 'ps1',
 'ps2',
 'ps3',
 'py3kwarning',
 'setcheckinterval',
 'setprofile',
 'setrecursionlimit',
 'settrace',
 'stderr',
 'stdin',
 'stdout',
 'subversion', 子版本
 'version', 版本
 'version_info', 版本信息
 'warnoptions',
 'winver']
"""