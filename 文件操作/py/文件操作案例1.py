#需求：给定一批文件，将不同文件后缀的文件移动到同一个文件夹下，文件夹名称为后缀名，并生产一个txt格式的文件清单
#0、获取所有的文件名称列表
import os
import shutil
# os.chdir('文件操作')  #切换目录到文件操作下，当前已经是的了，故本条多余
fileNameList = os.listdir() #获取当前文件所在目录的所有文件名，返回文件名列表（如果目录是一个文件夹，且文件夹里还有子文件或文件夹，这些文件不会被列入列表）
#1、遍历所有的文件
fileName: str    #添加类型提示，解决了部分情况下不出现方法提示的情况
for fileName in fileNameList:
    # print(fileName, type(fileName))
    index = fileName.rfind('.')
    # print(index)
#    #1、分解文件名，找到文件后缀
#     fileName.rfind()
    #2、判断是否存在文件后缀的文件夹
    foldName = fileName[index + 1:]
    if index == -1:
        continue
    # print(foldName)
    #存在，则移动过去
    #不存在，创建并移动
    if not os.path.exists(foldName):
        os.mkdir(foldName)
    shutil.move(fileName,foldName) #导入shutil，调用里面的move方法





#2、生成.txt格式的文件清单
