#需求：将一个图片信息的钱半部分写入到另一个文件中
#1、打开文件，取出文件前半部分
#1.1 打开源文件
fromFile = open('顺序.png', 'rb')
#1.2 取出前半部分数据
fromContent = fromFile.read()
content = fromContent[0:len(fromContent) // 2]
#1.3 关闭文件
fromFile.close()



#2、打开另一个文件，将取出的内容写入
#2.1 打开目标文件
toFile = open('顺序一半.png', 'wb')
#2.2 将取出前半部分数据写入到目标文件
toFile.write(content)
#2.3 关闭文件
toFile.close()
