#生成.txt格式的文件清单
#遍历打印函数：
import os
path = 'D:\PythonDemo'
def fileNamePrint(dir):
    fileLst = os.listdir(dir)
    for fileName in fileLst:
        new_file_name = dir + '/' + fileName
        if os.path.isdir(new_file_name):
            print(new_file_name)
            fileNamePrint(new_file_name)
        else:
            print('\t' +fileName)


os.chdir(path)
fileNamePrint('文件操作')