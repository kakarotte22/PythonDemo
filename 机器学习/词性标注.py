import jieba.posseg as pesg
segList = pesg.cut('把这篇报道修改一下。', HMM=True)   #带词性模式,隐马可夫模型,jieba.cut只是分词，不带词性
for word in segList:
    print(word)
