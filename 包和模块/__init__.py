#导入包的时候会执行这个文件里面的内容
#import M
#import M1, M2
#import M as p     导入模块，并把该模块起别名p
#import package   在__init__.py 文件中写import package.M
#from A import B as C   从A中导入B，并起个别名C
#from A import *      在A中写__all__=['主动告知导入者有用的模块部分1'，'主动告知导入者有用的模块部分2']（不写则默认导入所有非'_'开头的资源）    不建议使用
#from package import *      在__init__.py文件中中写__all__=['主动告知导入者有用的模块部分1'，'主动告知导入者有用的模块部分2']    不建议使用
#from . import M     从当前文件的上一级导入M    （脚本运行不可用）
#from .. import M     从当前文件的上上一级导入M   （脚本运行不可用）
#import M  第一次导入的时候，会在自己当下的命名空间执行M中的代码，并在当前命名空间创建一个模块对象M，将M中的顶层（最外层）属性和方法以属性的形式绑定到对象M中，在
#import的位置将import后面的变量名称引入到当前命名空间
#第二次导入，直接执行：import的位置将import后面的变量名称引入到当前命名空间
#查找顺序：内置模块——>sys.path列表顺序查找
#追加查找路径的三种方式：
#1、直接修改sys.path
#2、修改环境变量（仅在shell中可用，pycharm需要在setting里面改）
#3、添加.path文件
import site
print(site.getsitepackages())   #打印可添加path文件的地方
#在该地方添加path文件，文件内写需要添加的查找路径


#相对导入：用.来代替相对路径   包内导入使用较好
#绝对导入：指明包名和模块名    包外导入使用较好