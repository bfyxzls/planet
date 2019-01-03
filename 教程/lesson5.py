# 打开一个文件
f = open("foo.txt", "w")
f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
f = open("foo.txt", "r")
str = f.read()
print(str)
# 关闭打开的文件
f.close()


import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'name': '张三',
         'score':100,
         'life': 87
         }
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('data.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
output.close()

import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
print("data1.name:", pprint.pprint(data1).name)
pprint.pprint(data1)
data2 = pickle.load(pkl_file)
print("data2")
pprint.pprint(data2)
pkl_file.close()