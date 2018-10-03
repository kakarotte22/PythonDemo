# Python中存储系列数据，比较常见的数据类型有list，除此之外，还有tuple数据类型。相比与list，tuple中的元素不可修改，在映射中可以当键使用。
# tuple元组的item只能通过index访问，collections模块的namedtuple子类不仅可以使用item的index访问item，还可以通过item的name进行访问。
# 可以将namedtuple理解为c中的struct结构，其首先将各个item命名，然后对每个item赋予数据。

from collections import namedtuple

websites = [
    ('Sohu', 'http://www.google.com/', u'张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊')
]

Website = namedtuple('Website', ['name', 'url', 'founder'])

for website in websites:
    website = Website._make(website)
    print(website)
print(Website.name)