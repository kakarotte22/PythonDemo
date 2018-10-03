import svdRec
import numpy as np
from svdRec import svdRec
from numpy import *

A = np.array([[5, 5, 3, 0, 5, 5], [5, 0, 0, 0, 0, 0], [0, 3, 0, 5, 4, 5], [5, 4, 3, 3, 5, 5]])  #A的形状(6,4)
A = mat(A)
userIdName = {1: 'user1', 2: 'user2', 3: 'user3', 4: 'user4'}
itemDic = {'item1': 'i1', 'item2': 'i2', 'item3': 'i3', 'item4': 'i4', 'item5': 'i5', 'item6': 'i6'}
sc = svdRec.svdRec()
sc.load_data_numpy(A)
sc.load_item_encoder(itemDic)
sc.load_user_encoder(userIdName)
sc.SVD(2)
recommandItemId = sc.recommends_for_user(2, num_recom=2, show_similarity=True)
# recommandItemName = sc.get_item_name(recommandItemId[0])
# print(recommandItemId[0], type(recommandItemId[0]))
print(recommandItemId, type(recommandItemId))
