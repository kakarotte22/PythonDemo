import jieba
from sklearn.datasets.base import Bunch
seg_list = jieba.cut('小明1995年毕业于北京清华大学', cut_all=False)   #采用精准模式分词
print(type(seg_list))   #jieba.cut()得到的是一个生成器对象
print('//'.join(seg_list))    #Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
seg_list1 = jieba.cut('小明1995年毕业于北京清华大学', cut_all=True)   #采用整体模式分词
print('//'.join(seg_list1))
seg_list2 = jieba.cut_for_search('小明硕士毕业于中国科学院计算机所，后再日本京都大学深造')   #采用搜索引擎模式分词
print('//'.join(seg_list2))
